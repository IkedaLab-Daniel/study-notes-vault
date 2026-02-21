from dotenv import load_dotenv
import os
import getpass
from typing import List, Dict
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage, BaseMessage
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph import END, MessageGraph

load_dotenv()

### -- Tavily Setup -- ###
TAVILY_API_KEY = os.getenv("TTAVILY_API_KEY")

tavily_tool = TavilySearchResults(max_result=1)
sample_query = "midnight coding grind snacks ideas"
search_results = tavily_tool.invoke(sample_query)
print(search_results)