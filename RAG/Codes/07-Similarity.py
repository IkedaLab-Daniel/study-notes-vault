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

# print(f"\nEuclidean Distance for \n >> {documents[0]}\n >> {documents[1]}")
# print(euclidean_distance_fn(embeddings[0], embeddings[1]))

# print(f"\nEuclidean Distance for \n >> {documents[1]}\n >> {documents[2]}")
# print(euclidean_distance_fn(embeddings[1], embeddings[2]))

# > Compare all
l2_dist_manual = np.zeros([4,4])
for i in range(embeddings.shape[0]):
    for j in range(embeddings.shape[0]):
        l2_dist_manual[i,j] = euclidean_distance_fn(embeddings[i], embeddings[j])

print(f"Distance of Vector 1, Vector 2: {l2_dist_manual[0,1]}")
print(f"Distance of Vector 2, Vector 1: {l2_dist_manual[1,0]}")

# > Compare all - improved
l2_dist_manual_improved = np.zeros([4,4])
for i in range(embeddings.shape[0]):
    for j in range(embeddings.shape[0]):
        if j > i:
            l2_dist_manual_improved[i,j] = euclidean_distance_fn(embeddings[i], embeddings[j])
        elif i > j:
            l2_dist_manual_improved[i,j] = l2_dist_manual_improved[j,i]

print(f"Distance of Vector 1, Vector 2: {l2_dist_manual_improved[0,1]}")
print(f"Distance of Vector 2, Vector 1: {l2_dist_manual_improved[1,0]}")
# ? Measure distance between vectors -> Lower = Similar/Closer to each other

# > Calculate using scipy
l2_dist_scipy = scipy.spatial.distance.cdist(embeddings, embeddings, "euclidean")
print(l2_dist_scipy)
print(np.allclose(l2_dist_manual, l2_dist_scipy))

# > Manual implementation of dot product calculation
def dot_product_fn(vector1, vector2):
    return sum(x * y for x,y in zip(vector1, vector2))

print(f"\nDot Product of vector 1 and vector 2 is: {dot_product_fn(embeddings[0], embeddings[1])}")
print(f"\nDot Product of vector 2 and vector 3 is: {dot_product_fn(embeddings[1], embeddings[2])}")

# > Calculate dot product between all vectors
dot_product_manual = np.empty([4,4])
for i in range(embeddings.shape[0]):
    for j in range(embeddings.shape[0]):
        dot_product_manual[i,j] = dot_product_fn(embeddings[i], embeddings[j])

print(f"Dot Product Manual: \n {dot_product_manual}")
# ? Measures Similarity -> Higher = More Similar

# > Matrix multiplication operator
dot_product_operator = embeddings @ embeddings.T
print(dot_product_manual)
print(np.allclose(dot_product_manual, dot_product_operator, atol=1e-05))

# ? Equivalent to `np.matmul()` if both arrays are 2-D:
print(np.matmul(embeddings,embeddings.T))

# > Calculate dot product distance
"""
    > The dot product between two vectors provides a similarity score. 
    > If, on the other hand, we would like a distance, we can simply take the negative of the dot product:
"""
dot_product_distance = -dot_product_manual
print(dot_product_distance)

# > Cosine Similarity and Distance
# > Manual Implementation
    # > Calculate L2 norm
l2_norms = np.sqrt(np.sum(embeddings**2, axis=1))
print("\n", l2_norms)

    # > L2 norms reshape
l2_norms_reshaped = l2_norms.reshape(-1, 1)
print("\n", l2_norms_reshaped)

# > Normalize embedding vectors
normalized_embeddings_manual = embeddings/l2_norms_reshaped
print("\n", normalized_embeddings_manual)

# > Verify that vectors are normalized
print("\nVerify:")
print(np.sqrt(np.sum(normalized_embeddings_manual**2, axis=1)))

# > Normalize embedding using PyTorch
normalized_embedding_torch = torch.nn.functional.normalize(
    torch.from_numpy(embeddings)
).numpy()

print("\n", normalized_embedding_torch)
# ? Verifiy
print(np.allclose(normalized_embeddings_manual, normalized_embedding_torch))

# > Calculate cosine similary manually
print("\nCosine similary of Vector 1 and 2:", dot_product_fn(normalized_embeddings_manual[0], normalized_embeddings_manual[1]))

# > Calculate All
cosine_similarity_manual = np.empty([4,4])
for i in range(normalized_embeddings_manual.shape[0]):
    for j in range(normalized_embeddings_manual.shape[0]):
        cosine_similarity_manual[i,j] = dot_product_fn(
            normalized_embeddings_manual[i], 
            normalized_embeddings_manual[j]
        )

print("\n", cosine_similarity_manual)

# > Calculate cosng similarity using matrix calculation
cosine_similarity_operator = normalized_embeddings_manual @ normalized_embeddings_manual.T
print("\n", cosine_similarity_operator)

# > Calculate cosine distance
print("\n")
print(1 - cosine_similarity_manual)

# > Similarity Search Using a Query
# ? Embed the query
query_embedding = model.encode(
    ["Who is responsible for a coding project and fixing others' mistakes?"]
)

# ? Normalize the query embedding
normalized_query_embedding = torch.nn.functional.normalize(
    torch.from_numpy(query_embedding)
).numpy()

# ? Third, calculate the cosine similarity between the documents and the query by using the dot product:
cosine_similarity_q3 = normalized_embeddings_manual @ normalized_query_embedding.T

# ? Fourth, find the position of the vector with the highest cosine similarity:
highest_cossim_position = cosine_similarity_q3.argmax()

# ? Fifth, find the document in that position in the `documents` array:
print("\n")
print(documents[highest_cossim_position])

print("-- End --")