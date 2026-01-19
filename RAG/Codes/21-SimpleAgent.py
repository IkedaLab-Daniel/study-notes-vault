from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_community.utilities import WikipediaAPIWrapper
import re
from utils import print_agent

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
def divide_numbers(dividend: str, divisor: str) -> str:
    """ 
    Divide two numbers. Only use this with actual numeric values, not results from other operations.
    
    Args:
        dividend: The actual number to be divided (must be a number, not a reference)
        divisor: The actual number to divide by (must be a number, not a reference)
    
    Returns:
        The result of the division or an error message
    """
    try:
        # Extract only digits, decimal points, and negative signs
        div1_match = re.search(r'-?\d+\.?\d*', dividend.strip())
        div2_match = re.search(r'-?\d+\.?\d*', divisor.strip())
        
        if not div1_match or not div2_match:
            return f"Error: Invalid input. Got dividend='{dividend}' and divisor='{divisor}'. Please provide actual numbers."
        
        div1 = float(div1_match.group())
        div2 = float(div2_match.group())
        
        if div2 == 0:
            return "Error: Cannot divide by zero"
        
        return str(div1 / div2)
    except Exception as e:
        return f"Error: Could not perform division. Please provide valid numbers. Got: dividend='{dividend}', divisor='{divisor}'" 

@tool
def search_wikipedia(query: str) -> str:
    """
    Search Wikipedia for information about a topic.
    
    Args:
        query: The topic or question to search for on Wikipedia
    
    Returns:
        A summary of the Wikipedia article
    """
    wikipedia = WikipediaAPIWrapper()
    return wikipedia.run(query)

tools = [add_numbers, multiply_numbers, divide_numbers, search_wikipedia, search_wikipedia]

math_agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt="You are a helpful assistant that can perform math operations (addition, multiplication, division) and search Wikipedia for information. You can also search on Wikipedia searching information."
)

print("""\033[34m 
    |-------------------------------|
    |          Math Agent           |
    |-------------------------------|
""")
query = input("\033[37m   >> Enter query: ")

print("\033[33m⏳ Processing your request...\033[0m")

# Stream the agent's response to show intermediate steps
for chunk in math_agent.stream(
    {"messages": [("human", query)]},
    stream_mode="values"
):
    # Check if any tools are being called
    if "messages" in chunk and len(chunk["messages"]) > 0:
        last_msg = chunk["messages"][-1]
        if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
            for tool_call in last_msg.tool_calls:
                if "wikipedia" in tool_call["name"].lower():
                    print_agent()
                    print("""\033[33m
|-------------------------------------------------------------|
          Wait, I'll search on the web, hold on...
|-------------------------------------------------------------|
                    \033[0m""")

                else:
                    print(f"\033[33m🧮 Using {tool_call['name']}...\033[0m")

response = chunk

final_answer = response["messages"][-1].content

print(f"""\033[34m 
    |------------------------ Query ------------------------|
        >> {query}           
    |-------------------------------------------------------|
""")
print_agent()
print(f"""\033[92m
|-------------------------------------------------------------|
>> {final_answer}
|-------------------------------------------------------------|
       """)