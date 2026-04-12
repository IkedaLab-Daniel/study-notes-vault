import asyncio
import logging
from beeai_framework.backend import UserMessage, SystemMessage
from beeai_framework.adapters.groq import GroqChatModel

## -- Simple Chat -- ##

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
# async def main() -> None:
#     logging.getLogger('asyncio').setLevel(logging.CRITICAL) # Suppress unwanted warnings
#     response = await basic_chat_example()
# if __name__ == "__main__":
#     asyncio.run(main())


## -- Prompt Templates -- ##

import asyncio
import logging
import string
from beeai_framework.adapters.groq import GroqChatModel
from beeai_framework.backend import UserMessage

class SimplePromptTemplate:
    """SSimple prompt template using Python string formatting."""

    def __init__(self, template: str):
        self.template = template

    def render(self, variables: dict) -> str:
        """Remder the template with provided variables."""
        # Replace mustache-style {{variable}} with Python format {variable}
        formatted_template = self.template
        for key, value in variables.items():
            formatted_template = formatted_template.replace(f"{{{{{key}}}}}", f"{{{key}}}")

        return formatted_template.format(**variables)
    