import os
from dotenv import load_dotenv
from autogen import ConversableAgent
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
            "model": "llama-3.1-8b-instant",
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
#     message="Can you explain what a neural network is?",
#     recipient=tutor,
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
print("--------" * 10)


## -- Built-in Agent Types -- ##
from autogen import AssistantAgent, UserProxyAgent
from autogen.coding import LocalCommandLineCodeExecutor


# > Create Assistant Agent
assistant = AssistantAgent(
    name="assistant",
    system_message="You are a helpful assistant who writes and explains Python code clearly.",
    llm_config=llm_config,
)

# > User Proxy Agent
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=5,
    code_execution_config={
        "executor": LocalCommandLineCodeExecutor(work_dir="coding", timeout=30),
    }
)

# > Start
# chat_result = user_proxy.initiate_chat(
#     recipient=assistant,
#     message="execute an nmap scan at 127.0.0.1. Local nmap already installed. Save result as scan.txt",
#     max_turns=4,
#     summary_method="reflection_with_llm"
# )

# Step 6: Print summary
# print("\nFinal Summary:")
# print(chat_result.summary)

## -- Human-in-the-loop -- ##
from autogen import ConversableAgent
import random

# > Define system message
triage_system_message = """
You are a bug triage assistant. You will be given bug report summaries.

For each bug:
- If it is urgent (e.g., 'crash', 'security', or 'data loss' is mentioned), escalate it and ask the human agent for confirmation.
- If it seems minor (e.g., cosmetic, typo), suggest closing it but still ask for human review.
- Otherwise, classify it as medium priority and ask the human for review.

Once all bugs are processed, summarize what was escalated, closed, or marked as medium priority.
End by saying: "You can type exit to finish."
"""

# > Create triage agent
triage_bot =ConversableAgent(
    name="triage_agent",
    system_message=triage_system_message,
    llm_config=llm_config,
)

# > Create human agent
human = ConversableAgent(
    name="human",
    human_input_mode="ALWAYS",
)

# > Generate sample bugs
BUGS = [
    "App crashes when opening user profile.",
    "Minor UI misalignment on settings page.",
    "Password reset email not sent consistently.",
    "Typo in the About Us footer text.",
    "Database connection timeout under heavy load.",
    "Login form allows SQL injection attack.",
]

random.shuffle(BUGS)
selected_bugs = BUGS[:3]

initial_prompt = (
    "Please triage the following bug reports one by one:\n\n" +
    "\n".join([f"{i+1}. {bug}" for i, bug in enumerate(selected_bugs, 1)])
)

# > Start converstaion
result = human.initiate_chat(
    recipient=triage_bot,
    message=initial_prompt
)