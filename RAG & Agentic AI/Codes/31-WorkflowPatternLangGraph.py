from langgraph.graph import StateGraph, END, START
from langgraph.types import Send

from typing import TypedDict, Annotated, List, Literal
from pydantic import BaseModel, Field
import operator
from pprint import pprint

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os

## --- Init LLM -- ##

load_dotenv()
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    # model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API")
)

print(llm.invoke('Hello'))