import os
from dotenv import load_dotenv
import json
import asyncio
import warnings
import numpy as np
from typing import List, Optional

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
        print("Falling back to mock LLM for demonstration")
        
        # ! Fallback mock LLM for demonstration
        from llama_index.core.llms.mock import MockLLM
        return MockLLM(max_tokens=512)


print(" --- working ---")