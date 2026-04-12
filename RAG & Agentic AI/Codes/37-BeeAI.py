import asyncio
import logging
from beeai_framework.backend import UserMessage, SystemMessage
from beeai_framework.adapters.groq import GroqChatModel
from openai import project

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
    
# > Business evaluation template
async def prompt_template_example():
    llm = GroqChatModel(
        model_id="llama-3.3-70b-versatile"
    )

    # Create a prompt template for data science project evaluation
    template_content = """
    You are a senior data scientist evaluating a machine learning project proposal.
    
    Project Details:
    - Project Name: {{project_name}}
    - Business Problem: {{business_problem}}
    - Available Data: {{data_description}}
    - Timeline: {{timeline}}
    - Success Metrics: {{success_metrics}}
    
    Please provide:
    1. Feasibility assessment (1-10 scale)
    2. Key technical challenges
    3. Recommended approach
    4. Risk mitigation strategies
    5. Expected outcomes
    
    Be specific and actionable in your recommendations.
    """

    # Create the prompt template
    prompt_template = SimplePromptTemplate(template_content)

    project_scenario = [
        {
            "project_name": "Smart Inventory Optimization",
            "business_problem": "Reduce inventory costs while maintaining 95% product availability",
            "data_description": "2 years of sales data, supplier lead times, seasonal patterns, 500K records",
            "timeline": "3 months development, 1 month testing",
            "success_metrics": "15% cost reduction, maintain 95% availability, <2% forecast error"
        },
        {
            "project_name": "Fraud Detection System",
            "business_problem": "Detect fraudulent transactions in real-time with minimal false positives",
            "data_description": "1M transaction records, user behavior data, device fingerprints",
            "timeline": "6 months development, 2 months validation",
            "success_metrics": "95% fraud detection rate, <1% false positive rate, <100ms response time"
        }
    ]

    for i, scenario in enumerate(project_scenario, 1):
        print(f"\n=== Project Evaluation {i}: {scenario['project_name']} ===")

        # Render the template with scenario data
        rendered_prompt = prompt_template.render(scenario)
        print("\n   Rendered promot:")
        print(rendered_prompt)

        #  Generate evaluation using create(method)

        messages = [UserMessage(content=rendered_prompt)]
        response = await llm.run(messages)

        print("### LLM Response: ###\n")
        print(response.get_text_content())

async def main() -> None:
    logging.getLogger('asyncio').setLevel(logging.CRITICAL) # Suppress unwanted warnings
    await prompt_template_example()
if __name__ == "__main__":
    asyncio.run(main())