from langgraph.graph import StateGraph, END
from langchain_core.prompts import ChatPromptTemplate
from typing import TypedDict
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
    prompt = ChatPromptTemplate.from_template(
"""You're a resume assistant. Read the following job description and summarize the key qualifications and experience the ideal candidate should have, phrased as if from the perspective of a strong applicant's resume summary.

Job Description:
{job_description}
"""
    )

    chain = prompt | llm
    response = chain.invoke({"job_description": state["job_description"]})

    return {**state, "resume_summary": response.content}

dummy_state: ChainState = {
    "job_description": "We are looking for a coffee lover to test our brand's newly formulated 3-in-1 coffee flavors",
    "resume_summary": "",
    "cover_letter": "",
}

## -- Generate Cover Letter Agent -- ##
def generate_cover_letter(state: ChainState) -> ChainState:
    prompt = ChatPromptTemplate.from_template(
"""You're a cover letter writing assistant. Using the resume summary below, write a professional and personalized cover letter for the following job.

Resume Summary:
{resume_summary}

Job Description:
{job_description}
"""
    )

    chain = prompt | llm
    response = chain.invoke(
        {
            "resume_summary": state["resume_summary"],
            "job_description": state["job_description"],
        }
    )

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

    prompt = ChatPromptTemplate.from_template(
"""You are a French translator agent. Translate the following text into French:
{user_input}
French Translation:
"""
    )

    chain = prompt | llm
    result = chain.invoke({"user_input": user_input})

    return {"output": result.content}


def summarize(state: RouterState):
    """Summarize the given text"""

    user_input = state["user_input"]

    prompt = ChatPromptTemplate.from_template(
"""You are a summarizer agent. Summarize the given text:
{user_input}
---
Output:
"""
    )

    chain = prompt | llm
    result = chain.invoke({"user_input": user_input})

    return {"output": result.content}

def definer(state: RouterState):
    """Determine user intent"""

    user_input = state["user_input"]

    prompt = ChatPromptTemplate.from_template(
"""You are a routing classifier.

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
    )

    chain = prompt | llm
    result = chain.invoke({"user_input": user_input})

    return {"task_type": result.content.strip().lower()}

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