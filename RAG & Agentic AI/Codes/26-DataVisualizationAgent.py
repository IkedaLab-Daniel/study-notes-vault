def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')


import pandas as pd
import matplotlib.pyplot as plt
from langchain_groq import ChatGroq
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from utils import print_agent
from dotenv import load_dotenv
import os
import sys

load_dotenv()
GROQ_API = os.getenv("GROQ_API")

### -- Load Dataset -- ###
try:
    df = pd.read_csv(
        "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/ZNoKMJ9rssJn-QbJ49kOzA/student-mat.csv"
    )
    print("Dataset Loaded:")
    print(df.head(5))
    print(df.info())
except Exception as ICE:
    print("Dataset import error: ", ICE)
    sys.exit(1)

### -- Agent Setup -- ###
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=GROQ_API,
    max_tokens=256
)

agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=False,
    return_intermediate_steps=True,
    handle_parsing_errors=True,
    allow_dangerous_code=True
)

# ? Test
# query = "Hello! I'm Ice."
# response = llm.invoke(query)
# print("     >>", query)
# print_agent()
# print("     >>",response.content)

response = agent.invoke("How many rows of data are in this file?")
print(response['output'])