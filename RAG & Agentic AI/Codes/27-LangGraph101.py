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