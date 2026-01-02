import gradio as gr
import re # > For extracting video id 
from youtube_transcript_api import YouTubeTranscriptApi  # > For extracting transcripts from YouTube videos
from langchain.text_splitter import RecursiveCharacterTextSplitter  # > For splitting text into manageable segments
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes  # > For specifying model types
from ibm_watsonx_ai import APIClient, Credentials  # > For API client and credentials management
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams  # > For managing model parameters
from ibm_watsonx_ai.foundation_models.utils.enums import DecodingMethods  # > For defining decoding methods
from langchain_ibm import WatsonxLLM, WatsonxEmbeddings  # > For interacting with IBM's LLM and embeddings
from ibm_watsonx_ai.foundation_models.utils import get_embedding_model_specs  # > For retrieving model specifications
from ibm_watsonx_ai.foundation_models.utils.enums import EmbeddingTypes  # > For specifying types of embeddings
from langchain_community.vectorstores import FAISS  # > For efficient vector storage and similarity search
from langchain.chains import LLMChain  # > For creating chains of operations with LLMs
from langchain.prompts import PromptTemplate  # > For defining prompt templates
from dotenv import load_dotenv
import os
load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")

def get_video_id(url):
    # > Regex pattern to match YT video URLs
    pattern = r'https:\/\/www\.youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else None

# ? sample get_video_id usage
# url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# video_id = get_video_id(url)
# print(video_id)

def get_transcript(url):
    # > Extracts the video ID from the URL
    video_id = get_video_id(url)
    
    # > Create a YouTubeTranscriptApi() object
    ytt_api = YouTubeTranscriptApi()
    
    # > Fetch the list of available transcripts for the given YouTube video
    transcripts = ytt_api.list(video_id)
    
    transcript = ""
    for t in transcripts:
        # > Check if the transcript's language is English
        if t.language_code == 'en':
            if t.is_generated:
                # > If no transcript has been set yet, use the auto-generated one
                if len(transcript) == 0:
                    transcript = t.fetch()
            else:
                # > If a manually created transcript is found, use it (overrides auto-generated)
                transcript = t.fetch()
                break  # > Prioritize the manually created transcript, exit the loop
    
    return transcript if transcript else None

# ? Sample YouTube URL
# url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# ? Fetching the transcript
#transcript = get_transcript(url)

# ? Output the fetched transcript
# print(transcript)

print(" --- End ---")