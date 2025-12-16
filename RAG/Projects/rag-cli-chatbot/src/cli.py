from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

# Load the QA chain from the existing 03-RAG.py file
def load_qa_chain():
    loader = TextLoader("ai.txt")
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
    chunks = text_splitter.split_documents(documents)

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 2}
    )

    llm = Ollama(
        model="gemma3:1b",
        temperature=0
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )
    
    return qa_chain

def bot_profile():
    print(f"""\033[92m
    ⣿⣿⣿⣿⣿⣷⣿⣿⣿⡅⡹⢿⠆⠙⠋⠉⠻⠿⣿⣿⣿⣿⣿⣿⣮⠻⣦⡙⢷⡑⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⠡⠌⠂⣙⠻⣛⠻⠷⠐⠈⠛⢱⣮⣷⣽⣿
    ⣿⣿⣿⣿⡇⢿⢹⣿⣶⠐⠁⠀⣀⣠⣤⠄⠀⠀⠈⠙⠻⣿⣿⣿⣦⣵⣌⠻⣷⢝⠦⠚⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣻⣿⣊⡃⠀⣙⠿⣿⣿⣿⣎⢮⡀⢮⣽⣿⣿
    ⢿⣿⣿⣿⣧⡸⡎⡛⡩⠖⠀⣴⣿⣿⣿⠀⠀⠀⠀⠸⠇⠀⠙⢿⣿⣿⣿⣷⣌⢷⣑⢷⣄⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣫⠶⠛⠉⠀⠁⠀⠈⠈⠀⠠⠜⠻⣿⣆⢿⣼⣿⣿⣿
    ⢐⣿⣿⣿⣿⣧⢧⣧⢻⣦⢀⣹⣿⣿⣿⣇⠀⠄⠀⠀⠀⡀⠀⠈⢻⣿⣿⣿⣿⣷⣝⢦⡹⠷⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⠈⠁⠀⠀⠀⠁⠀⠀⠀⠱⣶⣄⡀⠀⠈⠛⠜⣿⣿⣿⣿
    ⠀⠊⢫⣿⣏⣿⡌⣼⣄⢫⡌⣿⣿⣿⣿⣿⣦⡈⠲⣄⣤⣤⡡⢀⣠⣿⣿⣿⣿⣿⣿⣷⣼⣍⢬⣦⡙⣿⣿⣿⣿⣿⣯⢁⡄⠀⡀⡀⠀⠄⢈⣠⢪⠀⣿⣿⣿⣦⠀⢉⢂⠹⡿⣿⣿
    ⠀⠀⠄⢹⢃⢻⣟⠙⣿⣦⠱⢻⣿⣿⣿⣿⣿⣿⣷⣬⣍⣭⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡙⢿⣼⡿⣿⣿⣿⣿⣿⣷⣄⠘⣱⢦⣤⡴⡿⢈⣼⣿⣿⣿⣇⣴⣶⣮⣅⢻⣿⡏
    ⠀⠀⠈⠹⣇⢡⢿⡆⠻⣿⣷⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣍⡻⣿⣟⣻⣿⣿⣿⣿⣷⣦⣥⣬⣤⣴⣾⣿⣿⣿⣿⣷⣿⣿⣿⣿⣷⡜⠃
    ⠀⠀⠀⢀⣘⠈⢂⠃⣧⡹⣿⣷⡄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣅⡙⢿⣟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⡕⠂
    ⠀⠀⠀⠀⠀⠀⠛⢷⣜⢷⡌⠻⣿⣿⣦⣝⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣹⣷⣦⣹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠉⠃⠀
    """)

def main():
    qa_chain = load_qa_chain()
    print("Welcome to the RAG CLI Chatbot! Type 'exit' to quit.")
    
    while True:
        print("""\033[34m 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⢸⡇⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠙⢻⡟⠁⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡀⢰⡄⠀⣄⠀⠻⣦⣸⣇⡾⠋⠀⣤⠀⢰⡆⣀⡀⠀⠀
⠀⠀⠀⢈⣹⣿⣧⣀⢻⡄⠀⠈⢻⡏⠀⠀⢰⣏⣠⡼⣿⣍⠀⠀⠀
⠀⠀⠀⠈⠁⣀⣠⣭⡿⢷⣄⡀⢸⡇⢀⣤⠿⢿⣥⣄⡀⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠈⣙⣿⣿⣋⠁⠀⠀⠀⠈⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠛⢶⣶⡶⠟⠉⢸⡇⠙⠻⣶⣶⡞⠛⠃⠀⠀⠀⠀
⠀⠀⠀⠈⣛⣶⡾⠋⣽⠃⠀⠀⣸⣇⠀⠀⠸⡏⠛⢶⣾⡛⠀⠀⠀
⠀⠀⠀⠘⠋⢸⠇⠀⠟⠀⣠⡾⢻⡟⢷⣄⠀⠿⠀⠸⡏⠙⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢀⣼⣧⡀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢹⡏⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
        question = input("\033[34m>> You: ")
        if question.lower() == 'exit':
            print("Goodbye!")
            break
        
        answer = qa_chain.invoke(question)
        bot_profile()
        print(f"""
|--------------------------------------------------------------------------|
>> {answer['result']}
|--------------------------------------------------------------------------|
""")

if __name__ == "__main__":
    main()