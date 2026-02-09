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

groq_llm = langchain_openai.ChatOpenAI(
     model="llama-3.1-8b-instant",  # Fast, reliable, good for function calling
     api_key=os.getenv('GROQ_API'),  # Get from https://console.groq.com
     base_url="https://api.groq.com/openai/v1"
 )