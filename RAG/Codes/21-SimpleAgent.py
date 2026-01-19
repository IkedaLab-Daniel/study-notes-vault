from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:3b")

def add_number(numbers: str) -> int:
    """ 
    Add a list of numbers together. Provide numbers separated by commas or spaces.
    
    Args:
        numbers: A string containing numbers to add, e.g., "-10, -20, -30" or "5 10 15"
    
    Returns:
        The sum of all the numbers
    """
    import re
    # Extract all numbers including negative ones
    nums = re.findall(r'-?\d+\.?\d*', numbers)
    result = sum(float(n) for n in nums)
    return int(result) if result.is_integer() else result

add_agent = create_react_agent(
    model=llm,
    tools=[add_number],
    prompt="You are a helpful math assistanct that can perform some operations such as addition"
)

response = add_agent.invoke(
    {"messages": [("human", "Add the numbers 817239127, 19234412")]}
)

final_answer = response["messages"][-1].content

print(final_answer)