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

### -- Exercise 3 -- ###
"""
Create an agent to automate the entire process you previously completed.
"""
class TipCalculatorAgent:
    def __init__(self):
        self.llm_with_tool = llm.bind_tools([calculate_tip])
        self.tool_map = {
            "calculate_tip": calculate_tip
        }

    def run(self, query: str):
        chat_history = [HumanMessage(content=query)]

        response = self.llm_with_tool.invoke(chat_history)
        if not response.tool_calls:
            return response.content
        
        tool_call = response.tool_calls[0]
        tool_name = tool_call["name"]
        too_args = tool_call["args"]
        tool_call_id = tool_call["id"]

        tool_result = self.tool_map[tool_name].invoke(too_args)

        tool_message = ToolMessage(content=str(tool_result), tool_call_id=tool_call_id)
        chat_history.extend([response, tool_message])

        final_response = self.llm_with_tool.invoke(chat_history)
        return final_response.content
    
my_agent = TipCalculatorAgent()

print_agent()
print(my_agent.run("How much should I tip on $60 at 20%?"))