from multiprocessing import dummy

from langgraph.graph import StateGraph, END, START
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

def print_workflow_info(workflow, app=None):
    """Prints comprehensive information about a LangGraph workflow."""
    print("WORKFLOW INFORMATION")
    print("====================")
    print(f"Nodes: {workflow.nodes}")
    print(f"Edges: {workflow.edges}")

    
    # Use getter method for finish points if available
    try:
        finish_points = workflow.finish_points
        print(f"Finish points: {finish_points}")
    except:
        try:
            # Alternative approaches
            print(f"Finish point: {workflow._finish_point}")
        except:
            print("Finish points attribute not directly accessible")

## -- State -- ##
class ChainState(TypedDict):
    job_description: str
    resume_summary: str
    cover_letter: str

## -- Resume Summary Agent -- ##
def generate_resume_summary(state: ChainState) -> ChainState:
    prompt = f"""
You're a resume assistant. Read the following job description and summarize the key qualifications and experience the ideal candidate should have, phrased as if from the perspective of a strong applicant's resume summary.

Job Description:
{state['job_description']}
"""

    response = llm.invoke(prompt)

    return {**state, "resume_summary": response.content}

dummy_state: ChainState = {
    "job_description": "We are looking for a coffee lover to test our brand's newly formulated 3-in-1 coffee flavors",
    "resume_summary": "",
    "cover_letter": "",
}

## -- Generate Cover Letter Agent -- ##
def generate_cover_letter(state: ChainState) -> ChainState:
    prompt = f"""
You're a cover letter writing assistant. Using the resume summary below, write a professional and personalized cover letter for the following job.

Resume Summary:
{state['resume_summary']}

Job Description:
{state['job_description']}
"""

    response = llm.invoke(prompt)

    return {**state, "cover_letter": response.content}

## -- LangGraph Workflow -- ##

workflow = StateGraph(ChainState)

# > nodes
workflow.add_node("generate_resume_summary", generate_resume_summary)
workflow.add_node("generate_cover_letter", generate_cover_letter)

# > Start, edge, end

workflow.set_entry_point("generate_resume_summary")
workflow.add_edge("generate_resume_summary", "generate_cover_letter")
workflow.set_finish_point("generate_cover_letter")

# print_workflow_info(workflow)

app = workflow.compile()

input_state = {
        "job_description": "We are looking for a data scientist with experience in machine learning, NLP, and Python. Prior work with large datasets and experience deploying models into production is required."
}

# result = app.invoke(input_state)

# print("====" * 30)
# print(result['resume_summary'])

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

def router_node(state: RouterState):
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

dummy_state: RouterState = {
    "user_input": "Skibidi Sigma",
    "task_type": "",
    "output": ""
}

result = router_node(dummy_state)
dummy_state.update(result)
print(dummy_state["task_type"])