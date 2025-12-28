import os
from dotenv import load_dotenv
import json
import asyncio
import warnings
import numpy as np
from typing import List, Optional
from utils import print_agent

warnings.filterwarnings('ignore')
load_dotenv()

# > Core LlamaIndex imports
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Document,
    Settings,
    DocumentSummaryIndex,
    KeywordTableIndex
)

from llama_index.core.retrievers import (
    BaseRetriever,
    VectorIndexRetriever,
    AutoMergingRetriever,
    RecursiveRetriever,
    QueryFusionRetriever
)

from llama_index.core.indices.document_summary import (
    DocumentSummaryIndexLLMRetriever,
    DocumentSummaryIndexEmbeddingRetriever
)

from llama_index.core.node_parser import SentenceSplitter, HierarchicalNodeParser
from llama_index.core.schema import NodeWithScore, QueryBundle
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SentenceTransformerRerank
from llama_index.core.embeddings import BaseEmbedding
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# > Advance retriever imports
from llama_index.retrievers.bm25 import BM25Retriever

# > IBM WatsonX LlmanaIndex Integration
from ibm_watsonx_ai import APIClient
from llama_index.llms.ibm import WatsonxLLM

# > Sentence transformers
from sentence_transformers import SentenceTransformer

# > Statistical libraries for fusion techniques
try:
    from scipy import stats
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False
    print("⚠️ scipy not available - some advanced fusion features will be limited")

print("✅ All imports successful!")

API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")
PROJECT_ID = os.getenv("PROJECT_ID")

# > Watsonx.ai LLM integration
# >> watson.ai LLM using officialk LlamaIndex integration
def create_watson_llm():
    """Create watsonx.ai LLM instance using official LlamaIndex integration."""

    try:
        # > Client the API client object
        api_client = APIClient({
            "url": URL,
            "api_key": API_KEY
        })

        # > # Use llama-index-llms-ibm (official watsonx.ai integration)
        llm = WatsonxLLM(
            model_id="meta-llama/llama-3-3-70b-instruct",
            url=URL,
            project_id=PROJECT_ID,
            api_client=api_client,
            temperature=0.1
        )
        print("✅ watsonx.ai LLM initialized using official LlamaIndex integration")

        # > Test Watson
        # response = llm.complete("I'm sleepy, so I'll drink a hot black ")
        # print(f"🤖 Watson response: {response}")

        return llm
    except Exception as e:
        print(f"⚠️ watsonx.ai initialization error: {e}")
        print("⚠️ Falling back to mock LLM for demonstration")
        
        # ! Fallback mock LLM for demonstration
        from llama_index.core.llms.mock import MockLLM
        return MockLLM(max_tokens=512)

# > Initialize embedding model first
print("🔧 Initializing HuggingFace embeddings...")
embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)
print("✅ HuggingFace embeddings initialized!")

# > Setup with watsonx.ai
print("🔧 Initializing watsonx.ai LLM...")
llm = create_watson_llm()

# > Configure global settings
Settings.llm = llm
Settings.embed_model = embed_model
print("✅ watsonx.ai LLM and embeddings configured!")

# > Sample Data Setup
# Sample data for the lab - AI/ML focused documents
SAMPLE_DOCUMENTS = [
    "Machine learning is a subset of artificial intelligence that focuses on algorithms that can learn from data.",
    "Deep learning uses neural networks with multiple layers to model and understand complex patterns in data.",
    "Natural language processing enables computers to understand, interpret, and generate human language.",
    "Computer vision allows machines to interpret and understand visual information from the world.",
    "Reinforcement learning is a type of machine learning where agents learn to make decisions through rewards and penalties.",
    "Supervised learning uses labeled training data to learn a mapping from inputs to outputs.",
    "Unsupervised learning finds hidden patterns in data without labeled examples.",
    "Transfer learning leverages knowledge from pre-trained models to improve performance on new tasks.",
    "Generative AI can create new content including text, images, code, and more.",
    "Large language models are trained on vast amounts of text data to understand and generate human-like text."
]

# Consistent query examples used throughout the lab
DEMO_QUERIES = {
    "basic": "What is machine learning?",
    "technical": "neural networks deep learning", 
    "learning_types": "different types of learning",
    "advanced": "How do neural networks work in deep learning?",
    "applications": "What are the applications of AI?",
    "comprehensive": "What are the main approaches to machine learning?",
    "specific": "supervised learning techniques"
}

print(f"📄 Loaded {len(SAMPLE_DOCUMENTS)} sample documents")
print(f"🔍 Prepared {len(DEMO_QUERIES)} consistent demo queries")
for i, doc in enumerate(SAMPLE_DOCUMENTS[:3], 1):
    print(f"{i}. {doc}")
print("...")

# > Initialize Lab Environment
class AdvancedRetrieversLab:
    def __init__(self):
        print("🚀 Initializing Advanced Retrievers Lab...")
        self.documents = [Document(text=text) for text in SAMPLE_DOCUMENTS]
        self.nodes = SentenceSplitter().get_nodes_from_documents(self.documents)

        print("📊 Creating indexes...")
        self.vector_index = VectorStoreIndex.from_documents(self.documents)
        self.document_summary_index = DocumentSummaryIndex.from_documents(self.documents)
        self.keyword_index = KeywordTableIndex.from_documents(self.documents)

# > Init lab
lab = AdvancedRetrieversLab()

# > Core Retriever Demonstration - Vector Index Retriever
def demo_vector_index_retriever():
    print("=" * 60)
    print("1. VECTOR INDEX RETRIEVER")
    print("=" * 60)

        # >> Basic Vector Retriever
    vector_retriever = VectorIndexRetriever(
        index=lab.vector_index,
        similarity_top_k=3
    )

        # > Alternative creation method
    alt_retriever = lab.vector_index.as_retriever(similarity_top_k=3)

    query = DEMO_QUERIES["basic"]
    nodes = vector_retriever.retrieve(query)

    print(f"Query: {query}")
    print(f"Retrieved {len(nodes)} nodes:")

    for i, node in enumerate(nodes, 1):
        print(f"{i}. Score: {node.score:.4F}")
        print(f"    Text: {node.text[:100]}")
        print()

def demo_BM25():
    print("=" * 60)
    print("2. BM25 Retriever")
    print("=" * 60)

    try:
        import Stemmer

        # > Create BM25 retriever with default parameters
        bm25_retriever = BM25Retriever.from_defaults(
            nodes=lab.nodes,
            similarity_top_k=3,
            stemmer=Stemmer.Stemmer("english"),
            language="english"
        )

        query = DEMO_QUERIES["technical"]
        nodes = bm25_retriever.retrieve(query)
        print_agent()
        print(f"Query: {query}")
        print("BM25 analyzes exact keyword matches with sophisticated scoring")
        print(f"Retrieved {len(nodes)} nodes:")

        for i, node in enumerate(nodes, 1):
            score = node.score if hasattr(node, 'score') and node.score else 0
            print(f"{i}. BM25 Score: {score:.4f}")
            print(f"    Text: {node.text[:100]}")

            # > Highlight which query terms appear in text
            text_lower = node.text.lower()
            query_terms = query.lower().split()
            found_terms = [term for term in query_terms if term in text_lower]
            if found_terms:
                print(f"    -> Found terms: {found_terms}")
            print()
        
        print("BM25 vs TF-IDF Comparison:")
        print("TF-IDF Problem: Linear term frequency scaling")
        print("  Example: 10 occurrences → score of 10, 100 occurrences → score of 100")
        print("BM25 Solution: Saturation function")
        print("  Example: 10 occurrences → high score, 100 occurrences → slightly higher score")
        print()
        print("TF-IDF Problem: No document length consideration")
        print("  Example: Long documents dominate results")
        print("BM25 Solution: Length normalization (b parameter)")
        print("  Example: Scores adjusted based on document length vs. average")
        print()
        print("Key BM25 Parameters:")
        print("- k1 ≈ 1.2: Term frequency saturation (how quickly scores plateau)")
        print("- b ≈ 0.75: Document length normalization (0=none, 1=full)")
        print("- IDF weighting: Rare terms get higher scores")

    except ImportError:
        print("⚠️ BM25Retriever requires 'pip install PyStemmer'")
        print("Demonstrating BM25 concepts with fallback vector search...")

        fallback_retriever = lab.vector_index.as_retriever(similarity_top_k=3)
        query = DEMO_QUERIES["technical"]
        nodes = fallback_retriever.retrieve(query)

        print(f"Query: {query}")
        print("(Using vector fallback to demonstrate BM25 concepts)")
        
        for i, node in enumerate(nodes, 1):
            print(f"{i}. Vector Score: {node.score:.4f}")
            print(f"   Text: {node.text[:100]}...")
            
            # > Demonstrate TF-IDF concept manually
            text_lower = node.text.lower()
            query_terms = query.lower().split()
            found_terms = [term for term in query_terms if term in text_lower]
            
            if found_terms:
                print(f"   → BM25 would boost this result for terms: {found_terms}")
            print()
        
        print("BM25 Concept Demonstration:")
        print("1. TF-IDF Foundation:")
        print("   - Term Frequency: How often words appear in document")
        print("   - Inverse Document Frequency: How rare words are across collection")
        print("   - TF-IDF = TF × IDF (balances frequency vs rarity)")
        print()
        print("2. BM25 Improvements:")
        print("   - Saturation: Prevents over-scoring repeated terms")
        print("   - Length normalization: Prevents long document bias")
        print("   - Tunable parameters: k1 (saturation) and b (length adjustment)")
        print()
        print("3. Real-world Usage:")
        print("   - Elasticsearch default scoring function")
        print("   - Apache Lucene/Solr standard")
        print("   - Used in 83% of text-based recommender systems")
        print("   - Developed by Robertson & Spärck Jones at City University London")

def demo_document_summary_index_retriever():
    print("=" * 60)
    print("3. DOCUMENT SUMMARY INDEX RETRIEVERS")
    print("=" * 60)

    # > LLM-Based
    doc_summary_retriever_llm = DocumentSummaryIndexLLMRetriever(
        lab.document_summary_index,
        choice_top_k=3
    )

    # > Embedding-Based
    doc_summary_retriever_embedding = DocumentSummaryIndexEmbeddingRetriever(
        lab.document_summary_index,
        similarity_top_k=3
    )

    query = DEMO_QUERIES["learning_types"]
    print(f"Query: {query}")
    

demo_document_summary_index_retriever()

print(" --- working ---")