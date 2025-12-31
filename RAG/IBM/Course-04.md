# Advanced RAG with Vector Databases and Retrievers

> # Module 1

## Advanced Retrievers and Vector Databases for RAG

* This course focuses on using vector databases and advanced retrievers to build high-performance Retrieval-Augmented Generation (RAG) applications.
* You will gain deep expertise in advanced retriever strategies and how they improve the relevance, accuracy, and grounding of LLM-generated responses.
* The course emphasizes practical implementation and comparison of retriever types such as:

  * Multi-query retrievers
  * Self-querying retrievers
  * Parent-document retrievers
* You will learn how retrievers work within LangChain and LlamaIndex and how retrieval strategies directly impact RAG quality.
* The course covers vector database indexing methods, including:

  * Graph-based indexing
  * Hierarchical Navigable Small World (HNSW)
  * Locality Sensitive Hashing (LSH)
* You will understand how indexing strategies affect retrieval speed, scalability, and semantic accuracy.
* Hands-on labs guide you in applying and evaluating retrievers using LangChain, LlamaIndex, FAISS, and ChromaDB.
* You will build a complete RAG-powered application using LangChain and Gradio.
* Practical exercises focus on retrieval design, evaluation, and integration with vector databases.
* The course is designed for developers, engineers, data scientists, AI engineers, AI enthusiasts, and computer science students working with LLMs and semantic search.
* Prerequisites include Python programming, familiarity with vector databases, and working knowledge of RAG and similarity search.
* The course consists of two modules:

  * **Module 1: Advanced Retrievers for RAG**

    * Introduction to retrievers in LangChain
    * Standard vector store retrievers and advanced retriever types
    * Hands-on extraction of relevant document chunks
    * Index types and advanced retrievers in LlamaIndex
    * Query Fusion Retriever and fusion strategies
  * **Module 2: Build a Comprehensive RAG Application**

    * Introduction to FAISS and comparison with ChromaDB
    * FAISS index types and extension using Milvus
    * Understanding when to use FAISS vs ChromaDB
    * Semantic similarity search with FAISS
    * Building a YouTube transcript Q&A summarization tool using FAISS and LangChain
* By the end of the course, you will be equipped to build intelligent, scalable, and context-aware RAG systems using advanced retrieval and indexing techniques.

## Explore Advanced Retrievers in Langchain: Part 1

* A **LangChain retriever** is an interface that returns documents or document chunks in response to an unstructured text query.
* Retrievers are more general than vector stores; their role is retrieval, not necessarily storage.
* A retriever takes a **string query as input** and returns a **list of documents or chunks** as output.
* One of the simplest retriever types is the **vector store-based retriever**.
* This retriever works on top of an existing **vector database** created by:

  * Loading source documents
  * Splitting them into chunks
  * Embedding those chunks
* The vector store-based retriever embeds the user query and compares it with stored embeddings to retrieve the most relevant chunks.
* Retrieval can be performed using:

  * **Similarity search**, which returns chunks most similar to the query
  * **Maximum Marginal Relevance (MMR)**, which balances relevance and diversity
* **MMR** reduces redundancy by selecting results that are relevant to the query while being less similar to each other.
* The vector store-based retriever is simple and efficient because it does not require an LLM during retrieval.
* In LangChain, this retriever can be created directly from a vector store using the `retriever` method.
* Vector store-based retrievers are commonly used as the baseline retrieval method in RAG pipelines.

## Explore Advanced Retrievers in Langchain: Part 2

* A **LangChain retriever** is an interface that returns documents or chunks based on an unstructured query.
* Beyond the basic vector store-based retriever, LangChain provides **advanced retrievers** to improve recall, relevance, and context handling.

### Multi-Query Retriever

* Uses an **LLM to generate multiple alternative versions of a user query**.
* Each query variant is executed against a base retriever (usually a vector store-based retriever).
* The results from all queries are combined and deduplicated to produce a richer set of documents.
* Helps overcome issues caused by:

  * Subtle differences in query wording
  * Imperfect embeddings that fail to capture full semantics
* Can work with different retrieval strategies such as similarity search or MMR.

### Self-Query Retriever

* Designed for documents that include **metadata** (e.g., year, rating, author).
* Uses an LLM to split a user query into:

  * A **semantic search query** (text)
  * A **metadata filter** (structured constraints)
* Requires:

  * A vector store
  * Descriptions of document metadata fields
* Enables queries like filtering documents by numeric or categorical metadata (e.g., movies with ratings above a threshold).
* Improves precision by combining semantic search with structured filtering.

### Parent Document Retriever

* Addresses the trade-off between **small chunks for accurate embeddings** and **large chunks for better context**.

* Uses two text splitters:

  * **Child splitter**: creates small chunks for embedding
  * **Parent splitter**: creates larger chunks for retrieval

* During retrieval:

  * Small chunks are matched via embeddings
  * Their parent documents are returned as results

* Ensures retrieved content has sufficient context while maintaining embedding quality.

* These advanced retrievers enhance RAG systems by improving recall, relevance, and contextual completeness compared to basic vector store-based retrieval.

## Advanced Retrievers in LlamaIndex

* **LlamaIndex** provides multiple index types and retrievers to build flexible, intelligent retrieval pipelines for RAG and search systems.

### Core Index Types

* **VectorStoreIndex**

  * Stores vector embeddings for document chunks.
  * Best for semantic search based on meaning.
  * Commonly used with LLM-powered pipelines and RAG.

* **DocumentSummaryIndex**

  * Generates and stores summaries at indexing time.
  * Uses summaries to filter relevant documents before retrieving full content.
  * Ideal for large, diverse document collections that exceed LLM context limits.

* **KeywordTableIndex**

  * Extracts keywords and maps them to content chunks.
  * Enables exact keyword matching.
  * Useful for rule-based or hybrid search scenarios.

### Core and Advanced Retrievers

* **Vector Index Retriever**

  * Uses embeddings to retrieve semantically similar content.
  * Ideal for general-purpose search and RAG pipelines.

* **BM25 Retriever**

  * Keyword-based retrieval using exact matches.
  * Improves on TF-IDF with term frequency saturation and document length normalization.
  * Effective for technical or keyword-sensitive documents.

* **Document Summary Index Retriever**

  * Retrieves documents using summaries instead of full text.
  * Two variants:

    * LLM-based (more accurate but slower and more expensive)
    * Embedding-based semantic similarity (more efficient for large datasets)
  * Always returns full documents, not summaries.

* **Auto Merging Retriever**

  * Uses hierarchical chunking with parent and child nodes.
  * If enough child nodes from the same parent are retrieved, returns the parent node.
  * Preserves broader context in long documents.

* **Recursive Retriever**

  * Follows references between nodes, such as citations or metadata links.
  * Supports chunk and metadata references.
  * Useful for research papers and interconnected documents.

* **Query Fusion Retriever**

  * Combines results from multiple retrievers (e.g., vector + keyword).
  * Can generate multiple query variations using an LLM.
  * Improves recall through result fusion.

### Fusion Strategies

* **Reciprocal Rank Fusion**

  * Prioritizes documents ranked highly across multiple retrievers.
  * Robust and independent of score scales.

* **Relative Score Fusion**

  * Normalizes scores within each retriever.
  * Preserves relative confidence of each result set.

* **Distribution-Based Fusion**

  * Uses statistical normalization (e.g., z-scores, percentiles).
  * Handles large score variability effectively.

### Recommended Use Cases

* **General Q&A**: Vector Index Retriever + BM25 Retriever.

* **Technical documents**: BM25 as primary, Vector Retriever as secondary.

* **Long documents**: Auto Merging Retriever.

* **Research papers**: Recursive Retriever.

* **Large document collections**: Document Summary Index Retriever followed by Vector Search.

* LlamaIndex’s combination of index types, retrievers, and fusion strategies enables scalable, accurate, and context-aware retrieval pipelines.

## Summary: Advanced Retrievers for RAG

- A LangChain retriever is an interface that returns documents based on an unstructured query
- There are several different types of LangChain retrievers
- The vector store-based retriever retrieves documents from a vector database
- A vector store-based retriever can be created directly from the vector store object with the retriever method by using similarity search or MMR 
- That similarity search is when the retriever accepts a query and retrieves the most similar data
- MMR is a technique used to balance the relevance and diversity of retrieved results
- The multi-query retriever uses an LLM to create different versions of the query, generating a richer set of retrieved documents
- The self query retriever converts the query into two components, a string to look up semantically, and a metadata filter to accompany it
- The parent document retriever has two text splitters: a parent splitter that splits the text into large chunks to be retrieved, and a child splitter that splits the document into small chunks to generate meaningful embeddings
- The core LlamaIndex index types are the VectorStoreIndex, the DocumentSummaryIndex, and the KeywordTableIndex
- The VectorStoreIndex stores vector embeddings for each document chunk, is best suited for semantic retrieval, and is commonly used in pipelines that involve large language models
- The DocumentSummaryIndex generates and stores summaries of documents, which are used to filter documents before retrieving the full content, and is useful when working with large and diverse document sets 
- The KeywordTableIndex extracts keywords from documents and maps them to specific content chunks, and is useful in hybrid or rule-based search scenarios
- The Vector Index Retriever uses vector embeddings to find semantically related content, and is ideal for general-purpose search and RAG pipelines
- The BM25 Retriever is a keyword-based method for ranking documents, and it retrieves content based on exact keyword matches rather than semantic similarity
- The Document Summary Index Retriever uses document summaries instead of the actual documents to find relevant content
- There are two versions of the Document Summary Index Retriever, one uses LLM, and the other uses semantic similarity
- The Auto Merging Retriever preserves context in long documents using a hierarchical structure, and uses hierarchical chunking to break documents into parent and child nodes
- The Recursive Retriever follows relationships between nodes and uses references such as citations in academic papers or metadata links
- The Query Fusion Retriever combines results from different retrievers using fusion strategies
- The fusion strategies supported by the Query Fusion Retriever are Reciprocal Rank Fusion, Relative Score Fusion, and Distribution-Based Fusion

> # Module 2

## Introduction to FAISS vs Chroma DB

* **FAISS (Facebook AI Similarity Search)** and **Chroma DB** are tools for vector similarity search, but they’re designed for different goals and use cases.

---

### What is FAISS?

* A **library** developed by Meta for fast vector similarity search.
* Runs on a **single machine** (CPU or GPU).
* No built-in database or server—you interact with it purely through code.
* Offers **fine-grained control** and **high performance**.
* Best when you want maximum optimization and are comfortable managing everything yourself.

---

### What is Chroma DB?

* A **full vector database** built specifically for AI applications.
* Stores **vectors + metadata** (tags, descriptions, IDs).
* Can run **locally or as a server**.
* Easy to integrate with **LangChain and LlamaIndex**.
* Optimized for fast prototyping and developer convenience.

---

### Key Differences: FAISS vs Chroma DB

| Feature                | FAISS             | Chroma DB                      |
| ---------------------- | ----------------- | ------------------------------ |
| Type                   | Library           | Database                       |
| Deployment             | Single-node only  | Single-node or distributed     |
| Metadata support       | ❌ Not native      | ✅ Built-in                     |
| Index options          | Many              | HNSW only                      |
| Ease of use            | Low-level, manual | High-level, developer-friendly |
| LangChain / LlamaIndex | ✅ Yes             | ✅ Yes                          |

---

### FAISS Index Types

Indexes trade off **speed, memory, and accuracy**.

### 1. Flat Index

* Brute-force comparison against all vectors.
* Uses Euclidean distance or dot product.
* ✅ Most accurate
* ❌ Very slow for large datasets

---

### 2. Inverted File Index (IVF)

* Clusters vectors using methods like **k-means**.
* Searches only within the nearest clusters (Voronoi cells).
* ✅ Much faster than flat
* ⚠️ Slight accuracy loss

---

### 3. Locality-Sensitive Hashing (LSH)

* Uses hash functions to group similar vectors.
* Fast and memory-efficient.
* Good for **high-dimensional sparse data** (e.g., text).
* ⚠️ Neither the fastest nor most accurate option

---

### 4. Hierarchical Navigable Small World (HNSW)

* Organizes vectors into **multiple graph layers**.
* Top layers: sparse, fast navigation
* Lower layers: dense, fine-grained search
* Search starts at the top and moves downward.
* ✅ Fast **and** accurate for large datasets
* This is the **only index type used by Chroma DB**

---

## Extending FAISS with Milvus

FAISS alone lacks:

* Metadata filtering
* Distributed scaling

**Milvus** fills these gaps:

* Uses FAISS as an indexing engine.
* Supports **metadata + hybrid queries**
  *(e.g., “find similar items under $50”)*
* Enables **distributed, production-scale deployments**

---

## When to Use What?

* **Use FAISS**

  * You want full control and maximum performance.
  * Single-machine setup is enough.
  * You’re building custom or experimental systems.

* **Use Chroma DB**

  * You want fast prototyping.
  * You need metadata filtering.
  * You’re building AI apps or RAG pipelines quickly.

* **Use Milvus**

  * You need production-ready scalability.
  * You want metadata + hybrid search.
  * You’re working with large, distributed datasets.

---

## Key Takeaways

* FAISS = power and control, but low-level.
* Chroma DB = ease of use and metadata support.
* Milvus = FAISS + scalability + metadata.
* All three can integrate with **LangChain** and **LlamaIndex**.
* Choose based on **project size, complexity, and infrastructure needs**.