from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

load_dotenv()
SERPER_API = os.getenv('SERPER_API')

search_tool = SerperDevTool()
# print(type(search_tool))