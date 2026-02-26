import warnings
warnings.filterwarnings('ignore')

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool
from dotenv import load_dotenv
import os
import json

load_dotenv() 
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

def tavily_test():
    response = search_tool.invoke("What's the weather like in Tokyo today?")
    print("--- Tavily Search Results ---")

    # Handle different response shapes returned by the Tavily tool.
    if isinstance(response, dict):
        query = response.get('query')
        if query:
            print(f"Query: {query}\n")

        results = response.get('results', [])
        if isinstance(results, list) and results:
            for result in results:
                title = result.get('title', 'No title') if isinstance(result, dict) else str(result)
                url = result.get('url', '#') if isinstance(result, dict) else '#'
                content = result.get('content', '') if isinstance(result, dict) else ''
                print(f"* **Title:** [{title}]({url})")
                print(f"  **Content:** {content}")
                print("-" * 20)
        else:
            print('No results found in response.')

    elif isinstance(response, list):
        print('Response is a list of results:')
        for item in response:
            if isinstance(item, dict):
                title = item.get('title', item.get('name', 'No title'))
                url = item.get('url', '#')
                content = item.get('content', '')
                print(f"* **Title:** [{title}]({url})")
                print(f"  **Content:** {content}")
            else:
                print('-', item)

    else:
        print('Unexpected response type:', type(response))
        print(response)

tavily_test()