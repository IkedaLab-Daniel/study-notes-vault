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
print(embeddings.shape)

print("-- End --")