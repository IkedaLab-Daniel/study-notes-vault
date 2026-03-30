from langgraph.graph import StateGraph, END, START
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

result = generate_resume_summary(dummy_state)
dummy_state.update(result)
print(dummy_state)