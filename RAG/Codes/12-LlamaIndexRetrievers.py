import os
from dotenv import load_env
import json
import asyncio
import warnings
import numpy as np
from typing import List, Optional

warnings.filterwarnings('ignore')
load_env()

# > Core LlamaIndex imports
from llama_index.core import (
    VectorStoreIndexm,
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