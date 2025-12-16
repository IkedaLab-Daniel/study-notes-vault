from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
import textwrap

def load_document(file_path):
    loader = TextLoader(file_path)
    return loader.load()

def split_document(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
    return text_splitter.split_documents(documents)

def create_embeddings():
    return OllamaEmbeddings(
        model="nomic-embed-text"
    )

def create_vector_store(chunks, embeddings):
    return FAISS.from_documents(chunks, embeddings)

def create_retriever(vectorstore):
    return vectorstore.as_retriever(
        search_kwargs={"k": 2}
    )

def load_llm():
    return Ollama(
        model="gemma3:1b",
        temperature=0
    )

def build_qa_chain(llm, retriever):
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

def answer_question(qa_chain, question):
    answer = qa_chain.invoke(question)
    return textwrap.fill(answer["result"], width=40)

def main():
    documents = load_document("ai.txt")
    chunks = split_document(documents)
    embeddings = create_embeddings()
    vectorstore = create_vector_store(chunks, embeddings)
    retriever = create_retriever(vectorstore)
    llm = load_llm()
    qa_chain = build_qa_chain(llm, retriever)

    print("\n\n\n")
    while True:
        question = input("Enter your question (or 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        print(f"""\033[34m
|----------------------------------------------------------------|
>>    Question: {question}
|----------------------------------------------------------------|
        \033[0m""")
        wrapped_answer = answer_question(qa_chain, question)
        print(f"""\033[92m
|----------------------------------------------------------------|
>> {wrapped_answer}
|----------------------------------------------------------------|
""")

if __name__ == "__main__":
    main()