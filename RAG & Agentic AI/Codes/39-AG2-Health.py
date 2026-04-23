import os

from autogen import ConversableAgent, GroupChat, GroupChatManager
from openai import OpenAI


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

