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
print(GROQ_LLM.invoke("Hello! I'm Ice.").content)

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