from dotenv import load_dotenv
import os

from autogen import ConversableAgent, GroupChat, GroupChatManager
from openai import OpenAI
from utils import print_agent

load_dotenv()

# Groq exposes an OpenAI-compatible API.
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
	raise ValueError("Missing GROQ_API_KEY. Set it in your environment.")

groq_base_url = "https://api.groq.com/openai/v1"
groq_model = "llama-3.1-8b-instant"

# OpenAI-compatible client configured for Groq.
client = OpenAI(api_key=groq_api_key, base_url=groq_base_url)

# AG2/AutoGen LLM config for ConversableAgent and GroupChatManager.
llm_config = {
	"config_list": [
		{
			"model": groq_model,
			"api_key": groq_api_key,
			"base_url": groq_base_url,
			"api_type": "openai",
		}
	]
}

# Disable Docker execution to prevent runtime errors
code_execution_config = {"use_docker": False}

## -- Agents -- ##
patient_agent = ConversableAgent(
    name="patient", 
    system_message="You describe symptoms and ask for medical help.", 
    llm_config=llm_config
)

diagnosis_agent = ConversableAgent(
    name="diagnosis", 
    system_message="You analyze symptoms and provide a possible diagnosis. Summarize key points in one response.", 
    llm_config=llm_config
)

pharmacy_agent = ConversableAgent(
    name="pharmacy", 
    system_message="You recommend medications based on diagnosis. Only respond once.", 
    llm_config=llm_config
)

consultation_agent = ConversableAgent(
    name="consultation", 
    system_message="You determine if a doctor's visit is required. Provide a final summary with clear next steps. IMPORTANT: End your response with 'CONSULTATION_COMPLETE' to signal the end of the conversation.", 
    llm_config=llm_config
)

## -- Group Chat -- ##
groupchat = GroupChat(
	agents=[diagnosis_agent, pharmacy_agent, consultation_agent],
	messages=[],
	max_round=5,
	speaker_selection_method="round_robin"
)

manager = GroupChatManager(
	name="manager",
	groupchat=groupchat
)

## -- Start Consulatation -- ##
print_agent()
print("""
   |----------------------------------------------------|
   |  Welcome to the AI Healthcare Consultation System! |
   |----------------------------------------------------|
	  """)
symptoms = input("""
	🩺 >> Please describe your symptoms: """)
    
response = patient_agent.initiate_chat(
	manager,
	message=f"I am feeling {symptoms}. Can you help?",
)