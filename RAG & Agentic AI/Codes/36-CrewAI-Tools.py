from tabnanny import verbose

from crewai import Agent, Task, Crew, Process
from crewai import LLM
from crewai_tools import PDFSearchTool, SerperDevTool

from dotenv import load_dotenv
load_dotenv()
import os

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API"),
    max_tokens=1000
)

os.environ['SERPER_API_KEY'] = 'SERPER_API_KEY'

web_search_tool = SerperDevTool()

## -- PDF Search Tool -- ##

pdf_search_tool = PDFSearchTool(
    pdf="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/7vgNfis17dQfjHAiIKkBOg/The-Daily-Dish-FAQ.pdf",
    config=dict(
        embedder=dict(
            provider="huggingface",
            config=dict(
                model="sentence-transformers/all-MiniLM-L6-v2"
            )
        )
    )
)

## -- Approach 1: The Standard Method (Agent-Centric Tools // Generalist)

# > 1.1. Create the Agent
agent_centric_agent = Agent(
    role="The Daily Dish Inquiry Specialist",
    goal="""ccurately answer customer questions about The Daily Dish restaurant. 
    You must decide whether to use the restaurant's FAQ PDF or a web search to find the best answer.""",
    backstory="""You are an AI assistant for 'The Daily Dish'.
    You have access to two tools: one for searching the restaurant's FAQ document and another for searching the web.
    Your job is to analyze the user's question and choose the most appropriate tool to find the information needed to provide a helpful response.""",
    tools=[pdf_search_tool, web_search_tool],
    verbose=True,
    allow_delegation=False,
    llm=llm   
)

# > 1.2 Define the Task

agent_centric_task = Task(
    description="Answer the following customer query: '{customer_query}'. "
                "Analyze the question and use the tools at your disposal (PDF search or web search) to find the most relevant information. "
                "Synthesize the findings into a clear and friendly response.",
    expected_output="A comprehensive and well-formatted answer to the customer's query",
    agent=agent_centric_agent
)

# > 1.3 Assemble Crew

agent_centric_crew = Crew(
    agents=[agent_centric_agent],
    tasks=[agent_centric_task],
    process=Process.sequential,
    verbose=False
)


## -- Approach 2: A More Focused Method (Task-Centric Tools) -- ##

# > 2.1 Create the Agent
task_centric_agent = Agent(
    role="Customer Service Specialist",
    goal="Provide exceptional customer service by following a multi-step process to answer customer questions accurately.",
    backstory="""You are an AI assistant for 'The Daily Dish'.
    You are an expert at following instructions. You will be given a sequence of tasks to complete.
    For each task, you will be provided with the specific tool needed to accomplish it.
    Your job is to execute each task diligently and pass the results to the next step.""",
    tools=[], # The agent is not given any tools directly
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# > Define the Tasks with Specific Tools
faq_search_task = Task(
    description="Search the restaurant's FAQ PDF for information related to the customer's query: '{customer_query}'.",
    expected_output="A snippet of the most relevant information from the PDF, or a statement that the information was not found.",
    tools=[pdf_search_tool], # Tool assigned directly to the task
    agent=task_centric_agent
)

response_drafting_task = Task(
    description="Using the information gathered from the FAQ search, draft a friendly and comprehensive response to the customer's query: '{customer_query}'.",
    expected_output="The final, customer-facing response.",
    agent=task_centric_agent,
    context=[faq_search_task]
)

# > Assemble the New Crew
task_centric_crew = Crew(
    agents=[task_centric_agent],
    tasks=[faq_search_task, response_drafting_task],
    process=Process.sequential,
    verbose=True
)