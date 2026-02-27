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

# tavily_test()

### -- Clothing Recommendation Tool -- ###
@tool
def recommend_clothing(weather: str) -> str:
    """
    Returns a clothing recommendation based on the provided weather description.

    This function examines the input string for specific keywords or temperature indicators 
    (e.g., "snow", "freezing", "rain", "85°F") to suggest appropriate attire. It handles 
    common weather conditions like snow, rain, heat, and cold by providing simple and practical 
    clothing advice.

    :param weather: A brief description of the weather (e.g., "Overcast, 64.9°F")
    :return: A string with clothing recommendations suitable for the weather
    """

    weather = weather.lower()

    if "snow" in weather or "freezing" in weather:
        return "Wear a heavy coat, gloves, and boots."
    elif "rain" in weather or "wet" in weather:
        return "Bring a raincoat and waterproof shoes."
    elif "hot" in weather or "85" in weather:
        return "T-shirt, shorts, and sunscreen recommended."
    elif "cold" in weather or "50" in weather:
        return "Wear a warm jacket or sweater."
    else:
        return "A light jacket should be fine."
    
tools = [search_tool, recommend_clothing]

tools_by_name = {
    tool.name: tool
    for tool in tools
}

### -- Setting up the Language Model -- ###
from langchain_groq import ChatGroq

model = ChatGroq(
    api_key=os.getenv("GROQ_API"),
    model="llama-3.1-8b-instant"
)

### -- System Prompt -- ###
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage, SystemMessage

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a helpful AI assistant that thinks step-by-step and uses tools when needed.

When responding to queries:
1. First, think about what information you need
2. Use available tools if you need current data or specific capabilities  
3. Provide clear, helpful responses based on your reasoning and any tool results

Always explain your thinking process to help users understand your approach.
"""),
    MessagesPlaceholder(variable_name="scratch_pad")
])

### -- Binding Tools to the Model -- ###
model_react=chat_prompt|model.bind_tools(tools)

### -- Agent State -- ###
from typing import (Annotated, Sequence, TypedDict)
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    """The state of the agent"""
    messages: Annotated[Sequence[BaseMessage], add_messages]

### -- Demo State Management -- ###
state: AgentState = {"messages": []}

# state["messages"] = add_messages(state["messages"], [HumanMessage(content="hellor")])
# print("After greeting:", state["messages"])

### -- Manual ReAct Execution (Understanding the Flow) -- ###
# > Step 1: Initial Query Processing
dummy_state: AgentState = {
    "messages": [HumanMessage( "What's the weather like in Zurich, and what should I wear based on the temperature?")]
}

response = model_react.invoke({"scratch_pad": dummy_state["messages"]})

dummy_state["messages"] = add_messages(dummy_state["messages"], [response])

print("---" * 20)
print(dummy_state["messages"][-1].content)
print("Tool Call: ", response.tool_calls[-1])
print("---" * 20)

# > Step 2: Tool Execution
tool_call = response.tool_calls[-1]
print("Tool call:", tool_call)

tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
print("Tool result preview: ", tool_result[0]['title'])

tool_message = ToolMessage(
    content=json.dumps(tool_result),
    name=tool_call["name"],
    tool_call_id=tool_call["id"]
)

dummy_state["messages"] = add_messages(dummy_state["messages"], [tool_message])

print("---" * 20)
print(dummy_state["messages"])