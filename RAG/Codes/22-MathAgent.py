"""
RAG.Codes.22-MathAgent
Dependencies
pip install langchain==0.3.23 \n
    langchain-ibm==0.3.10 \n         # > Using WatsonX 
    langchain-community==0.3.16 \n
    wikipedia==1.4.0 \n
    openai==1.77.0 \n
    langchain-openai==0.3.16
"""

from langchain_community.chat_models import ChatOllama
#from langchain_ibm import ChatWatsonx
from langchain.agents import AgentType
from dotenv import load_dotenv
import os
import re

load_dotenv()

llm = ChatOllama(
    model="llama3.2:3b"
)

response = llm.invoke("Hi there! I'm Ice!")
print("\nResponse: ", response.content)

## -- Open AI Alternative: Groq (FREE!) -- ##
# Get free API key at: https://console.groq.com/keys
from langchain_openai import ChatOpenAI

groq_llm = ChatOpenAI(
     model="llama-3.3-70b-versatile",  # or "mixtral-8x7b-32768", "llama-3.1-8b-instant"
     api_key=os.getenv('GROQ_API'),  # Get from https://console.groq.com
     base_url="https://api.groq.com/openai/v1"
 )

response = groq_llm.invoke("Hi there! I'm Ice!")
print("\nGroq Response: ", response.content)

## -- Or just use your existing Ollama (simplest!) -- ##
# response = llm.invoke("What's 5 + 3?")
# print("\nOllama Response: ", response.content)

## -- Open AI (Paid) -- ##
# from langchain_openai import ChatOpenAI

# openai_llm = ChatOpenAI(
#     model="gpt-4.1-nano",
#     api_key="I DONT HAVE OPENAI TOKENSSSS!! ૮(˶ㅠ︿ㅠ)ა"
# )

# response = openai_llm.invoke("Hi there! I'm Ice!")
# print("\nResponse: ", response.content)