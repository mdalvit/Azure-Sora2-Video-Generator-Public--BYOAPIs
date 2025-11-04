# Sora2 Video Generator

A lightweight Flask web application with Microsoft Fluent Design UI for generating videos using Azure's Sora2 API.

## Features

- 🎨 Clean, modern UI with Microsoft Fluent Design
- 🎥 Generate videos from text prompts using Sora2
- ⚙️ Customizable video size and duration
- 🔐 Secure API key authentication
- 📱 Responsive design for mobile and desktop

## Prerequisites

- Python 3.8 or higher
- Azure Sora2 API endpoint and API key

## Installation

1. Clone or download this repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
   - Copy `.env.example` to `.env`
   - Edit `.env` and add your Azure credentials:
```
AZURE_ENDPOINT_URL=<your-endpoint-url>
AZURE_API_KEY=<your-api-key>
```

## Running the Application

### Option 1: Using Python directly
```bash
python app.py
```

### Option 2: Using Flask CLI
```bash
flask run
```

The application will be available at `http://localhost:5000`

## Usage

1. Open your browser and navigate to `http://localhost:5000`
2. Enter a description of the video you want to generate in the search box
3. Select your preferred video size and duration
4. Click "Generate Video" or press Enter
5. Wait for the video generation to complete
6. The API response will be displayed below the search box

## Configuration

You can configure the following parameters:

- **Video Size**: Choose from portrait or landscape orientations in various resolutions
  - 720x1280 (Portrait)
  - 1280x720 (Landscape)
  - 1080x1920 (Full HD Portrait)
  - 1920x1080 (Full HD Landscape)

- **Duration**: Select video length from 4 to 10 seconds

## API Integration

The application integrates with Azure's Sora2 API using the following pattern:

```bash
curl -X POST "<your-endpoint-url>" \
  -H "Content-Type: application/json" \
  -H "Api-key: $AZURE_API_KEY" \
  -d '{
     "model": "sora-2",
     "prompt" : "A video of a cat",
     "size" : "720x1280",
     "seconds" : "4"
    }'
```

## Project Structure

```
Sora2_test/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Microsoft Fluent Design UI template
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
└── README.md            # This file
```

## Security Notes

- Never commit your `.env` file with actual API keys to version control
- Keep your Azure API key secure and rotate it regularly
- The `.env` file is gitignored by default

## Troubleshooting

**Issue**: API request fails with 401 Unauthorized
- **Solution**: Verify your API key is correct in the `.env` file

**Issue**: Connection timeout
- **Solution**: Video generation can take time. The timeout is set to 2 minutes. Check your network connection and Azure service status.

**Issue**: Module not found errors
- **Solution**: Make sure you've installed all requirements: `pip install -r requirements.txt`

## License

This project is open source and available for educational and commercial use.
