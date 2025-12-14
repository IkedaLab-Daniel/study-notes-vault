from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# > Connect to model
llm = OllamaLLM(
    model="gemma3:1b",
    temperature=0.2
)

propmt = ChatPromptTemplate.from_template(""" 
You are a helpful coding assistant.
Write clean, single, well-commented code.

Task:
{task}

Return only the code.

""")


chain = (
    propmt 
    | llm 
    | StrOutputParser()
)

result = chain.invoke({
    "task": "Python function that checks if a number is prime"
})

print(result)