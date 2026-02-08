# import warnings # ? Ignore Warning
# warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")
from random import randint
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# > Step 1 - Connect to local LLM
model = "gemma3:1b"

llm = OllamaLLM(
    model=model,
    temperature=0.2,
)

# >  Step 2 - Prompt Template
prompt = PromptTemplate(
    input_variables=["task"],
    template="""
You are a helpful coding assistant for HTML 
Add CSS <style> and JS <script> on the same file (HTML) if needed.

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
user_prompt = input("Enter code generation request: ")
result = chain.run(
    task=user_prompt
)

# > Step 5 - HTML file creation
    #  > Remove code block markers if present
if result.startswith("```html"):
    result = result[len("```html"):].lstrip()
if result.endswith("```"):
    result = result[:-3].rstrip()

    # > Save HTML
filename = "./generations/Output" + str((randint(1,1000))) + ".html"
with open(filename, "x") as file:
    print(f"{filename} successfully created...")
with open(filename, "w") as file:
    file.write(result)

print(result)
print(f"""\033[92m
    |-----------------------------------------|
    >> Code execution completed successfully <<
      >>  Code: {filename} <<
    |-----------------------------------------|
\033[0m""")