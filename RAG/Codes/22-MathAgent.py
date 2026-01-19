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

## -- Open AI Alternative: Groq (FREE!) -- ##
# Get free API key at: https://console.groq.com/keys
from langchain_openai import ChatOpenAI

groq_llm = ChatOpenAI(
     model="llama-3.3-70b-versatile",  # or "mixtral-8x7b-32768", "llama-3.1-8b-instant"
     api_key=os.getenv('GROQ_API'),  # Get from https://console.groq.com
     base_url="https://api.groq.com/openai/v1"
 )

# response = groq_llm.invoke("Hi there! I'm Ice!")
# print("\nGroq Response: ", response.content)

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

## -- Functions -- ##

def add_numbers(inputs:str) -> dict:
    """
    Adds a list of numbers provided in the input dictionary or extracts numbers from a string.

    Parameters:
    - inputs (str): 
    string, it should contain numbers that can be extracted and summed.

    Returns:
    - dict: A dictionary with a single key "result" containing the sum of the numbers.

    Example Input (Dictionary):
    {"numbers": [10, 20, 30]}

    Example Input (String):
    "Add the numbers 10, 20, and 30."

    Example Output:
    {"result": 60}
    """
    numbers = [int(x) for x in inputs.replace(",", "").split() if x.isdigit()]
    result = sum(numbers)
    return {"result": result}

## -- Tool -- ##
# from langchain.agents import Tool
# add_tool = Tool(
#     name="AddTool",
#     func=add_numbers,
#     description="Adds a list of numbers and returns the results."
# )

## @tool operator ##
from langchain_core.tools import tool
import re

@tool
def add_numbers(inputs:str) -> dict:
    """
    Adds a list of numbers provided in the input string.
    Parameters:
    - inputs (str): 
    string, it should contain numbers that can be extracted and summed.
    Returns:
    - dict: A dictionary with a single key "result" containing the sum of the numbers.
    Example Input:
    "Add the numbers 10, 20, and 30."
    Example Output:
    {"result": 60}
    """
    # Use regular expressions to extract all numbers from the input
    numbers = [int(num) for num in re.findall(r'\d+', inputs)]
    # numbers = [int(x) for x in inputs.replace(",", "").split() if x.isdigit()]
    
    result = sum(numbers)
    return {"result": result}