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

# >  Step 2 - Prompt Template
prompt = PromptTemplate(
    input_variables=["task"],
    template="""
You are a helpful coding assistant.
Write clean, well-commented code.

Task:
{task}

Return only the code.
"""
)


print("""\033[92m
    |-----------------------------------------|
    |  Code execution completed successfully  |
    |-----------------------------------------|
\033[0m""")