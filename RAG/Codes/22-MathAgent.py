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
import re

llm = ChatOllama(
    model="llama3.2:3b"
)

response = llm.invoke("Hi there! I'm Ice!")
print("\nResponse: ", response.content)

## -- Open AI -- ##
from langchain_openai import ChatOpenAI

openai_llm = ChatOpenAI(
    model="gpt-4.1-nano",
    api_key="I DONT HAVE OPENAI TOKENSSSS!! ૮(˶ㅠ︿ㅠ)ა"
)

response = openai_llm.invoke("Hi there! I'm Ice!")
print("\nResponse: ", response.content)