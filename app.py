import os
import requests
from flask import Flask, render_template, request, jsonify, Response
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

AZURE_API_KEY = os.getenv('AZURE_API_KEY')
AZURE_ENDPOINT_URL = os.getenv('AZURE_ENDPOINT_URL')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_video():
    try:
        data = request.get_json()
        print(f"Received data: {data}")
        
        prompt = data.get('prompt', '') if data else ''
        size = data.get('size', '720x1280') if data else '720x1280'
        seconds = data.get('seconds', '4') if data else '4'
        
        print(f"Prompt: {prompt}, Size: {size}, Seconds: {seconds}")
        
        if not prompt:
            print("Error: No prompt provided")
            return jsonify({'error': 'Prompt is required'}), 400
        
        headers = {'Content-Type': 'application/json', 'api-key': AZURE_API_KEY}
        payload = {'model': 'sora-2', 'prompt': prompt, 'size': size, 'seconds': str(seconds)}
        
        print(f"Calling: {AZURE_ENDPOINT_URL}")
        print(f"Payload: {payload}")
        
        response = requests.post(AZURE_ENDPOINT_URL, headers=headers, json=payload, timeout=120)
        
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")
        
        if response.status_code in [200, 201, 202]:
            video_data = response.json()
            return jsonify({'success': True, 'video_id': video_data.get('id'), 'status': video_data.get('status'), 'data': video_data})
        else:
            return jsonify({'error': 'API request failed', 'details': response.text}), response.status_code
    except Exception as e:
        print(f"Exception: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/status/<video_id>', methods=['GET'])
def check_status(video_id):
    try:
        headers = {'api-key': AZURE_API_KEY}
        response = requests.get(f"{AZURE_ENDPOINT_URL}/{video_id}", headers=headers, timeout=30)
        
        if response.status_code == 200:
            video_data = response.json()
            if video_data.get('status') == 'completed':
                video_data['video_url'] = f"/video/{video_id}"
            return jsonify({'success': True, 'data': video_data})
        else:
            return jsonify({'error': 'Failed to get status', 'details': response.text}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/video/<video_id>', methods=['GET'])
def get_video(video_id):
    try:
        headers = {'api-key': AZURE_API_KEY}
        response = requests.get(f"{AZURE_ENDPOINT_URL}/{video_id}/content", headers=headers, stream=True, timeout=60)
        
        if response.status_code == 200:
            return Response(response.iter_content(chunk_size=8192), content_type='video/mp4')
        else:
            return jsonify({'error': 'Video not available', 'details': response.text}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
