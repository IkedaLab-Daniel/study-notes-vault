import re
from pytube import YouTube
from langchain_core.tools import tool
import yt_dlp
from typing import List, Dict
from langchain_core.messages import HumanMessage, ToolMessage
import json

# > Suppress Warnings
import warnings
warnings.filterwarnings("ignore")

# > Suppress pytube errors
import logging
pytube_logger = logging.getLogger("pytube")
pytube_logger.setLevel(logging.ERROR)

# > Supress py-dlp warnings
yt_dlp_logger = logging.getLogger("yt_dlp")
pytube_logger.setLevel(logging.ERROR)

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

llm = init_chat_model(
    "llama-3.1-8b-instant", 
    model_provider="groq",
    api_key=os.getenv("GROQ_API")
)

### -- Defining video ID extractor tool -- ###
@tool
def extract_video_id(url: str) -> str:
    """
    Extracts the 11-character YouTube video ID from a URL.
    
    Args:
        url (str): A YouTube URL containing a video ID.

    Returns:
        str: Extracted video ID or error message if parsing fails.
    """
    
    # Regex pattern to match video IDs
    pattern = r'(?:v=|be/|embed/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else "Error: Invalid YouTube URL"

print(extract_video_id.name)
print("----------------------------")
print(extract_video_id.description)
print("----------------------------")
print(extract_video_id.func)

print(extract_video_id.run("https://www.youtube.com/watch?v=hfIUstzHs9A"))