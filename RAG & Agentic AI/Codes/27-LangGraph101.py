from langgraph.graph import StateGraph
from langchain_groq import ChatGroq
from utils import print_agent
from dotenv import load_dotenv
import os

load_dotenv()

### -- LLM Setup -- ###

GROQ_API = os.getenv("GROQ_API")
GROQ_LLM = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=GROQ_API,
    max_tokens=256
)

# ? Test LLM
# print(GROQ_LLM.invoke("Hello! I'm Ice.").content)

### -- States -- ###
from typing import TypedDict, Optional

class AuthState(TypedDict):
    username: Optional[str]
    password: Optional[str]
    is_authenticated: Optional[bool]
    output: Optional[str]

# > Example Objects and Their States
# ? Successful Login
auth_state_1: AuthState = {
    "username": "iceice123",
    "password": "123",
    "is_authenticated": True,
    "output": "Login Successful."
}
print(f"auth_state_1: {auth_state_1}")

# ? Unsuccessful Login
auth_state_2: AuthState = {
    "username": "",
    "password": "wrongpassword",
    "is_authenticated": False,
    "output": "Authentication failed."
}
print(f"auth_state_2: {auth_state_2}")

### -- Nodes -- ###
def input_node(state):
    print(state)
    if state.get('username', "") == "":
        state['username'] = input("Enter username   >> ")
    
    passsword = input("Enter you password   >> ")

    return {"password": passsword}

# input_node(auth_state_1)
# input_node(auth_state_2)

def validate_credentials_node(state):
    # ? Extract username and password from the state
    username = state.get("username", "")
    password = state.get("password", "")

    print(f"Username: {username} | Password: {password}")
    # ? Simulated credential validation
    if username == "test_user" and password == "secure_password":
        is_authenticated = True
    else:
        is_authenticated = False
    
    # ? Return the updated state
    return {"is_authenticated": is_authenticated}

## -- Test Functionality -- ##
# ? Incorrect format
# validate_credentials_node(auth_state_1)

# ? Correct format
auth_state_3: AuthState = {
    "username": "test_user",
    "password": "secure_password",
    "is_authenticated": False,
    "output": "Authentication failed."
}
print(f"auth_state_3: {auth_state_3}")

print(validate_credentials_node(auth_state_3))

## -- Success & Failure Node -- ##
def success_node(state):
    return {"output": "Authentication successful! Welcome."}

print(success_node(auth_state_3))

def failure_node(state):
    return {"output": "NOt successful, please try again!"}

# > Router Node
def router(state):
    if state['is_authenticated']:
        return "success_node"
    else:
        return "failure_node"
    
## --- Creating the Graph --- ##
from langgraph.graph import StateGraph
from langgraph.graph import END
# ? Create an instance of StateGraph
workflow = StateGraph(AuthState)
print(workflow)

# > Adding nodes to the graph
workflow.add_node("InputNode", input_node)
workflow.add_node("ValidateCredential", validate_credentials_node)
workflow.add_node("Success", success_node)
workflow.add_node("Failure", failure_node)

### -- Edges -- ###
workflow.add_edge("InputNode", "ValidateCredential")
workflow.add_edge("Success", END)
workflow.add_edge("Failure", "InputNode")

### -- Building an Authentication Workflow -- ###
workflow.add_conditional_edges("ValidateCredential", router, {"success_node": "Success", "failure_node": "Failure"})

### -- Setting the Entry Point -- ###
workflow.set_entry_point("InputNode")

### -- Compiling the Workflow -- ###
app = workflow.compile()

### -- Running the Application -- ###
# inputs = {"username": "test_user"}
# result = app.invoke(inputs)
# print(result)
# print(result['output'])

### -- Builing a QA Workflot Specific to the Guidede Project -- ###
# > Define the structure if the QA State
class QAState(TypedDict):
    question: Optional[str]
    context: Optional[str]
    answer: Optional[str]

# ? Sample object
qa_state_example = QAState(
    question="What is the purpose of this guided project?",
    context="This project focuses on building a chatbot using Python.",
    answer=None
)

print("\n", "-" * 60)
for key, value in qa_state_example.items():
    print(f"{key}: {value}")

## -- Defining the Input Validation Node -- ##
def input_validation_node(state):
    # ? Extract question from the state
    question = state.get("question", "").strip()

    if not question:
        return {"valid": False, "error": "Question cannot be empty."}
    
    return {"valid": True}

# ? Test
print(input_validation_node(qa_state_example))

## -- Definiing the Context Provider -- ##
def context_provider_node(state):
    question = state.get("question", "").lower()
    if "langgraph" in question or "guided project" in question:
        context = (
            "This guided project is about using LangGraph, a Python library to design state-based workflows. ",
            "LangGraph simplifies building complex applications by connecting modular nodes with conditional edges."
        )
        return {"context": context}

    # ? If unrelated, set context to null
    return {"context": None}

# ? Test
print(context_provider_node(qa_state_example))

## -- Integrating LLM for QA Workflow -- ##
def llm_qa_node(state):
    # ? Extract the question and context from state
    question = state.get("question", "")
    context = state.get("context", None)

    # ? Check context
    if not context:
        return {"answer": "I don't have enough context to answer your question."}

    # ? Construct prompt
    prompt = f"Context: {context}\nQuestion: {question}\nAnswer the question based on the provided context."

    try:
        response = GROQ_LLM.invoke(prompt)
        return {"answer": response.content.strip()}
    except Exception as ICE:
        return {"answer": f"An error occurred: {str(ICE)}"}

# ? Test
print(llm_qa_node(qa_state_example))

## -- Creating the QA Workflow Graph -- ##
qa_workflow = StateGraph(QAState)

# > Add nodes
qa_workflow.add_node("InputNode", input_validation_node)
qa_workflow.add_node("ContextNode", context_provider_node)
qa_workflow.add_node("QANode", llm_qa_node)

# > Entry points
qa_workflow.set_entry_point("InputNode")

# > Edges
qa_workflow.add_edge("InputNode", "ContextNode")
qa_workflow.add_edge("ContextNode", "QANode")
qa_workflow.add_edge("QANode", END)

# > Compile
qa_agent = qa_workflow.compile()

# ? Test
print_agent()
# response = qa_agent.invoke(qa_state_example)
# for key, value in response.items():
#     print(
#     f"""\033[32m
# | {key}: 
# |       - {value}\033[36m
# =====================================================\033[0m"""
#     )


### -- EXERCISE 1 - Define the State Type -- ###
"""
Here, you will define the state schema used by the graph. It should keep track of:

- n: a counter starting from 1.
- letter: a randomly generated lowercase letter at each step.
"""

import random
import string

class CounterState(TypedDict):
    n: Optional[int]
    letter: Optional[str]

### -- EXERCISE 2 - Create add() node function -- ###
"""
This node should represent the increment step such that:

- It adds 1 to the current value of n.
- It randomly selects a lowercase letter and updates the letter field.
"""
def add(state):
    current_value = state.get("n", 1)
    new_n = current_value + 1

    letters = string.ascii_lowercase
    random_letter = random.choice(letters)

    return ({"n": new_n, "letter": random_letter})

# ? Saple State
exercise_state = CounterState(
    n=1,
    letter="a"
)

# ? Test
print("\n\n")
print(add(exercise_state))

### -- EXERCISE 3 - Create print_out() node Function -- ###
"""
This node should print the current state such that:

- It logs the value of n and the current random letter.
- The state is returned.
"""
def print_out(state):
    n = state.get("n", None)
    letter = state.get("letter", None)

    if not n or not letter:
        print("No `n` or No `letter` yet")
        print("return new state with initial value")
        return({ "n": 1, "letter": random.choice(string.ascii_lowercase)})
    
    print(f""" 
    State current values
    >>    n   :   {n}
    >>  letter :  {letter}
""")
    
    return state

### -- EXERCISE 4 - Stop Condition -- ###
"""
Create a function that has a termination condition:

- If the counter reaches 13 or more, the workflow should end.
- Otherwise, it should loop back to add node.
"""
def stop_condition(state):
    return state.get("n", 0) >= 13

### -- EXERCISE 5 - Graph Contruction -- ###
"""
In this exercise, you'll build the LangGraph flow:

- Create a `StateGraph` object using the `ChainState` that you made.
- Add nodes `add` and `print`.
- Add an edge between `add` and `print`
- Add a conditional edge between `print` and `END` based on `stop_condition`.
- Set `add` as entry point of the graph.
"""
counter_workflow = StateGraph(CounterState)

counter_workflow.add_node("add", add)
counter_workflow.add_node("print", print_out)

counter_workflow.add_edge("add", "print")

counter_workflow.add_conditional_edges("print", stop_condition, {
    True: END,
    False: "add"
})

counter_workflow.set_entry_point("add")

### -- EXERCISE 6: Compile and Run -- ###
"""
Compile the graph and start execution with the given initial input:

- The counter should begin at 1.
- Keep letter empty (to be filled in by the add node).
"""
counter_app = counter_workflow.compile()

result = counter_app.invoke({ "n": 1})
print_agent()
print(result)