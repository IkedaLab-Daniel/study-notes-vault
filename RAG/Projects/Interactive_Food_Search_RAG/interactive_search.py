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

def interactive_food_chatbot(collection):
    """Interactive CLI chatbot for food recommendations"""
    print("\n" + "="*50)
    print("🤖 INTERACTIVE FOOD SEARCH CHATBOT")
    print("="*50)
    print("Commands:")
    print("  • Type any food name or description to search")
    print("  • 'help' - Show available commands")
    print("  • 'quit' or 'exit' - Exit the system")
    print("  • Ctrl+C - Emergency exit")
    print("-" * 50)

    while True:
        try:
            # > Get user input
            user_input = input("\n🔍 Search for food: ").strip()

            # > Handle empty input
            if not user_input:
                print("   Please enter a search term or 'help' for commands")
                continue

            # > Handle exit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Thank you for using the Food Recommendation System!")
                print("   Goodbye!")
                break
            # > Handle help command
            elif user_input.lower() in ['help', 'h']:
                show_help_menu()
            # Handle food search
            else:
                handle_food_search(collection, user_input)
        except KeyboardInterrupt:
            print("\n\n👋 System interrupted. Goodbye!")
            break
        except Exception as ice:
            print("Error:", ice)

def show_help_menu():
    """Display help information for users"""
    print("\n📖 HELP MENU")
    print("-" * 30)
    print("Search Examples:")
    print("  • 'chocolate dessert' - Find chocolate desserts")
    print("  • 'Italian food' - Find Italian cuisine")
    print("  • 'sweet treats' - Find sweet desserts")
    print("  • 'baked goods' - Find baked items")
    print("  • 'low calorie' - Find lower-calorie options")
    print("\nCommands:")
    print("  • 'help' - Show this help menu")
    print("  • 'quit' - Exit the system")
    
if __name__ == "__main__":
    main()