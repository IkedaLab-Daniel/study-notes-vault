from utils import print_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from dotenv import load_dotenv
import os

load_dotenv()

### -- LLM Setup -- ###
from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI
llm = init_chat_model(
    "llama-3.1-8b-instant", 
    model_provider="groq",
    api_key=os.getenv("GROQ_API")
)

@tool
def calculate_tip(total_bill: int, tip_percent: int) -> int:
    """
    Calculate total tip given total bill and tip percentaage.
    total_bill * (tip_percent / 100)
    
    :param total_bill: Total bill
    :type total_bill: int
    :param tip_percent: Tip percentage
    :type tip_percent: int
    :return: Description
    :rtype: the result value of calculation total_bill * (tip_percent / 100)
    """
    return total_bill * (tip_percent / 100)

tool_map = {
    "calculate_tip": calculate_tip
}

### -- Exercise 2 -- ###
"""
Simulate a user query like "How much should I tip on $60 at 20%?".
Bind the tool to the predefined llm and prompt the LLM with the query above. Then parse the LLM response for the tool calling details and invoke the tool accordingly. Finally, take the entire chat history and prompt the LLM for a final output.
"""
print("\n---\n")
exercise_llm_with_tool = llm.bind_tools([calculate_tip])

query = "How much should I tip on $60 at 20%?"
chat_history = [HumanMessage(content=query)]

response_1 = exercise_llm_with_tool.invoke(chat_history)

print_agent()
print(type(response_1))
print(response_1)

# ? Paese tool calls
tool_calls_1 = response_1.tool_calls

tool_1_name = tool_calls_1[0]["name"]
tool_1_args = tool_calls_1[0]["args"]
tool_call_1_id = tool_calls_1[0]["id"]

print(f""" 
    tool_1_name      - {tool_1_name}
    tool_1_args      - {tool_1_args}
    tool_call_1_id   - {tool_call_1_id} 
""")

tool_response = tool_map[tool_1_name].invoke(tool_1_args)
tool_message = ToolMessage(content=tool_response, tool_call_id=tool_call_1_id)

chat_history.extend([response_1, tool_message])

result = exercise_llm_with_tool.invoke(chat_history)
print_agent()
print(result.content)