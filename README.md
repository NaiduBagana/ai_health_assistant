# ai_health_assistant
##Please watch this video 
A FastAPI-based application that provides an AI-powered health assistant for managing medical appointments, answering health-related questions, and analyzing medical images.

## Features

- 💬 Text-based chat interface for medical queries
- 🗣️ Voice-to-text input processing
- 📅 Appointment scheduling, modification, and cancellation
- 📧 Email notifications for appointment confirmations and updates
- 🖼️ Medical image analysis with OpenAI vision capabilities

## Project Structure

```
ai-health-assistant/
├── app.py               # FastAPI application with all endpoints
├── assistant.py         # Core AI assistant functionality and agent setup
├── models.py            # Data models and storage logic
├── utils.py             # Utility functions for date parsing and email
├── main.py              # Command-line interface for testing
└── .env                 # Environment variables (create this)
```

## Prerequisites

- Python 3.8+
- FFmpeg (for audio processing)
- OpenAI API key
- SMTP server access for email notifications

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ai-health-assistant.git
   cd ai-health-assistant
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install fastapi uvicorn pydantic langchain langchain_openai openai python-dotenv python-multipart pydub
   ```

4. Install FFmpeg:
   - **macOS**: `brew install ffmpeg`
   - **Ubuntu/Debian**: `sudo apt-get install ffmpeg`
   - **Windows**: Download from [FFmpeg official website](https://ffmpeg.org/download.html)

## Configuration

Create a `.env` file in the project root with the following variables:

```
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# Email Configuration
EMAIL_SENDER=your_email@example.com
SMTP_PASSWORD=your_email_password_or_app_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### FFmpeg Path Configuration

If FFmpeg is not in your system PATH, update the path in `app.py`:

```python
# Update this line with your FFmpeg path
AudioSegment.converter = "/path/to/ffmpeg"
```

## Running the Application

### Command Line Interface

For testing the assistant without the API:

```bash
python main.py
```

### Web API

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The API will be available at http://localhost:8000

Interactive API documentation is available at:
- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)

## API Endpoints

### Chat

- **POST** `/chat`
  - Process text-based chat messages

### Voice Processing

- **POST** `/voice-to-text`
  - Convert audio recordings to text and process with the assistant

### Image Analysis

- **POST** `/analyze-image`
  - Analyze medical images using OpenAI's vision capabilities

### Appointments

- **POST** `/appointments`
  - Create a new appointment
- **GET** `/appointments/{user_id}`
  - List all appointments for a user
- **PUT** `/appointments/{appointment_id}`
  - Update an existing appointment
- **DELETE** `/appointments/{appointment_id}`
  - Cancel an appointment

## Usage Examples

### Chat Interaction

```python
import requests
import json

response = requests.post(
    "http://localhost:8000/chat",
    json={"user_id": "user123", "message": "What's the best way to treat a mild headache?"}
)
print(response.json()["response"])
```

### Schedule an Appointment

```python
import requests
from datetime import datetime, timedelta

# Schedule for tomorrow
appointment_time = (datetime.now() + timedelta(days=1)).isoformat()

response = requests.post(
    "http://localhost:8000/appointments",
    json={
        "user_id": "user123",
        "date_time": appointment_time,
        "purpose": "Annual check-up",
        "email": "patient@example.com"
    }
)
print(json.dumps(response.json(), indent=2))
```

### Voice Input

```python
import requests

with open("audio_recording.m4a", "rb") as f:
    files = {"audio_file": f}
    data = {"user_id": "user123"}
    response = requests.post("http://localhost:8000/voice-to-text", files=files, data=data)

print(response.json()["transcribed_text"])
print(response.json()["response"])
```

### Image Analysis

```python
import requests

with open("medical_image.jpg", "rb") as f:
    files = {"image_file": f}
    data = {
        "user_id": "user123", 
        "prompt": "What can you tell me about this skin rash?"
    }
    response = requests.post("http://localhost:8000/analyze-image", files=files, data=data)

print(response.json()["analysis"])
```

## Architecture

The application uses:

1. **FastAPI** - For the REST API endpoints
2. **LangChain** - For orchestrating the AI workflows
3. **OpenAI GPT-4 Turbo** - For natural language understanding and generation
4. **OpenAI Whisper** - For speech-to-text conversion
5. **OpenAI Vision** - For medical image analysis
6. **Pydantic** - For data validation and settings management

## Security Considerations

- This application handles sensitive medical information. In a production environment, implement proper authentication, authorization, and encryption.
- Store API keys and credentials securely, never in the code.
- Consider HIPAA compliance requirements if deploying in the US healthcare context.

## Future Improvements

- Add user authentication system
- Implement persistent storage with a database
- Add health records management
- Integrate with calendaring systems
- Add follow-up reminders
- Implement real-time chat with WebSockets

## License

[MIT License]

## Acknowledgements

- OpenAI for the GPT and Whisper models
- FastAPI for the web framework
- LangChain for the agent framework
