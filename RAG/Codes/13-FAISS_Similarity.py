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


from datasets import load_dataset
from pprint import pprint

dataset = load_dataset("ag_news")

# > Make it sklearn-like
data = dataset["train"]["text"]
target = dataset["train"]["label"]

# > Display the first 3 posts
for i in range(3):
    print(f"Sample post {i+1}:\n")
    pprint(data[i])
    print("\n" + "-" * 80 + "\n")

# > Basic preprocessing of text data
def preprocess_text(text):
    # ? Remove email headers
    text = re.sub(r'^From:.*\n?', '', text, flags=re.MULTILINE)
    # ? Remove email addresses
    text = re.sub(r'\S*@\S*\s?', '', text)
    # ? Remove punctuations and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # ? Convert to lowercase
    text = text.lower()
    # ? Remove excess whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# ? Preprocess each document
processed_documents = [preprocess_text(doc) for doc in data]


# > Choose a sample post to display
sample_index = 0  # for example, the first post in the dataset

# ? Print the original post
print("\033[93mOriginal post:\n")
print(data[sample_index])
print("\n" + "-"*80 + "\n\033[0m")

# ? Print the preprocessed post
print("\033[92mPreprocessed post:\n")
print(preprocess_text(data[sample_index]))
print("\n" + "-"*80 + "\n\033[0m")

# > Universal Sentence Encoder
import tensorflow_hub as hub
import numpy as np

# Load the Universal Sentence Encoder's TF Hub module (first time can take a bit)
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Suppose processed_documents is your list of preprocessed texts
# Instead of looping, embed everything at once
X_use = embed(processed_documents).numpy()

print(X_use)

print("\n --- End ---")