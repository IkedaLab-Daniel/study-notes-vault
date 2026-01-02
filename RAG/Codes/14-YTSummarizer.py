# Import necessary libraries for the YouTube bot
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

print(" --- End ---")