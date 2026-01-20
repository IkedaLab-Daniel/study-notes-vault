"""
RAG.Codes.22-MathAgent
Dependencies
pip install langchain==0.3.23 \n
    langchain-ibm==0.3.10 \n         # > Using WatsonX 
    langchain-community==0.3.16 \n
    wikipedia==1.4.0 \n
    openai==1.77.0 \n
    langchain-openai==0.3.16 \n
    langgraph==0.6.1
"""

from langchain_community.chat_models import ChatOllama
#from langchain_ibm import ChatWatsonx
from langchain.agents import AgentType
from dotenv import load_dotenv
import os
import re
from utils import print_agent

load_dotenv()

llm = ChatOllama(
    model="llama3.2:3b"
)

## -- Open AI Alternative: Groq (FREE!) -- ##
# Get free API key at: https://console.groq.com/keys
from langchain_openai import ChatOpenAI

groq_llm = ChatOpenAI(
     model="llama-3.3-70b-versatile",  # or "mixtral-8x7b-32768", "llama-3.1-8b-instant"
     api_key=os.getenv('GROQ_API'),  # Get from https://console.groq.com
     base_url="https://api.groq.com/openai/v1"
 )

# response = groq_llm.invoke("Hi there! I'm Ice!")
# print("\nGroq Response: ", response.content)

## -- Or just use your existing Ollama (simplest!) -- ##
# response = llm.invoke("What's 5 + 3?")
# print("\nOllama Response: ", response.content)

## -- Open AI (Paid) -- ##
# from langchain_openai import ChatOpenAI

# openai_llm = ChatOpenAI(
#     model="gpt-4.1-nano",
#     api_key="I DONT HAVE OPENAI TOKENSSSS!! ૮(˶ㅠ︿ㅠ)ა"
# )

# response = openai_llm.invoke("Hi there! I'm Ice!")
# print("\nResponse: ", response.content)

## -- Functions -- ##

def add_numbers(inputs:str) -> dict:
    """
    Adds a list of numbers provided in the input dictionary or extracts numbers from a string.

    Parameters:
    - inputs (str): 
    string, it should contain numbers that can be extracted and summed.

    Returns:
    - dict: A dictionary with a single key "result" containing the sum of the numbers.

    Example Input (Dictionary):
    {"numbers": [10, 20, 30]}

    Example Input (String):
    "Add the numbers 10, 20, and 30."

    Example Output:
    {"result": 60}
    """
    numbers = [int(x) for x in inputs.replace(",", "").split() if x.isdigit()]
    result = sum(numbers)
    return {"result": result}

## -- Tool -- ##
from langchain.agents import Tool
add_tool = Tool(
    name="AddTool",
    func=add_numbers,
    description="Adds a list of numbers and returns the results."
)

## @tool operator ##
from langchain_core.tools import tool
import re

@tool
def add_numbers(inputs:str) -> dict:
    """
    Adds a list of numbers provided in the input string.
    Parameters:
    - inputs (str): 
    string, it should contain numbers that can be extracted and summed.
    Returns:
    - dict: A dictionary with a single key "result" containing the sum of the numbers.
    Example Input:
    "Add the numbers 10, 20, and 30."
    Example Output:
    {"result": 60}
    """
    # Use regular expressions to extract all numbers from the input
    numbers = [int(num) for num in re.findall(r'\d+', inputs)]
    # numbers = [int(x) for x in inputs.replace(",", "").split() if x.isdigit()]
    
    result = sum(numbers)
    return {"result": result}

# print("Name: \n", add_numbers.name)
# print("Description: \n", add_numbers.description) 
# print("Args: \n", add_numbers.args) 

# test_input = "what is the sum between 10, 20 and 30 " 
# print(add_numbers.invoke(test_input))

# --- Comparing Approaches --- #
# print("Tool Constructor Approach:")
# print(f"Has Schema: {hasattr(add_tool, 'args_schema')}")
# print("\n")

# print("@tool Decorator approach:")
# print(f"Has Schema: {hasattr(add_numbers, 'args_schema')}")
# print(f"Args schema information: {add_numbers.args}")

# --- add_number with option --- #
from typing import List

@tool
def add_numbers_with_options(numbers: List[float], absolute: bool = False) -> float:
    """
    Adds a list of numberes provided as input
    
    Parameters:
    - numbers (Lost[float]): A list of numbers to be summed.
    - absolute (bool): If true, use the absolute values of the numbers before summing.

    Returns:
    - float: The total sum of the numbers.
    """
    if absolute:
        numbers = [abs(n) for n in numbers]
    return sum(numbers)

# print(f"Args Schema Info: {add_numbers_with_options.args}")
# print(f"Args Schema Info: {add_numbers.args}")
# print("\n-------------------------------\n")
# print(add_numbers_with_options.invoke({"numbers":[-1.1,-2.1,-3.0],"absolute":False}))
# print(add_numbers_with_options.invoke({"numbers":[-1.1,-2.1,-3.0],"absolute":True}))

# --- Improved tool return types with Python typing --- #
from typing import Dict, Union

@tool
def sum_numbers_with_complex_output(inputs: str) -> Dict[str, Union[float, str]]:
    """
    Extracts and sums all integers and decimal numbers from the input string.

    Parameters:
    - inputs (str): A string that may contain numeric values.

    Returns:
    - dict: A dictionary with the key "result". If numbers are found, the value is their sum (float). 
            If no numbers are found or an error occurs, the value is a corresponding message (str).

    Example Input:
    "Add 10, 20.5, and -3."

    Example Output:
    {"result": 27.5}
    """
    matches = re.findall(r'-?\d+(?:\.\d+)?', inputs)

    if not matches:
        return {"result": "No numbers found in input"}
    
    try:
        numbers = [float(num) for num in matches]
        total = sum(numbers)
        return {"result": total}
    except Exception as Ice:
        return {"result": f"Error during summation: {str(Ice)}"}

result = sum_numbers_with_complex_output.invoke("kalsjdnajklsnbdklnb")
print(result)
result = sum_numbers_with_complex_output.invoke("10, 20, 30")
print(result)

# -- straight forward version -- #
@tool
def sum_numbers_from_text(inputs: str) -> float:
    """
    Adds a list of numbers provided in the input string.
    
    Args:
        text: A string containing numbers that should be extracted and summed.
        
    Returns:
        The sum of all numbers found in the input.
    """
    # Use regular expressions to extract all numbers from the input
    numbers = [int(num) for num in re.findall(r'\d+', inputs)]
    result = sum(numbers)
    return result

# --- initialize_agent --- #
from langchain.agents import initialize_agent

agent = initialize_agent(
    [add_tool],
    llm=groq_llm,
    agent="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True
)

# response = agent.run("In 2023, the US GDP was approximately $27.72 trillion, while Canada's was around $2.14 trillion and Mexico's was about $1.79 trillion what is the total.")

# print("\n\n",response)

# agent.invoke({"input": "Add 10, 20, two and 30"})

## --- Structured chat zero react-description ---#
agent_2 = initialize_agent(
    [sum_numbers_from_text],
    llm=groq_llm,
    agent="structured-chat-zero-shot-react-description",
    verbose=True,
    handling_parsing_errors=True
)

# response = agent_2.invoke({"input": "Add 10, 20, two, and 30"})
# print("\n\n", response)

agent_3 = initialize_agent(
    [sum_numbers_with_complex_output],
    llm=groq_llm, 
    agent="openai-functions",
    verbose=True,
    handle_parsing_errors=True
)

# response = agent_3.invoke({"input": "Add 10, 20 and 30"})
# print(response)

agent_4 = initialize_agent(
    [add_numbers_with_options],
    llm=groq_llm,
    agent="structured-chat-zero-shot-react-description",
    verbose=True
)

# response = agent_4.invoke({
#      "input": "Add -10, -20, and -30 using absolute values."
# })

# print_agent()
# print("   >> ", response)

## --- create_react_agent --- ##
from langgraph.prebuilt import create_react_agent

agent_exec = create_react_agent(
    model=groq_llm,
    tools=[sum_numbers_from_text]
)

# msgs = agent_exec.invoke(
#     {
#         "messages": [
#             ("human", "Add the numbers -10, thirty-two, -20, -30")
#         ]
#     }
# )

# print_agent()
# print(msgs["messages"][-1].content)

@tool
def subtract_numbers(inputs: str) -> dict:
    """
    Extracts numbers from a string, negates the first number, and successively subtracts 
    the remaining numbers in the list.

    This function is designed to handle input in string format, where numbers are separated 
    by spaces, commas, or other delimiters. It parses the string, extracts valid numeric values, 
    and performs a step-by-step subtraction operation starting with the first number negated.

    Parameters:
    - inputs (str): 
      A string containing numbers to subtract. The string may include spaces, commas, or 
      other delimiters between the numbers.

    Returns:
    - dict: 
      A dictionary containing the key "result" with the calculated difference as its value. 
      If no valid numbers are found in the input string, the result defaults to 0.

    Example Input:
    "100, 20, 10"

    Example Output:
    {"result": -130}

    Notes:
    - Non-numeric characters in the input are ignored.
    - If the input string contains only one valid number, the result will be that number negated.
    - Handles a variety of delimiters (e.g., spaces, commas) but does not validate input formats 
      beyond extracting numeric values.
    """
    # Extract numbers from the string
    numbers = [int(num) for num in inputs.replace(",", "").split() if num.isdigit()]

    # If no numbers are found, return 0
    if not numbers:
        return {"result": 0}

    # Start with the first number negated
    result = -1 * numbers[0]

    # Subtract all subsequent numbers
    for num in numbers[1:]:
        result -= num

    return {"result": result}

# print("Name: \n", subtract_numbers.name)
# print("Description: \n", subtract_numbers.description) 
# print("Args: \n", subtract_numbers.args) 

# print("Calling Tool Function:")
# test_input = "10 20 30 and four a b" 
# print_agent()
# print(subtract_numbers.invoke(test_input))  # Example

@tool
def multiply_numbers(inputs: str) -> dict:
    """
    Extracts numbers from a string and calculates their product.

    Parameters:
    - inputs (str): A string containing numbers separated by spaces, commas, or other delimiters.

    Returns:
    - dict: A dictionary with the key "result" containing the product of the numbers.

    Example Input:
    "2, 3, 4"

    Example Output:
    {"result": 24}

    Notes:
    - If no numbers are found, the result defaults to 1 (neutral element for multiplication).
    """
    # Extract numbers from the string
    numbers = [int(num) for num in inputs.replace(",", "").split() if num.isdigit()]
    print(numbers)

    # If no numbers are found, return 1
    if not numbers:
        return {"result": 1}

    # Calculate the product of the numbers
    result = 1
    for num in numbers:
        result *= num
        print(num)

    return {"result": result}