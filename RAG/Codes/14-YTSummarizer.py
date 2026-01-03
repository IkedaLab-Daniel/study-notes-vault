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

def process(transcript):
    # > Initialize an empty string to hold the formatted transcript
    txt = ""

    # > Loop through each entry in the transcript
    for i in transcript:
        try:
            # > Append the text and its start time to the output string
            txt += f"Text: {i['text']} Start: {i['start']}\n"
        except KeyError:
            pass
    
    return txt

# ? Sample process() usage
# ? Sample transcript list
# transcript = [
#     {
#         "text": "We're no strangers to love.",
#         "start": 0.0,
#         "duration": 3.5
#     },
#     {
#         "text": "You know the rules and so do I.",
#         "start": 3.5,
#         "duration": 4.0
#     },
#     {
#         "text": "A full commitment's what I'm thinking of.",
#         "start": 7.5,
#         "duration": 4.0
#     }
# ]

# ? Processing the transcript
# formatted_transcript = process(transcript)

# ? Output the processed transcript
# print(formatted_transcript)

# > Chunking transcript
def chunk_transcript(processed_transcript, chunk_size=200, chunk_overlap=20):
    # > Initialize the RecursiveCharacterTextSplitter with specified chunk size and overlap
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    # > Split the transcript into chunks
    chunks = text_splitter.split_text(processed_transcript)
    return chunks

# ? Sample processed transcript string
# processed_transcript = """Text: We're no strangers to love. Start: 0.0
# Text: You know the rules and so do I. Start: 3.5
# Text: A full commitment's what I'm thinking of. Start: 7.5"""

# ? Chunking the transcript
# chunks = chunk_transcript(processed_transcript)

# ? Output the chunks
# print(chunks)

def setup_credentials():
    # > Define model id
    model_id = "meta-llama/llama-3-3-70b-instruct"

    # > Set up the credentials byspecifying the URL for IBM watchson services
    credentials = Credentials(url=URL)

    # > Create an API client using the credentials
    client = APIClient(credentials)
    
    # > Define the project ID associated with the WatsonX platform
    project_id = PROJECT_ID
    
    # > Return the model ID, credentials, client, and project ID (plus API_KEY) for later use
    return model_id, credentials, client, project_id, API_KEY

def initialize_watsonx_llm(model_id, credentials, project_id, parameters):
    # > Create and return an instance of the WatsonLLM with specified configuratiuon
    return WatsonxLLM(
        model_id=model_id,
        url=credentials.get("url"),
        project_id=project_id,
        params=parameters
    )

print(" --- End ---")