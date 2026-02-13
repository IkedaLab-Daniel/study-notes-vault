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

print(llm.invoke("Hello! I'm Ice.").content)