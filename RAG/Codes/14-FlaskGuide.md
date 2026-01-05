# YouTube Summarizer & Q&A - Flask API Transformation Guide

## Overview

This guide explains how to transform the Gradio-based YouTube Summarizer application into a Flask REST API web service.

## Current Application

The current application (`14-YTSummarizer.py`) is a Gradio-based web interface that:
- Fetches transcripts from YouTube videos
- Generates AI-powered summaries using IBM Watsonx AI
- Answers questions about video content using RAG (Retrieval-Augmented Generation)
- Uses FAISS for vector storage and similarity search

## Prerequisites

- Python 3.8+
- IBM Watsonx AI account with API credentials
- `.env` file with the following variables:
  ```
  PROJECT_ID=your_project_id
  API_KEY=your_api_key
  URL=your_watsonx_url
  ```

## Dependencies

### Current Dependencies
```txt
gradio
youtube-transcript-api
langchain
langchain-ibm
langchain-community
ibm-watsonx-ai
faiss-cpu
python-dotenv
```

### Additional Dependencies for Flask API
```txt
flask
flask-cors
```

## Flask API Architecture

### Recommended Structure

```
RAG/Codes/
├── 14-YTSummarizer.py (original)
├── flask_api/
│   ├── app.py                  # Main Flask application
│   ├── core/
│   │   ├── __init__.py
│   │   ├── transcript.py       # Transcript fetching logic
│   │   ├── summarizer.py       # Summary generation logic
│   │   └── qa_engine.py        # Q&A logic
│   ├── routes/
│   │   ├── __init__.py
│   │   └── api.py              # API endpoints
│   ├── utils/
│   │   ├── __init__.py
│   │   └── validators.py       # Input validation
│   └── config.py               # Configuration management
├── requirements.txt
├── .env
└── README.md
```

## Step-by-Step Transformation

### Step 1: Install Flask Dependencies

```bash
pip install flask flask-cors
```

### Step 2: Create Flask Application Structure

Create the main Flask app file `flask_api/app.py`:

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

# Import routes
from routes.api import api_blueprint
app.register_blueprint(api_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### Step 3: Extract Core Functions

Create `flask_api/core/transcript.py`:

```python
import re
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    """Extract YouTube video ID from URL"""
    pattern = r'https:\/\/www\.youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_transcript(url):
    """Fetch transcript from YouTube video"""
    video_id = get_video_id(url)
    if not video_id:
        return None
    
    ytt_api = YouTubeTranscriptApi()
    transcripts = ytt_api.list(video_id)
    
    transcript = ""
    for t in transcripts:
        if t.language_code == 'en':
            if t.is_generated:
                if len(transcript) == 0:
                    transcript = t.fetch()
            else:
                transcript = t.fetch()
                break
    
    return transcript if transcript else None

def process_transcript(transcript):
    """Format transcript into readable text"""
    txt = ""
    for i in transcript:
        try:
            txt += f"Text: {i['text']} Start: {i['start']}\n"
        except KeyError:
            pass
    return txt
```

Create `flask_api/core/summarizer.py`:

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ibm import WatsonxLLM
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from ibm_watsonx_ai import Credentials
import os

def setup_credentials():
    """Setup IBM Watsonx credentials"""
    model_id = "meta-llama/llama-3-3-70b-instruct"
    credentials = Credentials(
        url=os.getenv("URL"),
        api_key=os.getenv("API_KEY")
    )
    project_id = os.getenv("PROJECT_ID")
    return model_id, credentials, project_id

def create_summary_prompt():
    """Create prompt template for summarization"""
    template = """
    <|begin_of_text|><|start_header_id|>system<|end_header_id|>
    You are an AI assistant tasked with summarizing YouTube video transcripts.
    Provide concise, informative summaries that capture the main points.
    <|eot_id|><|start_header_id|>user<|end_header_id|>
    Please summarize the following YouTube video transcript:
    {transcript}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
    """
    return PromptTemplate(input_variables=["transcript"], template=template)

def generate_summary(processed_transcript):
    """Generate summary from processed transcript"""
    model_id, credentials, project_id = setup_credentials()
    
    llm = WatsonxLLM(
        model_id=model_id,
        url=credentials.get("url"),
        project_id=project_id,
        params={"max_new_tokens": 1000},
        apikey=os.getenv("API_KEY")
    )
    
    summary_prompt = create_summary_prompt()
    summary_chain = LLMChain(llm=llm, prompt=summary_prompt)
    
    return summary_chain.run({"transcript": processed_transcript})
```

Create `flask_api/core/qa_engine.py`:

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ibm import WatsonxLLM, WatsonxEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

def chunk_transcript(processed_transcript, chunk_size=200, chunk_overlap=20):
    """Split transcript into chunks"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return text_splitter.split_text(processed_transcript)

def create_faiss_index(chunks, credentials, project_id):
    """Create FAISS index from chunks"""
    embedding_model = WatsonxEmbeddings(
        model_id='ibm/slate-30m-english-rtrvr-v2',
        url=credentials["url"],
        project_id=project_id,
        apikey=os.getenv("API_KEY")
    )
    return FAISS.from_texts(chunks, embedding_model)

def create_qa_prompt_template():
    """Create Q&A prompt template"""
    qa_template = """
    You are an expert assistant providing detailed answers based on video content.
    Relevant Video Context: {context}
    Question: {question}
    """
    return PromptTemplate(
        input_variables=["context", "question"],
        template=qa_template
    )

def answer_question(processed_transcript, question, credentials, project_id):
    """Generate answer to question using RAG"""
    chunks = chunk_transcript(processed_transcript)
    faiss_index = create_faiss_index(chunks, credentials, project_id)
    
    llm = WatsonxLLM(
        model_id="meta-llama/llama-3-3-70b-instruct",
        url=credentials.get("url"),
        project_id=project_id,
        params={"max_new_tokens": 2000, "min_new_tokens": 50},
        apikey=os.getenv("API_KEY")
    )
    
    qa_prompt = create_qa_prompt_template()
    qa_chain = LLMChain(llm=llm, prompt=qa_prompt)
    
    relevant_context = faiss_index.similarity_search(question, k=7)
    answer = qa_chain.predict(context=relevant_context, question=question)
    
    return answer
```

### Step 4: Create API Routes

Create `flask_api/routes/api.py`:

```python
from flask import Blueprint, request, jsonify
from core.transcript import get_transcript, process_transcript
from core.summarizer import generate_summary, setup_credentials
from core.qa_engine import answer_question

api_blueprint = Blueprint('api', __name__)

# Cache for transcripts (consider using Redis in production)
transcript_cache = {}

@api_blueprint.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "YouTube Summarizer API"}), 200

@api_blueprint.route('/transcript', methods=['POST'])
def fetch_transcript():
    """Fetch and return YouTube video transcript"""
    data = request.get_json()
    
    if not data or 'video_url' not in data:
        return jsonify({"error": "video_url is required"}), 400
    
    video_url = data['video_url']
    
    try:
        # Check cache first
        if video_url in transcript_cache:
            return jsonify({
                "video_url": video_url,
                "transcript": transcript_cache[video_url],
                "cached": True
            }), 200
        
        # Fetch transcript
        fetched_transcript = get_transcript(video_url)
        if not fetched_transcript:
            return jsonify({"error": "Could not fetch transcript"}), 404
        
        processed = process_transcript(fetched_transcript)
        
        # Cache the result
        transcript_cache[video_url] = processed
        
        return jsonify({
            "video_url": video_url,
            "transcript": processed,
            "cached": False
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_blueprint.route('/summarize', methods=['POST'])
def summarize():
    """Generate summary of YouTube video"""
    data = request.get_json()
    
    if not data or 'video_url' not in data:
        return jsonify({"error": "video_url is required"}), 400
    
    video_url = data['video_url']
    
    try:
        # Get or fetch transcript
        if video_url in transcript_cache:
            processed_transcript = transcript_cache[video_url]
        else:
            fetched_transcript = get_transcript(video_url)
            if not fetched_transcript:
                return jsonify({"error": "Could not fetch transcript"}), 404
            processed_transcript = process_transcript(fetched_transcript)
            transcript_cache[video_url] = processed_transcript
        
        # Generate summary
        summary = generate_summary(processed_transcript)
        
        return jsonify({
            "video_url": video_url,
            "summary": summary
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_blueprint.route('/ask', methods=['POST'])
def ask_question():
    """Answer question about YouTube video content"""
    data = request.get_json()
    
    if not data or 'video_url' not in data or 'question' not in data:
        return jsonify({"error": "video_url and question are required"}), 400
    
    video_url = data['video_url']
    question = data['question']
    
    try:
        # Get or fetch transcript
        if video_url in transcript_cache:
            processed_transcript = transcript_cache[video_url]
        else:
            fetched_transcript = get_transcript(video_url)
            if not fetched_transcript:
                return jsonify({"error": "Could not fetch transcript"}), 404
            processed_transcript = process_transcript(fetched_transcript)
            transcript_cache[video_url] = processed_transcript
        
        # Setup credentials
        _, credentials, project_id = setup_credentials()
        
        # Generate answer
        answer = answer_question(processed_transcript, question, credentials, project_id)
        
        return jsonify({
            "video_url": video_url,
            "question": question,
            "answer": answer
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
```

### Step 5: Create Configuration File

Create `flask_api/config.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    PROJECT_ID = os.getenv('PROJECT_ID')
    API_KEY = os.getenv('API_KEY')
    URL = os.getenv('URL')
    
    # IBM Watsonx settings
    WATSONX_MODEL_ID = "meta-llama/llama-3-3-70b-instruct"
    EMBEDDING_MODEL_ID = 'ibm/slate-30m-english-rtrvr-v2'
    
    # Chunking parameters
    CHUNK_SIZE = 200
    CHUNK_OVERLAP = 20
    
    # RAG parameters
    SIMILARITY_TOP_K = 7

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

## API Endpoints

### 1. Health Check
```http
GET /api/health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "YouTube Summarizer API"
}
```

### 2. Fetch Transcript
```http
POST /api/transcript
Content-Type: application/json

{
  "video_url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
```

**Response:**
```json
{
  "video_url": "https://www.youtube.com/watch?v=VIDEO_ID",
  "transcript": "Text: ... Start: 0.0\n...",
  "cached": false
}
```

### 3. Summarize Video
```http
POST /api/summarize
Content-Type: application/json

{
  "video_url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
```

**Response:**
```json
{
  "video_url": "https://www.youtube.com/watch?v=VIDEO_ID",
  "summary": "This video discusses..."
}
```

### 4. Ask Question
```http
POST /api/ask
Content-Type: application/json

{
  "video_url": "https://www.youtube.com/watch?v=VIDEO_ID",
  "question": "What is the main topic of the video?"
}
```

**Response:**
```json
{
  "video_url": "https://www.youtube.com/watch?v=VIDEO_ID",
  "question": "What is the main topic of the video?",
  "answer": "Based on the video content..."
}
```

## Running the Flask API

### Development Mode
```bash
cd flask_api
python app.py
```

The API will be available at `http://localhost:5000`

### Production Mode (using Gunicorn)

Install Gunicorn:
```bash
pip install gunicorn
```

Run the application:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Testing the API

### Using cURL

**Health Check:**
```bash
curl http://localhost:5000/api/health
```

**Summarize Video:**
```bash
curl -X POST http://localhost:5000/api/summarize \
  -H "Content-Type: application/json" \
  -d '{"video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

**Ask Question:**
```bash
curl -X POST http://localhost:5000/api/ask \
  -H "Content-Type: application/json" \
  -d '{
    "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "question": "What is this video about?"
  }'
```

### Using Python Requests

```python
import requests

BASE_URL = "http://localhost:5000/api"

# Summarize video
response = requests.post(
    f"{BASE_URL}/summarize",
    json={"video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
)
print(response.json())

# Ask question
response = requests.post(
    f"{BASE_URL}/ask",
    json={
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "question": "What is the main theme?"
    }
)
print(response.json())
```

## Enhancements & Best Practices

### 1. Add Request Validation
Use Flask-RESTX or Marshmallow for request validation:
```bash
pip install flask-restx
```

### 2. Implement Caching
Use Redis for distributed caching:
```bash
pip install redis flask-caching
```

### 3. Add Rate Limiting
```bash
pip install flask-limiter
```

### 4. Add Authentication
```bash
pip install flask-jwt-extended
```

### 5. Logging
Add proper logging:
```python
import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
```

### 6. Error Handling
Create custom error handlers:
```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500
```

### 7. Docker Deployment

Create `Dockerfile`:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "5000:5000"
    environment:
      - PROJECT_ID=${PROJECT_ID}
      - API_KEY=${API_KEY}
      - URL=${URL}
    volumes:
      - .:/app
```

## Next Steps

1. **Implement the structure** - Create the directory structure and files
2. **Test locally** - Run and test the Flask API
3. **Add authentication** - Secure your API endpoints
4. **Deploy** - Use Docker, Heroku, AWS, or Google Cloud
5. **Monitor** - Add logging and monitoring tools
6. **Document** - Create OpenAPI/Swagger documentation

## Troubleshooting

### Common Issues

1. **CORS errors**: Make sure `flask-cors` is installed and configured
2. **Environment variables**: Ensure `.env` file is in the correct location
3. **Port conflicts**: Change the port if 5000 is already in use
4. **IBM Watsonx credentials**: Verify your credentials are valid

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-RESTX](https://flask-restx.readthedocs.io/)
- [IBM Watsonx AI Documentation](https://www.ibm.com/docs/en/watsonx-as-a-service)
- [LangChain Documentation](https://python.langchain.com/)

## License

See the main project license.
