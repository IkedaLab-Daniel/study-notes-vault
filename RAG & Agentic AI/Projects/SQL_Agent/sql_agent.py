def warn(*arg, **kwwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

from langchain_groq import ChatGroq
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
import argparse

from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API=os.getenv('GROQ_API')

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=GROQ_API,
    max_tokens=1024
)

### -- Argument Parser -- ###
parser = argparse.ArgumentParser()
parser.add_argument("--prompt", type=str, help="The prompt to send to the SQL Agent")
args = parser.parse_args()

mysql_username = 'root'  # Replace with your server connect information
mysql_password = 'ikedalab123' # ! This is just placeholder, not my password :P
mysql_host = '127.0.0.1' # Replace with your server connect information
mysql_port = '3306' # Replace with your server connect information
database_name = 'Chinook'
mysql_uri = f'mysql+mysqlconnector://{mysql_username}:{mysql_password}@{mysql_host}:{mysql_port}/{database_name}'
db = SQLDatabase.from_uri(mysql_uri)

agent_executor = create_sql_agent(llm=llm, db=db, verbose=True, handle_parsing_errors=True)

### -- Use the prompt from CLI -- ###
if args.prompt:
    agent_executor.invoke(args.prompt)
else:
    print("Please provide a prompt using --prompt argument")