# Build RAG Applications: Get Started

> # Module 1

## Course Overview: Getting Started with Retrieval-Augmented Generation (RAG)

* **Retrieval-Augmented Generation (RAG)** is a high-demand skill with strong career potential, offering competitive salaries and rapid market growth across industries such as healthcare, finance, legal tech, e-commerce, education, and customer service.

### Course Audience & Prerequisites

* Designed for aspiring **AI developers, ML engineers, data scientists, and AI researchers**.
* Requires **Python programming skills** and prior experience.
* Familiarity with **LangChain**, basic AI concepts, and web development is recommended.

### What You Will Learn

* **RAG fundamentals**: How retrieval and generative AI work together to produce accurate, context-aware responses.
* **Hands-on Lab 1**:

  * Use LangChain to split documents, generate embeddings, and build simple retrieval chains.
  * Work in a Jupyter Notebook environment.
* **Hands-on Lab 2**:

  * Build a full RAG application by integrating LangChain with a large language model.
  * Use **Gradio** to create an interactive question-and-answer bot.
* **Final Module**:

  * Explore **LlamaIndex** as an alternative RAG framework.
  * Build an icebreaker bot using **IBM Granite** and LlamaIndex.
  * Learn how to transfer RAG skills across frameworks.

### Key Skills Gained

* End-to-end **RAG pipeline development**
* Working with **vector databases**, embeddings, chunking strategies, retrievers, and prompt templates
* Building **interactive AI applications** using Gradio
* Applying RAG concepts across multiple frameworks (LangChain and LlamaIndex)

### Course Outcome

* A solid understanding of RAG architectures
* Practical experience building real-world RAG applications
* Reusable skills for future GenAI and AI-powered projects

## Introduction to Retrieval-Augmented Generation (RAG)

* **Retrieval-Augmented Generation (RAG)** is an AI framework that improves the responses of large language models (LLMs) by combining them with external knowledge sources, without retraining the model.
* It is especially useful for **domain-specific or confidential information** (e.g., company policies) that LLMs are not trained on.

## Why RAG Is Needed

* Pre-trained LLMs perform well on general knowledge but may produce **inaccurate or incomplete answers** for specialized domains.
* RAG supplements LLMs with **organization-specific data** such as internal documents, policies, and large text files to ensure accurate responses.

## Core Components of RAG

* **Retriever**: The core of RAG, responsible for finding relevant information from a knowledge base.
* **Generator**: The LLM that generates natural-language responses using the retrieved information.

## RAG Process Overview

1. **Text Embedding**

   * User prompts and knowledge base documents are converted into **high-dimensional vectors**.
   * A **question encoder** embeds the prompt.
   * A **context encoder** embeds the knowledge base documents.

2. **Chunking Knowledge Base**

   * Large documents are split into **smaller text chunks** for efficient retrieval.
   * Each chunk is embedded and stored with a unique **chunk ID**.

3. **Vector Storage**

   * Embedded chunks are stored in a **vector database**.
   * Each vector represents the semantic meaning of a text chunk.

4. **Retrieval**

   * The system compares the prompt vector with stored vectors using **distance metrics**.
   * Common metrics:

     * **Dot product**: Considers magnitude and direction.
     * **Cosine similarity**: Focuses on directional similarity.
   * The **top K most similar chunks** are selected.

5. **Augmented Query Creation**

   * Retrieved text chunks are combined with the original prompt to form an **augmented query**.

6. **Generation**

   * The LLM uses the augmented query to generate a **context-aware, accurate response**.

## Prompt and Context Encoding

* **Token embedding** converts words or sub-words into vectors using models like BERT or GPT.
* **Vector averaging** combines token vectors into a single representation for the prompt or text chunk.
* This representation captures the overall meaning of the input text.

## Key Takeaways

* RAG enables chatbots to answer **domain-specific questions** without retraining the LLM.
* It works by embedding prompts and documents, retrieving relevant context using similarity search, and generating responses from augmented input.
* Proper chunking, embedding, and distance metric selection are crucial for **efficient and accurate retrieval**.
* RAG significantly improves reliability when working with **private, large, or specialized datasets**.

## Summary: Introduction to RAG

- Retrieval-Augmented Generation (RAG) is a machine-learning technique that integrates information retrieval with generative AI to produce accurate and context-aware responses. 
- RAG enhances Large Language Models (LLMs) by integrating external or domain-specific knowledge without retraining. This helps LLMs generate more accurate and contextually relevant responses for specialized queries, such as a company’s mobile policy.
- RAG consists of two main components: the Retriever, which extracts relevant data from a knowledge base, and the Generator, which uses the retrieved information to generate responses in natural language.
- The RAG process comprises four steps: Text Embedding, Retrieval, Augmented Query Creation, and Model Generation.
- Text Embedding converts user prompts and knowledge base documents into high-dimensional vectors using AI models such as BERT or GPT.
- Retrieval matches the user query with similar vectors from the knowledge base to retrieve relevant information.
- Augmented Query Creation combines retrieved content with the user prompt.
- Model Generation uses the created augmented query to generate a response using the content from the knowledge base.
- Prompt encoding converts a text-based prompt into a numerical representation that an LLM can process. It uses Token Embedding and Vector Averaging to break documents into smaller text chunks, convert them into vectors, and index them in a vector database.
- Distance Metrics measure similarity between user queries and document vectors using methods such as dot product (magnitude-based) or cosine similarity (direction-based).
- RAG is an efficient response generation technique.  It retrieves the most relevant text chunks from the knowledge base to augment the model’s knowledge and produce an informed response. This ensures responses are accurate, domain-specific, and up-to-date.
- RAG allows chatbots to provide specialized answers by integrating relevant external knowledge, making them more reliable for industry-specific or confidential topics.

## Getting Started with Gradio
### What is Gradio?

* **Gradio** is an **open-source Python library** used to build simple, customizable **web-based user interfaces**.
* It is especially popular for **machine learning models** and computational tools because it requires minimal code and setup.

### How Gradio Works (Step-by-Step)

1. **Write Python functions**

   * Define the logic or model behavior you want users to interact with.
2. **Create a Gradio interface**

   * Use `gr.Interface()` to connect inputs and outputs to your function.
3. **Configure inputs and outputs**

   * Choose components like text boxes, numbers, or file uploads.
4. **Launch the server**

   * Call `.launch()` to start a local Gradio server.
5. **Access the web UI**

   * Gradio provides a **local or public URL** where users can interact in real time.

---

### Installing and Importing Gradio

* Install using pip:

  ```
  pip install gradio
  ```
* Import in Python:

  ```python
  import gradio as gr
  ```

---

### Creating a Simple Text Input–Output Interface

* Define a function that processes user input (e.g., echoing text).
* Use:

  * `gr.Textbox()` for text input
  * `gr.Textbox()` for text output
* Launch the interface to display two text boxes: input and output.

---

### Using Multiple Inputs

* Gradio supports multiple input types:

  * `gr.Textbox()` → text input
  * `gr.Number()` → numeric input
* Inputs are passed as a **list** to `gr.Interface()`.
* This allows combining different input types in one interface.

---

### Uploading Files with Gradio

* `gr.File()` enables users to:

  * Upload or drag-and-drop files
  * Upload multiple files at once
* Uploaded files are passed to the backend function as file paths.
* Useful for tasks like file counting, processing documents, or ML inference.

---

### Key Takeaways

* Gradio makes it easy to turn Python functions into **interactive web apps**.
* Core steps:

  * Write Python logic
  * Create an interface
  * Launch the server
  * Share or access the UI via a URL
* Supports **text, numbers, and file uploads** with minimal code.
* Ideal for **rapid prototyping**, demos, and ML model interaction.
