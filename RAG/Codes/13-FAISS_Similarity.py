import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import faiss
import re
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from pprint import pprint

# Suppressing warnings
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')


# > Dataset setupfrom sklearn.datasets import fetch_20newsgroups
from sklearn.datasets import fetch_20newsgroups
try:
    newsgroups_train = fetch_20newsgroups(subset='train')
    documents = newsgroups_train.data
except Exception as e:
    print(f"fetch_20newsgroups failed: {e}\nUsing local fallback documents.")
    documents = [
        "This is a sample document about machine learning and vectors.",
        "Natural language processing and semantic search with FAISS.",
        "Notes on software engineering, debugging, and code reviews.",
        "A short text about motorcycles and travel adventures."
    ]

print(f"Loaded {len(documents)} documents")

print(" --- End --- ")