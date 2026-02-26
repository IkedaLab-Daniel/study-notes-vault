import warnings
warnings.filterwarnings('ignore')

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool
from dotenv import load_dotenv
import os
import json

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# > Initialioze the Tavily search tool
search = TavilySearchResults()

@tool
def search_tool(query: str):
    """
    Search the web for infromation using Tavily API.

    :param query: The search query string
    :return: Search results related to the query
    """
    return search.invoke(query)