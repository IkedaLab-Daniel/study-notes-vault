import re
from pytube import YouTube
from langchain_core.tools import tool
import yt_dlp
from typing import List, Dict
from langchain_core.messages import HumanMessage, ToolMessage
import json
from utils import print_agent
import pprint

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

tools.append(search_youtube)
# ? Test
# search_out = search_youtube.run("Generative AI")
# print_agent()
# print(search_out)

### -- Metadata Extraction Tool -- ###
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
tools.append(get_full_metadata)
# meta_data=get_full_metadata.run("https://www.youtube.com/watch?v=T-D1OfcDW1M")
# print_agent()
# pprint.pprint(meta_data, indent=4)

###  -- Defining thumbnail retrieval tool -- ###
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
    

# result = thumbnails=get_thumbnails.run("https://www.youtube.com/watch?v=qWHaMrR5WHQ")
# print_agent()
# pprint.pprint(result, indent=4)
tools.append(get_thumbnails)

### -- Binding tools -- ###
llm_with_tools = llm.bind_tools(tools)

for tool in tools:
    schema = {
        "name": tool.name,
        "description": tool.description,
        "parameters": tool.args_schema.schema() if tool.args_schema else {},
        "return": tool.return_type if hasattr(tool, "return_type") else None
    }
    # pprint.pprint(schema)

### -- LLM calls tool -- ###
query = "I want to summarize youtube video: https://www.youtube.com/watch?v=T-D1OfcDW1M in english"
print(f"    >> Query: {query}")

messages = [HumanMessage(content=query)]
print(f"Messages: \n{messages}")

### -- LangChain tool binding process -- ###
response_1 = llm_with_tools.invoke(messages)
pprint.pprint(response_1)

messages.append(response_1)