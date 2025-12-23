import chromadb
from chromadb.utils import embedding_functions
import json
import re
import numpy as np
from typing import List, Dict, Any, Optional

print("\033[92m --- Start --- ")

# > Initialize ChromaDB client
client = chromadb.Client()

# > Data Loading function
def load_food_data(file_path: str) -> List[Dict]:
    """ Load food data from JSON file"""

    try:
        print("Attempting to load data")
        with open(file_path, 'r', encoding='utf-8') as file:
            food_data = json.load(file)

        # > Ensure each item has required field and normalize the structure
        for i, item in enumerate(food_data):

            # > 1 - Normalize food_id to string
            if 'food_id' not in item:
                item['food_id'] = str(i + 1)
            else:
                item['food_id'] = str(item['food_id'])

            # > 2 - Ensure required fields exist
            if 'food_ingredients' not in item:
                item['food_ingredients'] = []
            if 'food_description' not in item:
                item['food_description'] = ''
            if 'cuisine_type' not in item:
                item['cuisine_type'] = 'Unknown'
            if 'food_calories_per_serving' not in item:
                item['food_calories_per_serving'] = 0

            # > 3 - Extract taste features from nested food_features if available
            if 'food_features' in item and isinstance(item['food_features'], dict):
                taste_features = []
                for key, value in item['food_features'].items():
                    if value:
                        taste_features.append(str(value))
                item['taste_profile'] = ", ".join(taste_features)
            else:
                item['taste_profile'] = ""
            
        print(f"Successfully loaded {len(food_data)} food items form {file_path}")
        return food_data

    except Exception as error:
        print("\033[911mError:", error)
        return []

# > Collection Setup Function
def create_similarity_search_collection(collection_name: str, collection_metadata: dict = None):
    """"Create ChromaDB collection with sentence transformer embeddings"""
    try:
        # > Try to delete existing collection to start fresh
        result = client.delete_collection(collection_name)
    except Exception as error:
        pass

    # > Create embedding function
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    # > Create new collection
    return client.create_collection(
        name=collection_name,
        metadata=collection_metadata,
        configuration={
            "hnws": {"space": "cosine"},
            "embedding_function": sentence_transformer_ef
        }
    )

print(" --- End --- ")