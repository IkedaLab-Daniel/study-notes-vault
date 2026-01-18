from langchain_ibm import ChatWatsonx
from langchain.agents import Tool
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatWatsonx(
    model_id="ibm/granite-3-8b-instruct",
    url=os.getenv('URL'),
    project_id=os.getenv('PROJECT_ID'),
    apikey=os.getenv('API_KEY')
)

# query = input("Enter query: ")

# response = llm.invoke(query)

# print("Agent: ", response.content)

def add_number(inputs: str) -> dict:
    """ 
    Tool: add_number
    Description: Adds a list of numbers provided in the input dictionary or extracts numbers from a string
    Inputs: str (e.g., "Add 2, 3, and 5" or '{"numbers": [2, 3, 5]}')
    Outputs: dict (e.g., {"result": 10})
    """
    numbers = [int(x) for x in inputs.replace(',', ' ').split() if x.isdigit()]
    result = sum(numbers)
    return {"result": result}

add_tool = Tool(
    name="add_number",
    func=add_number,
    description="Adds a list of numbers provided in the input string or extracts numbers from a string and returns their sum."
)

print("Tool object", add_tool)
