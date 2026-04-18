import os
from dotenv import load_dotenv
from autogen import ConversableAgent, AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from autogen.llm_config import LLMConfig
import json
import time
import random

load_dotenv()

print("AG2 module imported")

groq_api_key = os.environ.get("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("Missing GROQ_API_KEY. Set it in your environment or .env file.")

## -- Conversable Agent -- ##
llm_config = {
    "config_list": [
        {
            "model": "llama-3.3-70b-versatile",
            "api_key": groq_api_key,
            "base_url": "https://api.groq.com/openai/v1",
            "api_type": "openai",
        }
    ]
}


# > Student Agent
student = ConversableAgent(
    name="student",
    system_message="You are a curious student. You ask clear, specific questions to learn new concepts.",
    human_input_mode="NEVER",
    llm_config=llm_config
)

# > Tutor agent
tutor = ConversableAgent(
    name="tutor",
    system_message="You are a helpful tutor who provides clear and concise explanations suitable for a beginner.",
    human_input_mode="NEVER",
    llm_config=llm_config
)

# > Start conversation
# chat_result = student.initiate_chat(
#     recipient=tutor,
#     message="Can you explain what a neural network is?",
#     max_turns=2,
#     summary_method="reflection_with_llm"
# )

# print("\nFinal Summary:")
# print(chat_result.summary)

## -- Creating Specialized Agents -- ##

# > Technical Expert Agent
tech_expert = ConversableAgent(
    name="tech_expert",
    system_message="""You are a senior software engineer with expertise in Python, AI, and system design.
    Provide technical, detailed explanations with code examples when appropriate.
    Always consider best practices and performance implications.""",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

# > Creative Writer Agent
creative_writer = ConversableAgent(
    name="creative_writer",
    system_message="""You are a creative writer and storyteller.
    Your responses are engaging, imaginative, and use vivid descriptions.
    You excel at making complex topics accessible through stories and analogies.""",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

# > Business Analyst Agent
business_analyst = ConversableAgent(
    name="business_analyst",
    system_message="""You are a business analyst focused on ROI, efficiency, and strategic planning.
    Always consider business impact, costs, and practical implementation.
    Provide actionable recommendations with clear metrics.""",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

agents = [tech_expert, creative_writer, business_analyst]
print("Specialized agents created!")

for agent in agents:
    print(f"- {agent.name}: {agent.system_message.split('.')[0]}.")