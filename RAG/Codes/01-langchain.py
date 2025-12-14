# import warnings # ? Ignore Warning
# warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# > Step 1 - Connect to local LLM
llm = Ollama(
    model="codellma",
    temperature=0.2
)

print("""\033[92m
    |-----------------------------------------|
    |  Code execution completed successfully  |
    |-----------------------------------------|
\033[0m""")