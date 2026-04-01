from pydoc import describe

from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

CYAN = "\033[96m"
BOLD = "\033[1m"
WHITE = "\033[97m"
BLUE = "\033[94m"
GRAY = "\033[90m"
RESET = "\033[0m"

## -- Setup Serper -- ##

load_dotenv()
SERPER_API = os.getenv('SERPER_API')
os.environ['SERPER_API_KEY'] = SERPER_API

search_tool = SerperDevTool()

search_query = "Latest Breakthroughs in machine learning"
search_results = search_tool.run(search_query=search_query)

for item in search_results.get("organic", []):
    print(f"{CYAN}[{item['position']}] {BOLD}{WHITE}{item['title']}{RESET}")
    print(f"{BLUE}{item['link']}{RESET}")
    print(f"{GRAY}{item['snippet']}{RESET}\n")

## -- Setup LLM -- ##

from crewai import LLM

llm = LLM(
    #model="groq/llama-3.1-8b-instant",
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API"),
    max_tokens=300
)

print(llm.call)

## -- Defining an Agent Directly as a Python Object -- ##

from crewai import Agent

research_agent = Agent(
    role='Senior Research Analyst',
    goal="Uncover cutting-edge information and insights on any subject with comprehensive analysis",
    backstory="""You are an expert researcher with extensive experience in gathering, analyzing, and synthesizing information across multiple domains. 
    Your analytical skills allow you to quickly identify key trends, separate fact from opinion, and produce insightful reports on any topic. 
    You excel at finding reliable sources and extracting valuable information efficiently.""",
    verbose=True,
    allow_delegation=False,
    llm = llm,
    tools=[SerperDevTool()]
)

writer_agent = Agent(
    role='Tech Content Strategist',
    goal='Craft well-structured and engaging content based on research findings',
    backstory="""You are a skilled content strategist known for translating 
    complex topics into clear and compelling narratives. Your writing makes 
    information accessible and engaging for a wide audience.""",
    verbose=True,
    llm = llm,
    allow_delegation=True
)

## -- Tasks -- ##

from crewai import Task

research_task = Task(
    description="Analyze the major {topic}, identifying key trends and technologies. Provide a detailed report on their potential impact.",
    agent=research_agent,
    expected_output="A detailed report on {topic}, including trends, emergin technologies, and their impact."
)

# Create a task for the Writer Agent
writer_task = Task(
  description="Create an engaging blog post based on the research findings about {topic}. Tailor the content for a tech-savvy audience, ensuring clarity and interest.",
  agent=writer_agent,
  expected_output="A 4-paragraph blog post on {topic}, written clearly and engagingly for tech enthusiasts."
)

## -- Workflow -- ##

from crewai import Crew, Process

crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, writer_task],
    process=Process.sequential,
    verbose=False
)

result = crew.kickoff(inputs={"topic": "Latest Generative AI breakthroughs"})

final_output = result.raw
print("Final output:", final_output)