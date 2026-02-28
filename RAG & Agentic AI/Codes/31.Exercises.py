from langchain.tools import tool


### -- Exercise 1 -- ###
""""
Instructions:

1. Create a tool called calculator_tool using the @tool decorator.
2. The tool should accept a mathematical expression as a string.
3. Use Python's eval() function carefully (or better yet, use the ast module for safety).
4. Test your tool with various mathematical expressions.
5. Add your tool to the tools list and test it with the ReAct agent.
"""
import math
import ast
import operator

@tool
def calculator_tool(expression: str) -> str:
    """
    Safely evaluate mathematical expressions.
    
    :param expression: A mathematical expression as a string (e.g., "2 + 3 * 4")
    :return: The result of the calculation
    """
    result = eval(expression)
    return result

print(calculator_tool.invoke("1 + 1"))

tool_list = [calculator_tool]
# "What's 15% of 250 plus the square root of 144?