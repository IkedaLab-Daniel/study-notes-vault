# rag-cli-chatbot

## Overview
This project implements a command-line interface (CLI) based chatbot that utilizes a retrieval-augmented generation (RAG) approach for answering questions. The chatbot leverages Langchain to load documents, create embeddings, and build a question-answering chain.

## Project Structure
```
rag-cli-chatbot
├── src
│   ├── 03-RAG.py          # Main logic for document processing and QA
│   ├── cli.py             # Command-line interface for the chatbot
│   └── __init__.py        # Package initialization
├── tests
│   └── test_cli.py        # Unit tests for CLI functionality
├── requirements.txt        # Project dependencies
├── .gitignore              # Files to ignore in version control
└── README.md               # Project documentation
```

## Installation
To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd rag-cli-chatbot
pip install -r requirements.txt
```

## Usage
To run the chatbot, execute the following command in your terminal:

```bash
python src/cli.py
```

You will be prompted to enter your questions, and the chatbot will respond based on the loaded documents.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.