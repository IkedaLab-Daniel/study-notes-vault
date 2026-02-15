import re
from pytube import YouTube, Search
from langchain_core.tools import tool
import yt_dlp
from typing import List, Dict
from langchain_core.messages import HumanMessage, ToolMessage
import json
from utils import print_agent
import pprint

from youtube_transcript_api import YouTubeTranscriptApi

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

### -- Tools -- ###
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

@tool
def get_full_metadata(url: str) -> dict:
    """Extract metadata given a YouTube URL, including title, views, duration, channel, likes, comments, and chapters."""
    with yt_dlp.YoutubeDL({'quiet': True, 'logger': yt_dlp_logger}) as ydl:
        info = ydl.extract_info(url, download=False)
        return {
            'title': info.get('title'),
            'views': info.get('view_count'),
            'duration': info.get('duration'),
            'channel': info.get('uploader'),
            'likes': info.get('like_count'),
            'comments': info.get('comment_count'),
            'chapters': info.get('chapters', [])
        }

# ! NOT WORKING
@tool
def get_thumbnails(url: str) -> List[Dict]:
    """
    Get available thumbnails for a YouTube video using its URL.
    
    :param url: YouTube video URL (any format)
    :type url: str
    :return: List of dicstionaries with thumbnail URLs and resolutions in YouTube's natibve order
    :rtype: List[Dict]
    """

    try:
        with yt_dlp.YoutubeDL({'quiet': True, 'logger': yt_dlp_logger}) as ydl:
            info = ydl.extract_info(url, download=False)

            thumbnails = []

            for t in info.get('thumbnail', []):
                if 'url' in t:
                    thumbnails.append({
                        "url": t['url'],
                        "width": t.get('width'),
                        "height": t.get('height'),
                        "resolution": f"{t.get('width', '')}x{t.get('height', '')}".strip('x')
                    })
            
            return thumbnails
        
    except Exception as ICE:
        return [{"error": f"Failed to get thumbnails: {str(ICE)}"}]
    
tools = [extract_video_id, fetch_transcript, search_youtube, get_full_metadata, get_thumbnails]

llm_with_tools = llm.bind_tools(tools)

tool_mapping = {
    "get_thumbnails" : get_thumbnails,
    "extract_video_id": extract_video_id,
    "fetch_transcript": fetch_transcript,
    "search_youtube": search_youtube,
    "get_full_metadata": get_full_metadata
}

### -- Recursive Chain Flow -- ###
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.messages import HumanMessage, ToolMessage
import json

def execute_tool(tool_call):
    """Execute single tool call and return ToolMessage"""
    try:
        result = tool_mapping[tool_call["name"]].invoke(tool_call["args"])
        content = json.dumps(result) if isinstance(result, (dict, list)) else str(result)
    except Exception as e:
        content = f"Error: {str(e)}"
    
    return ToolMessage(
        content=content,
        tool_call_id=tool_call["id"]
    )

# > Define core processing logic
def process_tool_calls(messages):
    """Recursive tool call processor"""
    last_message = messages[-1]

    # > Execute all tool calls in parallel
    tool_messages = [
        execute_tool(tc)
        for tc in getattr(last_message, 'tool_calls', [])
    ]

    # > Add tool responses to message history
    updated_messages = messages + tool_mapping

    # > Get next LLM response
    next_ai_response = llm_with_tools.invoke(updated_messages)

    return updated_messages + [next_ai_response]