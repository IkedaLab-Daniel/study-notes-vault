from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
import re

llm = ChatOllama(model="llama3.2:3b")

@tool
def add_numbers(numbers: str) -> int:
    """ 
    Add a list of numbers together. Provide numbers separated by commas or spaces.
    
    Args:
        numbers: A string containing numbers to add, e.g., "-10, -20, -30" or "5 10 15"
    
    Returns:
        The sum of all the numbers
    """
    nums = [int(num) for num in re.findall(r'-?\d+', numbers)]
    return sum(nums)

@tool
def multiply_numbers(numbers: str) -> int:
    """ 
    Multiply a list of numbers together. Provide numbers separated by commas or spaces.
    
    Args:
        numbers: A string containing numbers to multiply, e.g., "5, 10, 2" or "3 4 5"
    
    Returns:
        The product of all the numbers
    """
    nums = [int(num) for num in re.findall(r'-?\d+', numbers)]
    result = 1
    for num in nums:
        result *= num
    return result

@tool
def divide_numbers(dividend: str, divisor: str) -> float:
    """ 
    Divide two numbers.
    
    Args:
        dividend: The number to be divided
        divisor: The number to divide by
    
    Returns:
        The result of the division
    """
    div1 = float(dividend.strip())
    div2 = float(divisor.strip())
    if div2 == 0:
        return "Error: Cannot divide by zero"
    return div1 / div2 

math_agent = create_react_agent(
    model=llm,
    tools=[add_numbers, multiply_numbers, divide_numbers],
    prompt="You are a helpful math assistant that can perform operations such as addition, multiplication, and division"
)

query = input("Enter query: ")

response = math_agent.invoke(
    {"messages": [("human", query)]}
)

final_answer = response["messages"][-1].content

print(final_answer)