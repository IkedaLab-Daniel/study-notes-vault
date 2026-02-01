from langgraph.graph import StateGraph
from langchain_groq import ChatGroq
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

input_node(auth_state_1)
input_node(auth_state_2)

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
validate_credentials_node(auth_state_1)

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
inputs = {"username": "test_user"}
result = app.invoke(inputs)
print(result)
print(result['output'])