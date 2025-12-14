# import warnings # ? Ignore Warning
# warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# > Step 1 - Connect to local LLM
llm = OllamaLLM(
    model="gemma3:1b",
    temperature=0.2,
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

# > Step 3 - Create chain
chain = LLMChain(
    llm=llm,
    prompt=prompt
)

# > Step 4 - Run Chain
result = chain.run(
    task="Python function that checks if a number is prime"
)

print(result)



print("""\033[92m
    |-----------------------------------------|
    |  Code execution completed successfully  |
    |-----------------------------------------|
\033[0m""")