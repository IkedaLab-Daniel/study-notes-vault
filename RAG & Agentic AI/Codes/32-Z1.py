from langgraph.graph import StateGraph, END, START
from langchain_core.prompts import ChatPromptTemplate
from typing import TypedDict
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

from requests_toolbelt import user_agent

load_dotenv()
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    # model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API")
)
### -- Working Pattern: Routing -- ###

class RouterState(TypedDict):
    user_input: str
    task_type: str
    output: str

# > Translator

def translate(state: RouterState):
    """Translate a given text into French"""

    user_input = state["user_input"]

    prompt = f"""
    You are a French translator agent. Translate the following text into French:
    {user_input}
    French Translation:
    """

    result = llm.invoke(prompt)

    return {"output": result.content}


def summarize(state: RouterState):
    """Summarize the given text"""

    user_input = state["user_input"]

    prompt = f"""
    You are a summarizer agent. Summarize the given text:
    {user_input}
    ---
    Output:
"""
    
    result = llm.invoke(prompt)

    return {"output": result.content}

def definer(state: RouterState):
    """Determine user intent"""

    user_input = state["user_input"]

    prompt = f"""
You are a routing classifier.

Classify the user intent into ONE of these EXACT labels:
- summarize
- translate
- invalid

User input:
{user_input}

Rules:
- Output ONLY one word
- Do NOT explain
- Do NOT add punctuation
- Do NOT add quotes
- Your entire response must be exactly one of: summarize, translate, invalid

Answer:
"""
    
    result = llm.invoke(prompt)

    return {"task_type": result.content}

def router(state: RouterState):
    """Determine next step based on current state"""
    task_type = state["task_type"]

    if task_type == "translate":
        return "translate"
    elif task_type == "summarize":
        return "summarize"
    else:
        return "invalid"

def invalid_catch(state: RouterState):
    """Update state's Output into predefine error message"""
    return {"output": "Invalid user input. Please specify the given task (summarize or translate into French?)"}

## -- Workflow -- ##
 
workflow = StateGraph(RouterState)

# > nodes

workflow.add_node("definer", definer)
workflow.add_node("summarize", summarize)
workflow.add_node("translate", translate)
workflow.add_node("invalid", invalid_catch)

# > start, edge, end

workflow.set_entry_point("definer")
workflow.add_conditional_edges(
    "definer",
    router,
    {
        "summarize": "summarize",
        "translate": "translate",
        "invalid": "invalid"
    }
)
workflow.add_edge("summarize", END)
workflow.add_edge("translate", END)
workflow.add_edge("invalid", END)

app = workflow.compile()

print("\n\nGRAPH:")
print(app.get_graph().draw_mermaid())

user_input = input("Enter query: ")

dummy_state: RouterState = {
    "user_input": user_input,
    "output": "",
    "task_type": ""
}

result = app.invoke(dummy_state)
print("\n\n\n\n RESULT:")
print(result["output"])