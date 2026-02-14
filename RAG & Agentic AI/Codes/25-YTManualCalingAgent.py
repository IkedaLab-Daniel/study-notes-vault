import re
from pytube import YouTube
from langchain_core.tools import tool
import yt_dlp
from typing import List, Dict
from langchain_core.messages import HumanMessage, ToolMessage
import json
from utils import print_agent

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

### -- Tool list -- ###
tools = []
tools.append(extract_video_id)

### -- Defining transcript fetching tool -- ###
from youtube_transcript_api import YouTubeTranscriptApi

@tool
def fetch_transcript(video_id: str, language: str = "en") -> str:
    """
    Fetches the transcript of a YouTube video.
    
    :param video_id: The YouTube video ID (e.g., "dQw4w9WgXcQ")
    :type video_id: str
    :param language: Language code for the transcript (e.g., "en", "es").
    :type language: str
    :return: The transcript text or an error message.
    :rtype: str
    """

    try:
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id, languages=[language])
        return " ".join([snipper.text for snipper in transcript.snippets])
    except Exception as ICE:
        return f"Error: {str(ICE)}"

# ? Test
# print_agent()
# print(fetch_transcript.run("hfIUstzHs9A"))

tools.append(fetch_transcript)

### -- Defing YouTube search tool -- ###
from pytube import Search

@tool
def search_youtube(query: str) -> List[Dict[str, str]]:
    """
    Search YouTube for videos matching the query.
    
    :param query: The search terrm to look for on YouTube
    :type query: str
    :return: List of disctionaries containing video titles and IDs in format:
        [{'title': 'Video Title', 'video_id': 'abc123'}, ...]
        Returns error message if search fails
    :rtype: List[Dict[str, str]]
    """
    try:
        s = Search(query)
        return [
            {
                "title": yt.title,
                "video_id": yt.video_id,
                "url": f"https://youtu.be/{yt.video_id}"
            }
            for yt in s.results
        ]
    except Exception as ICE:
        return f"Error: {str(ICE)}"
    
# ? Test
search_out = search_youtube.run("Generative AI")
print_agent()
print(search_out)