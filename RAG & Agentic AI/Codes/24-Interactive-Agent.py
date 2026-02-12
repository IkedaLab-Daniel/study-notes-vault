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
tool_map = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply
}

input_ = {
    "a": 1,
    "b": 2
}

# result = tool_map["add"].invoke(input_)
# print_agent()
# print(result)

# result = add.invoke({ "a": 123123, "b": 190238921})
# print_agent()
# print(result)

### -- Add new tools to LLM -- ###
tools = [add, subtract, multiply]

llm_with_tools = llm.bind_tools(tools)

### -- Interacting with the Model -- ###
# ? Craft the user query
query = "What is 3 + 2?"
chat_history = [HumanMessage(content=query)]

# ? Invoke the model
response_1 = llm_with_tools.invoke(chat_history)
chat_history.append(response_1)

print_agent()
print(type(response_1))
print(response_1)

# ? Paese tool calls
tool_calls_1 = response_1.tool_calls

tool_1_name = tool_calls_1[0]["name"]
tool_1_args = tool_calls_1[0]["args"]
tool_call_1_id = tool_calls_1[0]["id"]

print_agent()
print(f'tool name:\n{tool_1_name}')
print(f'tool args:\n{tool_1_args}')
print(f'tool call ID:\n{tool_call_1_id}')

# ? Invoke the Tool
tool_response = tool_map[tool_1_name].invoke(tool_1_args)
tool_message = ToolMessage(content=tool_response, tool_call_id=tool_call_1_id)

print(tool_message)

chat_history.append(tool_message)

# ? Generate a final answer from chat history
answer = llm_with_tools.invoke(chat_history)
print_agent()
print(type(answer))
print(answer.content)

### -- Building an Agent -- ###
class ToolCallingAgent:
    def __init__(self, llm):
        self.llm_wuth_tools = llm.bind_tools(tools)
        self.tool_map = tool_map
    
    def run(self, query: str) -> str:
        # > Step 1: Initial user message
        chat_history = [HumanMessage(content=query)]

        # > Step 2: LLM Chooses tool
        response = self.llm_wuth_tools.invoke(chat_history)
        if not response.tool_calls:
            return response.content

        # > Step 3: Handle first tool call
        tool_call = response.tool_calls[0]
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        tool_call_id = tool_call["id"]

        # > Step 4: Call tool manually
        tool_result = self.tool_map[tool_name].invoke(tool_args)

        # > Step 5: Send result back to LLM
        tool_message = ToolMessage(content=str(tool_result), tool_call_id=tool_call_id)
        chat_history.extend([response, tool_message])

        # > Step 6: Fianl LLM Result
        final_response = self.llm_wuth_tools.invoke(chat_history)
        return final_response.content

my_agent = ToolCallingAgent(llm)

print_agent()
print(my_agent.run("one plus 2"))
print(my_agent.run("one - 2"))
print(my_agent.run("three times two"))