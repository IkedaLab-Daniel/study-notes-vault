import math

import numpy as np
import scipy
import torch
from sentence_transformers import SentenceTransformer

# > Obtain Vector Embeddings
documents = [
    'Bugs introduced by the intern had to be squashed by the lead developer.',
    'Bugs found by the quality assurance engineer were difficult to debug.',
    'Bugs are common throughout the warm summer months, according to the entomologist.',
    'Bugs, in particular spiders, are extensively studied by arachnologists.'
]

# > Load Pre-Trained model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# > Generate Embeddings
embeddings = model.encode(documents)
print("\033[92m\n\n")
# print(embeddings.shape)
# print(embeddings)

# > Manual implementation of L2 distance calculation
def euclidean_distance_fn(vector1, vector2):
    squared_sum = sum((x - y) ** 2 for x, y in zip(vector1, vector2))
    return math.sqrt(squared_sum)

print(f"\nEuclidean Distance for \n >> {documents[0]}\n >> {documents[1]}")
print(euclidean_distance_fn(embeddings[0], embeddings[1]))

print(f"\nEuclidean Distance for \n >> {documents[1]}\n >> {documents[2]}")
print(euclidean_distance_fn(embeddings[1], embeddings[2]))

print("-- End --")