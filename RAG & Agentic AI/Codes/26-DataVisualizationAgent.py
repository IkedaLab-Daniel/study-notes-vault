def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')


import pandas as pd
import matplotlib.pyplot as plt
from langchain_groq import ChatGroq
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API = os.getenv("GROQ_API")

### -- LLM Setup -- ###
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)