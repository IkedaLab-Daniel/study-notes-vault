def warn(*arg, **kwwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

from langchain_groq import ChatGroq
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API=os.getenv('GROQ_API')

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.5,
    api_key=GROQ_API,
    max_tokens=256
)

# ? Test
print(llm.invoke("What is the capital of Ontario?"))
print("\n", llm.invoke("What is the capital of Ontario?").content)