from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from dotenv import load_dotenv
from utils import print_agent
import os

load_dotenv()

### -- LLM Setup -- ###
from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI
llm = init_chat_model(
    "llama-3.1-8b-instant", 
    model_provider="groq",
    api_key=os.getenv('GROQ_API')
)

### -- Defining an add functiuon -- ###
@tool
def add(a: int, b: int) -> int:
    """
    Add a and b
    
    :param a: first integer to be added
    :type a: int
    :param b: second integer to be added
    :type b: int
    :return: sum of a and b
    :rtype: int
    """
    return a + b

tools = [add]

llm_with_tools = llm.bind_tools(tools)

### -- More tools --- ###
@tool
def subtract(a: int, b: int) -> int:
    """
    Subtract b from a
    
    :type a: int
    :type b: int
    :rtype: int
    """
    return a - b

@tool
def multiply(a: int, b: int) -> int:
    """
    Multiply a and b

    :type a: in
    :type b: int
    :rtype: int
    """
    return a * b

### -- Testing the functions -- ###
# tool_map = {
#     "add": add,
#     "subtract": subtract,
#     "multiply": multiply
# }

# input_ = {
#     "a": 1,
#     "b": 2
# }

# result = tool_map["add"].invoke(input_)
# print_agent()
# print(result)

result = add.invoke({ "a": 123123, "b": 190238921})
print_agent()
print(result)