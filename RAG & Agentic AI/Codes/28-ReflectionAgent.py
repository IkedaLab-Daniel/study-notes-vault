from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import END, MessageGraph, StateGraph

from typing import List, Sequence
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
import os

from utils import print_agent

load_dotenv()

# ANSI color constants
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"


### -- LLM Setup -- ###
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    max_tokens=256,
    api_key=os.getenv("GROQ_API")
)

# ? Test
print(llm.invoke("Hello! I'm Ice!").content)

### -- Generation Prompt for Posts -- ###
generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a professional LinkedIn content assistant tasked with crafting engaging, insightful, and well-structured LinkedIn posts."
            " Generate the best LinkedIn post possible for the user's request."
            " If the user provides feedback or critique, respond with a refined version of your previous attempts, improving clarity, tone, or engagement as needed.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# > Creating the Chain for LinkedIn Post Generation
generate_chain = generation_prompt | llm

# > Reflection Prompt for LinkedIn Post Critique
reflection_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a professional LinkedIn content strategist and thought leadership expert. Your task is to critically evaluate the given LinkedIn post and provide a comprehensive critique. Follow these guidelines:

        1. Assess the post’s overall quality, professionalism, and alignment with LinkedIn best practices.
        2. Evaluate the structure, tone, clarity, and readability of the post.
        3. Analyze the post’s potential for engagement (likes, comments, shares) and its effectiveness in building professional credibility.
        4. Consider the post’s relevance to the author’s industry, audience, or current trends.
        5. Examine the use of formatting (e.g., line breaks, bullet points), hashtags, mentions, and media (if any).
        6. Evaluate the effectiveness of any call-to-action or takeaway.

        Provide a detailed critique that includes:
        - A brief explanation of the post’s strengths and weaknesses.
        - Specific areas that could be improved.
        - Actionable suggestions for enhancing clarity, engagement, and professionalism.

        Your critique will be used to improve the post in the next revision step, so ensure your feedback is thoughtful, constructive, and practical.
        """
    ), 
    MessagesPlaceholder(variable_name="messages")
])

# > Creating the Relfect Chain
reflect_chain = reflection_prompt | llm

### -- Defining the Agent State for Reflection Agent -- ###

# ! Manual Satte Defination Example
# from typing import List, Annotated, TypedDict
# from langchain.schema import HumanMessage, AIMessage, SystemMessage

# # Define State with TypedDict
# class AgentState(TypedDict):
#     messages: Annotated[List[HumanMessage | AIMessage | SystemMessage], "add_messages"]

# > LangGraph's MessageGraph
graph = MessageGraph()

### -- Defining the Generation and Reflection Node -- ###
def generation_node(state: Sequence[BaseMessage]) -> List[BaseMessage]:
    generated_post = generate_chain.invoke({"messages": state})
    return [AIMessage(content=generated_post.content)]

def reflection_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    res = reflect_chain.invoke({"messages": messages})
    return [HumanMessage(content=res.content)]

# > Adding the Generation Node to the Graph
graph.add_node("generate", generation_node)

# >  Adding the Reflect Node to the Graph
graph.add_node("reflect", reflection_node)
graph.add_edge("reflect", "generate")

# > Setting the Entry Point in the Graph
graph.set_entry_point("generate")

### -- Adding a Router Node for Decision Making -- ###
# > Predefined Logic:
def should_continue(state: List[BaseMessage]):
    print(state)
    print(len(state))
    print("-" * 60)
    if len(state) > 6:
        return END
    return "reflect"

graph.add_conditional_edges("generate", should_continue)

# > Compiling the Workflow
workflow = graph.compile()

# > Define input
inputs = HumanMessage(content="""Write a linkedin post on getting a software developer job at IBM under 160 characters""")

# > Execute workflow
response = workflow.invoke(inputs)

print_agent()
print("1:")
print(f"{CYAN}{response[1].content}")
print("2:")
print(f"{GREEN}{response[2].content}")
print("Final Output:")
print(f"{YELLOW}{response[-1].content}")