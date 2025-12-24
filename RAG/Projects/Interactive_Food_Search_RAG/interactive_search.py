from shared_functions import *

# > Global variable to store loaded food items
food_items = []

def main():
    """ Main function for interaction CLI food recommendation system """
    try:
        print("🍽️  Interactive Food Recommendation System")
        print("=" * 50)
        print("Loading food database...")


        # > Load data
        global food_items
        food_items = load_food_data('./FoodDataSet.json') # > Will also print execution result

        # > Create and populate search collection
        collection = create_similarity_search_collection(
            "interactive_food_search",
            {"description": "A collection for interactive food search"}
        )
        populate_similarity_collection(collection, food_items)

        # > Start interactive chatbot
        # interactive_food_chatbot(collection) # TODO
        print(" --- ")

    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    main()