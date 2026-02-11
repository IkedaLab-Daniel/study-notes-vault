import numpy as np
import pandas as pd
import matplotlib
import seaborn
import sklearn
import langchain
import langchain_openai

import glob
import os
from typing import List, Optional
from dotenv import load_dotenv

from langchain_core.tools import tool

load_dotenv()

@tool
def list_csv_files() -> Optional[List[str]]:
    """List all CSV file names in the local directory.

    Returns:
        A list containing CSV file names.
        If no CSV files are found, returns None.
    """
    csv_files = glob.glob(os.path.join(os.getcwd(), "*.csv"))
    if not csv_files:
        return None
    return [os.path.basename(file) for file in csv_files]

print("Tool Name:", list_csv_files.name)
print("Tool Description:", list_csv_files.description)
print("Tool Arguments:", list_csv_files.args)

### -- LLM Setup -- ###
groq_llm = langchain_openai.ChatOpenAI(
     model="llama-3.1-8b-instant",  # Fast, reliable, good for function calling
     api_key=os.getenv('GROQ_API'),  # Get from https://console.groq.com
     base_url="https://api.groq.com/openai/v1"
 )

### -- Dataset caching tool -- ###
DATAFRAME_CACHE = {}

@tool 
def preload_datasets(paths: List[str]) -> str:
    """
    Loads CSV files into a global cache if not already loaded.
    
    This function helps to efficiently manage datasets by loading them once
    and storing them in memory for future use. Without caching, you would
    waste tokens describing dataset contents repeatedly in agent responses.
    
    Args:
        paths: A list of file paths to CSV files.

    Returns:
        A message summarizing which datasets were loaded or already cached.
    """
    loaded = []
    cached = []

    for path in paths:
        if path not in DATAFRAME_CACHE:
            DATAFRAME_CACHE[path] = pd.read_csv(path)
            loaded.append(path)
        else:
            cached.append(path)
    
    return (
        f"Loaded datasets: {loaded}\n"
        f"Already cached: {cached}" 
    )