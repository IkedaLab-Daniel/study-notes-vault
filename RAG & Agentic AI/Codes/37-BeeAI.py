import asyncio
from email import message
import logging
from beeai_framework.backend import UserMessage, SystemMessage
from beeai_framework.adapters.groq import GroqChatModel
from openai import project
from utils import print_agent

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

# async def main() -> None:
#     logging.getLogger('asyncio').setLevel(logging.CRITICAL) # Suppress unwanted warnings
#     await prompt_template_example()
# if __name__ == "__main__":
#     asyncio.run(main())

## -- Structured output magic (Pydantic) -- ##
import asyncio
import logging
from pydantic import BaseModel, Field
from typing import List
from beeai_framework.backend import UserMessage, SystemMessage
from beeai_framework.adapters.groq import GroqChatModel

# Define a structured output for business planning
class BusinessPlan(BaseModel):
    """A comprehensive business plan structure."""
    business_name: str = Field(description="Catchy name for the business")
    elevator_pitch: str = Field(description="30-second description of the business")
    target_market: str = Field(description="Primary target audience")
    unique_value_proposition: str = Field(description="What makes this business special")
    revenue_streams: List[str] = Field(description="Ways the business will make money")
    startup_costs: str = Field(description="Estimated initial investment needed")
    key_success_factors: List[str] = Field(description="Critical elements for success")

# > Generate structured business plans
async def structured_output_example():
    llm = GroqChatModel(
        model_id="llama-3.3-70b-versatile"
    )

    messages = [
        SystemMessage(content="You are an expert business consultant and entrepreneur."),
        UserMessage(content="Create a business plan for a mobile app that helps people find and book unique local experiences in their city.")
    ]

    response = await llm.run(messages, response_format=BusinessPlan)

    plan = response.output_structured
    if isinstance(plan, BaseModel):
        plan = plan.model_dump()
    elif plan is None:
        plan = {}

    print("User: Create a business plan for a mobile app that helps people find and book unique local experiences in their city.")
    print("\n🚀 AI-Generated Business Plan:")
    print(f"💡 Business Name: {plan.get('business_name', 'N/A')}")
    print(f"🎯 Elevator Pitch: {plan.get('elevator_pitch', 'N/A')}")
    print(f"👥 Target Market: {plan.get('target_market', 'N/A')}")
    print(f"⭐ Unique Value Proposition: {plan.get('unique_value_proposition', 'N/A')}")
    print(f"💰 Revenue Streams: {', '.join(plan.get('revenue_streams', []))}")
    print(f"💵 Startup Costs: {plan.get('startup_costs', 'N/A')}")
    print(f"🔑 Key Success Factors:")
    for factor in plan.get('key_success_factors', []):
        print(f"  - {factor}")

        
# async def main() -> None:
#     logging.getLogger('asyncio').setLevel(logging.CRITICAL) # Suppress unwanted warnings
#     await structured_output_example()
# if __name__ == "__main__":
#     asyncio.run(main())

## -- BeeAI Agent -- ## 
import asyncio
import logging
from beeai_framework.agents.requirement import RequirementAgent
from beeai_framework.memory import UnconstrainedMemory
from beeai_framework.backend import ChatModel, ChatModelParameters
from beeai_framework.adapters.groq import GroqChatModel

async def minimal_tracked_agent_example():
    """
    Minimal RequirementAgent
    """
    llm = GroqChatModel(
        model_id="llama-3.3-70b-versatile"
    )

     # CONSISTENT SYSTEM PROMPT (used in all examples)
    SYSTEM_INSTRUCTIONS = """You are an expert cybersecurity analyst specializing in threat assessment and risk analysis.

Your methodology:
1. Analyze the threat landscape systematically
2. Research authoritative sources when available
3. Provide comprehensive risk assessment with actionable recommendations
4. Focus on practical, implementable security measures"""

    minimal_agent = RequirementAgent(
        llm=llm,
        tools=[],
        memory=UnconstrainedMemory(),
        instructions=SYSTEM_INSTRUCTIONS
    )

    # CONSISTENT QUERY (used in all examples)
    ANALYSIS_QUERY = """Analyze the cybersecurity risks of quantum computing for financial institutions. 
    What are the main threats, timeline for concern, and recommended preparation strategies?"""

    result = await minimal_agent.run(ANALYSIS_QUERY)
    print(f"\n💬 Pure LLM Analysis:\n{result.output_structured.response}")

# async def main() -> None:
#     logging.getLogger('asyncio').setLevel(logging.CRITICAL)
#     await minimal_tracked_agent_example()

# if __name__ == "__main__":
#     asyncio.run(main())

## -- Tool calling with RequirementAgent -- ##
import asyncio
import logging
from beeai_framework.agents.requirement import RequirementAgent
from beeai_framework.agents.requirement.requirements.conditional import ConditionalRequirement
from beeai_framework.memory import UnconstrainedMemory
from beeai_framework.adapters.groq import GroqChatModel
from beeai_framework.tools.search.wikipedia import WikipediaTool
from beeai_framework.middleware.trajectory import GlobalTrajectoryMiddleware
from beeai_framework.tools import Tool

async def wikipedia_enhanced_agent_example():
    """
    RequirementAgent with Wikipedia - Research Enhancement and tracking
    
    Adding WikipediaTool provides access to Wikipedia summaries for contextual research.
    Same query - but now with research capability.
    Moreover, middleware is used to track all tool usage.
    """

    llm = GroqChatModel(
            model_id="llama-3.3-70b-versatile"
        )
    
    # SAME SYSTEM PROMPT as Example 1
    SYSTEM_INSTRUCTIONS = """You are an expert cybersecurity analyst specializing in threat assessment and risk analysis.

Your methodology:
1. Analyze the threat landscape systematically
2. Research authoritative sources when available
3. Provide comprehensive risk assessment with actionable recommendations
4. Focus on practical, implementable security measures"""
    
    wikipedia_agent = RequirementAgent(
        llm=llm,
        tools=[WikipediaTool()],
        memory=UnconstrainedMemory(),
        middlewares=[GlobalTrajectoryMiddleware(included=(Tool,))],
        requirements=[ConditionalRequirement(WikipediaTool, max_invocations=2)]
    )

    # SAME QUERY as Example 1
    ANALYSIS_QUERY = """Analyze the cybersecurity risks of quantum computing for financial institutions. 
    What are the main threats, timeline for concern, and recommended preparation strategies?"""
    
    result = await wikipedia_agent.run(ANALYSIS_QUERY)
    print(f"\n📖 Research-Enhanced Analysis:\n{result.output_structured.response}")

# async def main() -> None:
#     logging.getLogger('asyncio').setLevel(logging.CRITICAL)
#     await wikipedia_enhanced_agent_example()

# if __name__ == "__main__":
#     asyncio.run(main())

## -- Reasoning -- ##
import asyncio
import logging
from beeai_framework.agents.requirement import RequirementAgent
from beeai_framework.agents.requirement.requirements.conditional import ConditionalRequirement
from beeai_framework.memory import UnconstrainedMemory
from beeai_framework.adapters.groq import GroqChatModel
from beeai_framework.tools.think import ThinkTool
from beeai_framework.tools.search.wikipedia import WikipediaTool
from beeai_framework.middleware.trajectory import GlobalTrajectoryMiddleware
from beeai_framework.tools import Tool

async def reasoning_enhanced_agent_example():
    """
    RequirementAgent with Systematic Reasoning - ThinkTool + WikipediaTool
    
    Adding ThinkTool enables structured reasoning alongside research.
    Same query, same tracking - now with visible thinking process.
    """

    llm = GroqChatModel(
        model_id="llama-3.3-70b-versatile"
    )

    # SAME SYSTEM PROMPT as previous examples
    SYSTEM_INSTRUCTIONS = """You are an expert cybersecurity analyst specializing in threat assessment and risk analysis.

Your methodology:
1. Analyze the threat landscape systematically
2. Research authoritative sources when available
3. Provide comprehensive risk assessment with actionable recommendations
4. Focus on practical, implementable security measures"""

    reasoning_agent = RequirementAgent(
        llm=llm,
        tools=[ThinkTool(), WikipediaTool()],
        memory=UnconstrainedMemory(),
        instructions=SYSTEM_INSTRUCTIONS,
        middlewares=[GlobalTrajectoryMiddleware(included=[Tool,])],
        requirements=[
            ConditionalRequirement(ThinkTool, max_invocations=2),
            ConditionalRequirement(WikipediaTool, max_invocations=2)
        ]
    )

    # SAME QUERY as previous examples
    ANALYSIS_QUERY = """Analyze the cybersecurity risks of quantum computing for financial institutions. 
    What are the main threats, timeline for concern, and recommended preparation strategies?"""
    
    result = await reasoning_agent.run(ANALYSIS_QUERY)
    print_agent()
    print(f"\n🧠 Reasoning + Research Analysis:\n   >>   {result.output_structured.response}")

# async def main() -> None:
#     logging.getLogger('asyncio').setLevel(logging.CRITICAL)
#     await reasoning_enhanced_agent_example()

# if __name__ == "__main__":
#     asyncio.run(main())

## -- Controlled execution -- ##
import asyncio
import logging
from beeai_framework.agents.requirement import RequirementAgent
from beeai_framework.memory import UnconstrainedMemory
from beeai_framework.agents.requirement.requirements.conditional import ConditionalRequirement
from beeai_framework.adapters.groq import GroqChatModel
from beeai_framework.tools.search.wikipedia import WikipediaTool
from beeai_framework.tools.think import ThinkTool
from beeai_framework.middleware.trajectory import GlobalTrajectoryMiddleware
from beeai_framework.tools import Tool

async def controlled_execution_example():
    """
    RequirementAgent with Controlled Execution - Requirements System
    
    Requirements provide precise control over tool execution order and behavior.
    Same query, same tracking - but now with strict execution rules.
    """
    llm = GroqChatModel(
            model_id="llama-3.3-70b-versatile"
        )    
    
    # SAME SYSTEM PROMPT as previous examples
    SYSTEM_INSTRUCTIONS = """You are an expert cybersecurity analyst specializing in threat assessment and risk analysis.

Your methodology:
1. Analyze the threat landscape systematically
2. Research authoritative sources when available
3. Provide comprehensive risk assessment with actionable recommendations
4. Focus on practical, implementable security measures"""
    
    # RequirementAgent with strict execution control
    controlled_agent = RequirementAgent(
        llm=llm,
        tools=[ThinkTool(), WikipediaTool()],
        memory=UnconstrainedMemory(),
        instructions=SYSTEM_INSTRUCTIONS,
        middlewares=[GlobalTrajectoryMiddleware(included=(Tool,))],

        # > Requirements
        requirements=[
            ConditionalRequirement(
                ThinkTool,
                force_at_step=1,
                min_invocations=1,
                max_invocations=3,
                consecutive_allowed=False
            ),

            ConditionalRequirement(
                WikipediaTool,
                only_after=[ThinkTool],
                min_invocations=1,
                max_invocations=2
            )
        ]
    )

    # SAME QUERY as all previous examples
    ANALYSIS_QUERY = """Analyze the cybersecurity risks of quantum computing for financial institutions. 
    What are the main threats, timeline for concern, and recommended preparation strategies?"""
    
    result = await controlled_agent.run(ANALYSIS_QUERY)
    print_agent()
    print(f"\n🔧 Controlled Execution Analysis:\n   >>   {result.output_structured.response}")


# async def main() -> None:
#     logging.getLogger('asyncio').setLevel(logging.CRITICAL)
#     await controlled_execution_example()

# if __name__ == "__main__":
#     asyncio.run(main())

## -- ReAct Agent -- ##
import asyncio
import logging
from beeai_framework.agents.requirement import RequirementAgent
from beeai_framework.adapters.groq import GroqChatModel
from beeai_framework.memory import UnconstrainedMemory
from beeai_framework.tools.search.wikipedia import WikipediaTool
from beeai_framework.tools.think import ThinkTool
from beeai_framework.middleware.trajectory import GlobalTrajectoryMiddleware
from beeai_framework.tools import Tool

async def reasoning_enhanced_agent_example():
    llm = GroqChatModel(
            model_id="llama-3.3-70b-versatile"
        )
    
    # SAME SYSTEM PROMPT as previous examples
    SYSTEM_INSTRUCTIONS = """You are an expert cybersecurity analyst specializing in threat assessment and risk analysis.

Your methodology:
1. Analyze the threat landscape systematically
2. Research authoritative sources when available
3. Provide comprehensive risk assessment with actionable recommendations
4. Focus on practical, implementable security measures"""
    
    # RequirementAgent with reasoning + research capability
    reasoning_agent = RequirementAgent(
        llm=llm,
        tools=[ThinkTool(), WikipediaTool()],
        memory=UnconstrainedMemory(),
        middlewares=[GlobalTrajectoryMiddleware(included=(Tool,))],
        instructions=SYSTEM_INSTRUCTIONS,
        requirements=[
            ConditionalRequirement(
                ThinkTool,
                force_at_step=1,
                force_after=Tool, # ? Force reasoning after every tool call
                min_invocations=1,
                max_invocations=5,
                consecutive_allowed=False
            ),
            ConditionalRequirement(
                WikipediaTool,
                only_after=[ThinkTool],
                max_invocations=2
            )
        ]
    )

    # SAME QUERY as previous examples
    ANALYSIS_QUERY = """Analyze the cybersecurity risks of quantum computing for financial institutions. 
    What are the main threats, timeline for concern, and recommended preparation strategies?"""
    
    result = await reasoning_agent.run(ANALYSIS_QUERY)
    print_agent()
    print(f"\n🧠 Reasoning + Research Analysis:\n   >>   {result.output_structured.response}")

# async def main() -> None:
#     logging.getLogger('asyncio').setLevel(logging.CRITICAL)
#     await reasoning_enhanced_agent_example()

# if __name__ == "__main__":
#     asyncio.run(main())

## -- Human-in-the-loop -- ##
import asyncio
import logging
from beeai_framework.agents.requirement import RequirementAgent
from beeai_framework.adapters.groq import GroqChatModel
from beeai_framework.agents.requirement.requirements.conditional import ConditionalRequirement
from beeai_framework.agents.requirement.requirements.ask_permission import AskPermissionRequirement
from beeai_framework.memory import UnconstrainedMemory
from beeai_framework.tools.search.wikipedia import WikipediaTool
from beeai_framework.tools.think import ThinkTool
from beeai_framework.middleware.trajectory import GlobalTrajectoryMiddleware
from beeai_framework.tools import Tool

async def production_security_example():
    """
    Production-Ready RequirementAgent with Security Approval
    
    AskPermissionRequirement adds human-in-the-loop security controls.
    Same query, same tracking - but now with approval workflow.
    """
    llm = GroqChatModel(
            model_id="llama-3.3-70b-versatile"
        )    
    # SAME SYSTEM PROMPT as all previous examples
    SYSTEM_INSTRUCTIONS = """You are an expert cybersecurity analyst specializing in threat assessment and risk analysis.

Your methodology:
1. Analyze the threat landscape systematically
2. Research authoritative sources when available
3. Provide comprehensive risk assessment with actionable recommendations
4. Focus on practical, implementable security measures"""
    
    # Production-grade RequirementAgent with security approval
    secure_agent = RequirementAgent(
        llm=llm,
        tools=[ThinkTool(), WikipediaTool()],
        instructions=SYSTEM_INSTRUCTIONS,
        memory=UnconstrainedMemory(),
        middlewares=[GlobalTrajectoryMiddleware(included=(Tool,))],

        requirements=[
            ConditionalRequirement(
                ThinkTool,
                force_at_step=1,
                force_after=Tool, # ? Force reasoning after every tool call
                min_invocations=1,
                max_invocations=5,
                consecutive_allowed=False
            ),
            # SECURITY
            AskPermissionRequirement(
                WikipediaTool,
            ),
            ConditionalRequirement(
                WikipediaTool,
                only_after=[ThinkTool],
                min_invocations=0,  # Optional after approval
                max_invocations=1  # Limited even after approval
            )
        ]
    )

    # SAME QUERY as all previous examples
    ANALYSIS_QUERY = """Analyze the cybersecurity risks of quantum computing for financial institutions. 
    What are the main threats, timeline for concern, and recommended preparation strategies?"""
    
    result = await secure_agent.run(ANALYSIS_QUERY)
    print_agent()
    print(f"\n🛡️ Security-Approved Analysis:\n   >>   {result.output_structured.response}")

# async def main() -> None:
#     logging.getLogger('asyncio').setLevel(logging.CRITICAL)
#     await production_security_example()

# if __name__ == "__main__":
#     asyncio.run(main())

## -- Custom Tool -- ##
import asyncio
import logging
from beeai_framework.agents.experimental import RequirementAgent
from beeai_framework.memory import UnconstrainedMemory
from beeai_framework.tools import StringToolOutput, Tool, ToolRunOptions
from beeai_framework.context import RunContext
from beeai_framework.emitter import Emitter
from beeai_framework.adapters.groq import GroqChatModel
from beeai_framework.middleware.trajectory import GlobalTrajectoryMiddleware
from pydantic import BaseModel, Field
from typing import Any

# === REAL TOOL CREATION WITH OFFICIAL BEEAI TOOLS ===

class CalculatorInput(BaseModel):
    """Input model for basic mathematical calculations."""
    expression: str = Field(description="Mathematical expression using +, -, *, / (e.g., '10 + 5', '20 - 8', '4 * 6', '15 / 3')")

class SimpleCalculatorTool(Tool[CalculatorInput, ToolRunOptions, StringToolOutput]):
    """A simple calculator tool for basic arithmetic operations: add, subtract, multiply, divide."""
    name = "SimpleCalculator"
    description = "Performs basic arithmetic calculations: addition (+), subtraction (-), multiplication (*), and division (/)."
    input_schema = CalculatorInput

    def __init__(self, options: dict[str, Any] | None = None) -> None:
        super().__init__(options)

    def _create_emitter(self) -> Emitter:
        return Emitter.root().child(
            namespace=["tool", "calculator", "basic"],
            creator=self,
        )

    def _safe_calculate(self, expression: str) -> float:
        """Safely evaluate basic arithmetic expressions."""
        # Remove spaces for processing
        expr = expression.replace(' ', '')
        
        # Only allow numbers, basic operators, parentheses, and decimal points
        allowed_chars = set('0123456789+-*/().')
        if not all(c in allowed_chars for c in expr):
            raise ValueError("Only numbers and basic operators (+, -, *, /, parentheses) are allowed")
        
        try:
            # Use eval with restricted environment for basic arithmetic only
            result = eval(expr, {"__builtins__": {}}, {})
            return float(result)
        except ZeroDivisionError:
            raise ValueError("Division by zero is not allowed")
        except Exception as e:
            raise ValueError(f"Invalid arithmetic expression: {str(e)}")

    async def _run(
        self, input: CalculatorInput, options: ToolRunOptions | None, context: RunContext
    ) -> StringToolOutput:
        """Perform basic arithmetic calculations."""
        try:
            expression = input.expression.strip()
            
            # Perform calculation
            result = self._safe_calculate(expression)
            
            # Format result
            output = f"🧮 Simple Calculator\n"
            output += f"Expression: {expression}\n"
            output += f"Result: {result}\n"
            
            # Add operation type hint
            if '+' in expression:
                output += "Operation: Addition"
            elif '-' in expression:
                output += "Operation: Subtraction"
            elif '*' in expression:
                output += "Operation: Multiplication"
            elif '/' in expression:
                output += "Operation: Division"
            else:
                output += "Operation: Basic Arithmetic"
            
            return StringToolOutput(output)
            
        except ValueError as e:
            return StringToolOutput(f"❌ Calculation Error: {str(e)}")
        except Exception as e:
            return StringToolOutput(f"❌ Unexpected Error: {str(e)}")

async def calculator_agent_example():
    """RequirementAgent with SimpleCalculatorTool - Interactive Math Assistant"""
    
    llm = GroqChatModel(
            model_id="llama-3.3-70b-versatile"
        )        
    # Create calculator agent with our custom tool
    calculator_agent = RequirementAgent(
        llm=llm,
        tools=[SimpleCalculatorTool()],
        memory=UnconstrainedMemory(),
        instructions="""You are a helpful math assistant. When users ask for calculations, 
        use the SimpleCalculator tool to provide accurate results. 
        Always show both the expression and the calculated result.""",
        middlewares=[GlobalTrajectoryMiddleware(included=[Tool])],
    )
    
    # Interactive examples - simulating human input
    math_queries = [
        "What is 15 + 27?",
        "Calculate 144 divided by 12",
        "I need to know what 8 times 9 equals",
        "What's (10 + 5) * 3 - 7?"
    ]
    
    for query in math_queries:
        print(f"\n👤 Human: {query}")
        result = await calculator_agent.run(query)
        print(f"🤖 Agent: {result.output_structured.response}")

async def main() -> None:
    logging.getLogger('asyncio').setLevel(logging.CRITICAL)
    await calculator_agent_example()

if __name__ == "__main__":
    asyncio.run(main())
