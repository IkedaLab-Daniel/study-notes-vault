"""
RAG.Codes.22-MathAgent
Dependencies
pip install langchain==0.3.23 \n
    langchain-ibm==0.3.10 \n         # > Using WatsonX 
    langchain-community==0.3.16 \n
    wikipedia==1.4.0 \n
    openai==1.77.0 \n
    langchain-openai==0.3.16 \n
    langchain_ollama==1.0.1       # > Using Local LLM with Ollama
"""

from langchain_ollama import ChatOllama
#from langchain_ibm import ChatWatsonx
from langchain.agents import AgentType
import re
