from dotenv import load_dotenv
import os
load_dotenv()

# > Retrieve Top 2 Results Using a Vector Store-Backed Retriever

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from ibm_watsonx_ai.metanames import EmbedTextParamsMetaNames
from langchain_ibm import WatsonxEmbeddings
from utils import print_agent

def text_splitter(data, chunk_size, chunk_overlap):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )

    # ? Use split_documents for Document objects, split_text for strings
    if isinstance(data, list):
        chunk = splitter.split_documents(data)
    else:
        chunk = splitter.split_text(data)
    return chunk

def watsonx_embedding():
    embed_params = {
        EmbedTextParamsMetaNames.TRUNCATE_INPUT_TOKENS: 3,
        EmbedTextParamsMetaNames.RETURN_OPTIONS: {"input_text": True},
    }

    watsonx_embedding = WatsonxEmbeddings(
        model_id="ibm/slate-125m-english-rtrvr-v2",
        url=os.getenv("URL"),
        project_id=os.getenv("PROJECT_ID"),
        params=embed_params,
        apikey=os.getenv("API_KEY")
    )

    return watsonx_embedding

def main():
    loader = TextLoader('./companypolicies.txt')
    txt_file = loader.load()
    chunks = text_splitter(txt_file, 200, 20)

    
    vectordb = Chroma.from_documents(chunks, watsonx_embedding())

    retriever = vectordb.as_retriever(search_kwargs={"k": 2})

    query = "smoking policy"
    results = retriever.invoke(input=query)
    print_agent()
    print(f" >> Query: {query}")
    print(f"Total Result/s: {len(results)}:")
    
    for i in range(len(results)):
        print("-------------------------", i + 1, "-------------------------")
        print(f"   >> {results[i].page_content}\n")

if __name__ == "__main__":
    print(""" 
11 - Exercise 2: Retrieve the top two results for the company policy document for the query "smoking policy" using the Vector Store-Backed Retriever.
""")
    main()