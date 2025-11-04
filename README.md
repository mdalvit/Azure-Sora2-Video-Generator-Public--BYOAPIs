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
2. Enter a description of the video you want to generate in the text box
3. Select your preferred aspect ratio (16:9 or 9:16)
4. Select the resolution (currently 720p only)
5. Select the video duration (4s, 8s, or 12s)
6. Click "Generate Video" or press Enter
7. Wait for the video generation to complete (may take several minutes)
8. The video will be displayed once generation is complete

## Configuration

You can configure the following parameters:

- **Aspect Ratio**: Choose between landscape or portrait orientation
  - 16:9 (Landscape)
  - 9:16 (Portrait)

- **Resolution**: Currently only 720p is supported
  - 720p (1280x720 for 16:9, 720x1280 for 9:16)

- **Duration**: Select video length
  - 4 seconds
  - 8 seconds
  - 12 seconds

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
