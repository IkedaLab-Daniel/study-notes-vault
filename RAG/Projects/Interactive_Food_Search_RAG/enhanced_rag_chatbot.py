from shared_functions import *
from typing import List, Dict, Any
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watsonx_ai.foundation_models import ModelInference
import json
from dotenv import load_dotenv
import os

load_dotenv()

# > Global variables
food_items = []

# IBM Watsonx.ai Configuration
my_credentials = {
    "url": "https://jp-tok.ml.cloud.ibm.com",
    "apikey": os.getenv("API_KEY")
}

model_id = 'ibm/granite-3-8b-instruct'
gen_parms = {"max_new_tokens": 400}
project_id = os.getenv("PROJECT_ID")
space_id = None
verify = False

# > Initialize the LLM model
model = ModelInference(
    model_id=model_id,
    credentials=my_credentials,
    params=gen_parms,
    project_id=project_id,
    space_id=space_id,
    verify=verify
)

def main():
    """Main function for enchanced RAG chatbot system"""
    try:
        print("🤖 Enhanced RAG-Powered Food Recommendation Chatbot")
        print("   Powered by IBM Granite & ChromaDB")
        print("=" * 55)

        #  > 1 - Load food data
        global food_items
        food_items = load_food_data('./FoodDataSet.json')

        # > 2 - Create collection for RAG system
        collection = create_similarity_search_collection(
            "enchanced_rag_food_chatbot",
            {'description': 'Enhanced RAG chatbot with IBM watsonx.ai integration'}
        )

        # > 3 - Add the loaded food items into collection
        populate_similarity_collection(collection, food_items)

        # > 4 - Test LLM conncetion
        print("\nTesting LLM connection...")
        test_response = model.generate(prompt="Hello", params=None)
        if test_response and "results" in test_response:
            print("✅ LLM connection established")
        else:
            print("❌ LLM connection failed")
            return

        # > 5 - Start enchanced RAG chatbot
        # TODO: enchanced_rag_food_chatbot(collection)
        

    except Exception as Ice:
        print("Error", Ice)

if __name__ == "__main__":
    main()
    print(" --- End --- ")