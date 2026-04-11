import asyncio
import logging
from beeai_framework.backend import UserMessage, SystemMessage
from beeai_framework.adapters.groq import GroqChatModel

# Initialize the chat model
async def basic_chat_example():
    llm = GroqChatModel(
        model_id="llama-3.3-70b-versatile"
    )

    messages = [
        SystemMessage(content="You are a helpful AI assistant and creative writing expert."),
        UserMessage(content="Help me brainstorm a unique business idea for a food delivery service that doesn't exist yet.")
    ]


    response = await llm.run(messages)

    print("User: Help me brainstorm a unique business idea for a food delivery service that doesn't exist yet.")
    print(f"Assistant: {response.get_text_content()}")
    
    return response

# Run the basic chat example
async def main() -> None:
    logging.getLogger('asyncio').setLevel(logging.CRITICAL) # Suppress unwanted warnings
    response = await basic_chat_example()
if __name__ == "__main__":
    asyncio.run(main())
