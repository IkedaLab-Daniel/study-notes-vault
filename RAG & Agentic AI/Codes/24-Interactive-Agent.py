from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from dotenv import load_dotenv
import os

load_dotenv()

### -- LLM Setup -- ###
from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI
llm = init_chat_model("gpt-4o-mini", model_provider="openai")

groq_llm = ChatOpenAI(
     model="llama-3.1-8b-instant",  # Fast, reliable, good for function calling
     api_key=os.getenv('GROQ_API'),  # Get from https://console.groq.com
     base_url="https://api.groq.com/openai/v1"
 )