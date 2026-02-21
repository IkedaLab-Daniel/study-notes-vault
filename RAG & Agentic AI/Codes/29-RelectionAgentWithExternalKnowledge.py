from dotenv import load_dotenv
import os
import json
import getpass
from typing import List, Dict
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage, BaseMessage
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph import END, MessageGraph

load_dotenv()

### -- Tavily Setup -- ###
TAVILY_API_KEY = os.getenv("TTAVILY_API_KEY")

tavily_tool = TavilySearchResults(max_result=1)
sample_query = "midnight coding grind snacks ideas"
# search_results = tavily_tool.invoke(sample_query)
# print(search_results)

### -- LLM and Prompting -- ###
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API")
)
question = "Any ideas for midnight coding grind snacks?"
response = llm.invoke(question).content
print(response)

# > Crafting the Agent's Persona and Logic
prompt_template = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are Dr. Paul Saladino, "Carnivore MD," advocating for animal-based nutrition and challenging plant-centric dietary dogma. Focus on the superior bioavailability of animal foods and the potential toxicity of plant compounds such as oxalates, lectins, and phytates.

        Your response must follow these steps:
        1. {first_instruction}
        2. Present the evolutionary and biochemical rationale for animal-based nutrition, emphasizing nutrient density, bioavailability, and the absence of plant antinutrients.
        3. Challenge conventional "plants are healthy" narratives with mechanistic evidence about plant defense compounds and their impact on human physiology.
        4. Reflect and critique your answer. Be rigorous about evolutionary consistency and nutrient science.
        5. After the reflection, **list 1-3 search queries separately** for researching antinutrients, bioavailability studies, or evolutionary nutrition. Do not include them inside the reflection.

        Focus on: organ meats as superfoods, the carnivore elimination protocol, and why "fiber is unnecessary" based on human evolutionary biology.
        """
    ),
    MessagesPlaceholder(variable_name="messages"),
    (
        "system",
        "Answer the user's question above using the required format."
    )
])

# > Defining the responder
first_responder_prompt = prompt_template.partial(first_instruction="Provide a detailed ~250 word answer")
temp_chain = first_responder_prompt | llm
response = temp_chain.invoke({"messages": [HumanMessage(content=question)]})
print(response.content)

# > Structuring the Agent's Output: Data Models
class Reflection(BaseModel):
    missing: str = Field(default="", description="What information is missing")
    superfluous: str = Field(default="", description="What information is unnecessary")

class AnswerQuestion(BaseModel):
    answer: str = Field(description="Main response to the question")
    reflection: Reflection = Field(default_factory=Reflection, description="Self-critique of the answer")
    search_queries: List[str] = Field(default_factory=list, description="Queries for additional research")

### -- Binding tools to the Responder -- ###
initial_chain = first_responder_prompt | llm.bind_tools(tools=[AnswerQuestion])
response = initial_chain.invoke({"messages": [HumanMessage(question)]})
print("----------- Full Structured Output ------------")
print(response.tool_calls)

answer_content = response.tool_calls[0]['args']['answer']
print("---Initial Answer---")
print(answer_content)

Reflection_content = response.tool_calls[0]['args']['reflection']
print("---Reflection Answer---")
print(Reflection_content)

search_queries = response.tool_calls[0]['args']['search_queries']
print("---Search Queries---")
print(search_queries)

### -- Tool Execution -- ###
response_list = []
response_list.append(HumanMessage(content=question))
response_list.append(response)

tool_call = response.tool_calls[0]
search_queries = tool_call["args"].get("search_queries", [])
print(search_queries)

tavily_tool=TavilySearchResults(max_results=3)

def execute_tools(state: List[BaseMessage]) -> List[BaseMessage]:
    last_ai_message = state[-1]
    tool_messages = []
    for tool_call in last_ai_message.tool_calls:
        if tool_call["name"] in ["AnswerQuestion", "ReviseAnswer"]:
            call_id = tool_call["id"]
            search_queries = tool_call["args"].get("search_queries", [])
            query_results = {}
            for query in search_queries:
                result = tavily_tool.invoke(query)
                query_results[query] = result
            tool_messages.append(ToolMessage(
                content=json.dumps(query_results),
                tool_call_id=call_id)
            )
    return tool_messages

tool_response = execute_tools(response_list)
# Use .extend() to add all tool messages from the list
response_list.extend(tool_response)

print("\n\n------")
print(tool_response)
print(response_list)