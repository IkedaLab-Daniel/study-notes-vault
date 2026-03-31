from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

CYAN = "\033[96m"
BOLD = "\033[1m"
WHITE = "\033[97m"
BLUE = "\033[94m"
GRAY = "\033[90m"
RESET = "\033[0m"

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