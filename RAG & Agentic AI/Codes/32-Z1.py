from langgraph.graph import StateGraph, END, START
from langchain_core.prompts import ChatPromptTemplate
from typing import TypedDict
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    # model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API")
)

class RouterState(TypedDict):
    user_input: str
    task_type: str
    output: str

class Router(BaseModel):
    role: str = Field(..., description="Decide whether the user wants to summarize a passage  ouput 'summarize'  or translate text into French oupput translate.")

llm_router=llm.bind_tools([Router])
llm_router_structured = llm.with_structured_output(Router)


def _normalize_task_type(value: str) -> str:
    value = value.strip().lower()
    if value == "summarize":
        return "summarize"
    if value == "translate":
        return "translate"
    if "summar" in value:
        return "summarize"
    if "french" in value or "translat" in value:
        return "translate"
    return "summarize"

def router_node(state: RouterState) -> RouterState:
    routing_prompt = f"""
    You are an AI task classifier.
    
    Decide whether the user wants to:
    - "summarize" a passage
    - or "translate" text into French
    
    Respond with just one word: 'summarize' or 'translate'.
    
    User Input: "{state['user_input']}"
    """

    # Prefer structured output; if parsing fails, fall back to text/tool-call parsing.
    try:
        structured = llm_router_structured.invoke(routing_prompt)
        task_type = _normalize_task_type(structured.role)
    except Exception:
        response = llm_router.invoke(routing_prompt)
        if response.tool_calls:
            task_type = _normalize_task_type(response.tool_calls[0]["args"].get("role", ""))
        else:
            task_type = _normalize_task_type(getattr(response, "content", ""))

    return {**state, "task_type": task_type} # This becomes the next node's name!

def router(state: RouterState) -> str:
    return state['task_type']

def summarize_node(state: RouterState) -> RouterState:
    prompt = f"Please summarize the following passage:\n\n{state['user_input']}"
    response = llm.invoke(prompt)
    
    return {**state, "task_type": "summarize", "output": response.content}

def translate_node(state: RouterState) -> RouterState:
    prompt = f"Translate the following text to French:\n\n{state['user_input']}"
    response = llm.invoke(prompt)

    return {**state, "task_type": "translate", "output": response.content}

workflow = StateGraph(RouterState)

# > Nodes
workflow.add_node("router", router_node)
workflow.add_node("summarize", summarize_node)
workflow.add_node("translate", translate_node)

# > entry, edge, end
workflow.set_entry_point("router")
workflow.add_conditional_edges("router", router, {
    "summarize": "summarize",
    "translate": "translate"
})
workflow.set_finish_point("summarize")
workflow.set_finish_point("translate")

app = workflow.compile()

input_text = {
        "user_input": "Can you translate this sentence: I love programming?",
    }

result = app.invoke(input_text)

print(result['output'])
print(result['task_type'])