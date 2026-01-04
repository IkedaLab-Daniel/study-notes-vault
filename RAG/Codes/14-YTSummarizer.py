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

def setup_embedding_model(credentials, project_id):
    # > Create and return an instance of WatsonXEmbeddings
    return WatsonxEmbeddings(
        model_id='ibm/slate-30m-english-rtrvr-v2',
        url=credentials["url"],
        project_id=project_id
    )

def create_faiss_index(chunks, embedding_model):
    """
    Create a FAISS index from text chunks using the specified embedding model.
    
    :param chunks: List of text chunks
    :param embedding_model: The embedding model to use
    :return: FAISS index
    """
    # > Use the FAISS library to create an index from the provided text chunks
    return FAISS.from_texts(chunks, embedding_model)

def perform_similarity_search(faiss_index, query, k=3):
    """
    Search for specific queries within the embedded transcript using the FAISS index.
    
    :param faiss_index: The FAISS index containing embedded text chunks
    :param query: The text input for the similarity search
    :param k: The number of similar results to return (default is 3)
    :return: List of similar results
    """
    # > Perform the similarity search using the FAISS index
    results = faiss_index.similarity_search(query, k=k)
    return results

# > Summarizing the transcript
def create_summary_prompt():
    """
    Create a PromptTemplate for summarizing a YouTube video transcript.
    
    :return: PromptTemplate object
    """
    # > Define the template for the summary prompt
    template = """
    <|begin_of_text|><|start_header_id|>system<|end_header_id|>
    You are an AI assistant tasked with summarizing YouTube video transcripts. Provide concise, informative summaries that capture the main points of the video content.

    Instructions:
    1. Summarize the transcript in a single concise paragraph.
    2. Ignore any timestamps in your summary.
    3. Focus on the spoken content (Text) of the video.

    Note: In the transcript, "Text" refers to the spoken words in the video, and "start" indicates the timestamp when that part begins in the video.<|eot_id|><|start_header_id|>user<|end_header_id|>
    Please summarize the following YouTube video transcript:

    {transcript}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
    """
    
    # > Create the PromptTemplate object with the defined template
    prompt = PromptTemplate(
        input_variables=["transcript"],
        template=template
    )
    
    return prompt

def create_summary_chain(llm, prompt, verbose=True):
    """
    Create an LLMChain for generating summaries.
    
    :param llm: Language model instance
    :param prompt: PromptTemplate instance
    :param verbose: Boolean to enable verbose output (default: True)
    :return: LLMChain instance
    """
    return LLMChain(llm=llm, prompt=prompt, verbose=verbose)

# > Retrieving relevant context and generating answers
def retrieve(query, faiss_index, k=7):
    """
    Retrieve relevant context from the FAISS index based on the user's query.

    Parameters:
        query (str): The user's query string.
        faiss_index (FAISS): The FAISS index containing the embedded documents.
        k (int, optional): The number of most relevant documents to retrieve (default is 3).

    Returns:
        list: A list of the k most relevant documents (or document chunks).
    """
    relevant_context = faiss_index.similarity_search(query, k=k)
    return relevant_context

# > Creating the Q&A prompt template
def create_qa_prompt_template():
    """
    Create a PromptTemplate for question answering based on video content.
    Returns:
        PromptTemplate: A PromptTemplate object configured for Q&A tasks.
    """
    
    # > Define the template string
    qa_template = """
    You are an expert assistant providing detailed answers based on the following video content.
    Relevant Video Context: {context}
    Based on the above context, please answer the following question:
    Question: {question}
    """

    # > Create thje PromptTemplate Object
    prompt_template = PromptTemplate(
        input_variables=["centext", "questions"],
        template=qa_template
    )

    return prompt_template

print(" --- End ---")