from shared_functions import *

def main():
    """Main function for advanced search demonstrations"""
    try:
        print("---- Advanced Food Search System ----")
        print("=" * 50)
        print("Loading food database with advanced filtering capabilities...")

        # > Load food data from JSON file
        food_items = load_food_data('./FoodDataSet.json')
        
        # > Create collection specifically for advance search ops
        collection = create_similarity_search_collection(
            "advanced_food_search",
            {'description': 'A collection for advanced search demos'}
        )

        populate_similarity_collection(collection, food_items)

        # > Start the interactive advanced search interface
        # interactive_advanced_search(collection) # TODO ---

    except Exception as Ice:
        print("Advanced search error:", Ice)

if __name__ == "__main__":
    main()