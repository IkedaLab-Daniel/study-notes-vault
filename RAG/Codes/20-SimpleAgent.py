from langchain_ibm import ChatWatsonx
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatWatsonx(
    model_id="ibm/granite-3-8b-instruct",
    url=os.getenv('URL'),
    project_id=os.getenv('PROJECT_ID'),
    apikey=os.getenv('API_KEY')
)

query = input("Enter query: ")

response = llm.invoke(query)

print("Agent: ", response.content)