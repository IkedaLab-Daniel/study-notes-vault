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

# ! NOTE: This wont work on terminal. I'm executing the code on Jupyter Notebook.

response = agent.invoke("How many rows of data are in this file?")
print(response['output'])

### -- Checking -- ###
code_done = response['intermediate_steps'][-1][0].tool_input.replace('; ', '\n')
print(code_done)

# ? Test
response = agent.invoke("Give me all the data where student's age is over 18 years old.")
code_done = response['intermediate_steps'][-1][0].tool_input.replace('; ', '\n')
print(code_done)

### -- Plot data with natural language -- ###
# ? Task 1
response = agent.invoke("Generate a bar chart to plot the gender count.")
print(response['intermediate_steps'][-1][0].tool_input.replace('; ', '\n'))

# ? Task 2
response = agent.invoke("Generate a pie chart to display average value of Walc for each Gender.")
print(response['intermediate_steps'][-1][0].tool_input.replace('; ', '\n'))

# ? Task 3
response = agent.invoke("Create box plots to analyze the relationship between 'freetime' (amount of free time) and 'G3' (final grade) across different levels of free time.")
print(response['intermediate_steps'][-1][0].tool_input.replace('; ', '\n'))

# ? Task 4
response = agent.invoke("Generate scatter plots to examine the correlation between 'Dalc' (daily alcohol consumption) and 'G3', and between 'Walc' (weekend alcohol consumption) and 'G3'.")
print(response['intermediate_steps'][-1][0].tool_input.replace('; ', '\n'))