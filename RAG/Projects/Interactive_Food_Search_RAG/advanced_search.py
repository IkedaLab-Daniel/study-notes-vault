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
        interactive_advanced_search(collection)

    except Exception as Ice:
        print("Advanced search error:", Ice)

def interactive_advanced_search(collection):
    """Interactive advanced search with filtering options"""
    print("\n" + "="*50)
    print("🔧 ADVANCED SEARCH WITH FILTERS")
    print("="*50)
    print("Search Options:")
    print("  1. Basic similarity search")
    print("  2. Cuisine-filtered search")  
    print("  3. Calorie-filtered search")
    print("  4. Combined filters search")
    print("  5. Demonstration mode")
    print("  6. Help")
    print("  7. Exit")
    print("-" * 50)
    
    while True:
        try:
            choice = input("\n📋 Select option (1-7): ").strip()
            
            if choice == '1':
                perform_basic_search(collection)
            elif choice == '2':
                perform_cuisine_filtered_search(collection)
            elif choice == '3':
                perform_calorie_filtered_search(collection)
            elif choice == '4':
                perform_combined_filtered_search(collection)
            elif choice == '5':
                run_search_demonstrations(collection)
            elif choice == '6':
                show_advanced_help()
            elif choice == '7':
                print("👋 Exiting Advanced Search System. Goodbye!")
                break
            else:
                print("❌ Invalid option. Please select 1-7.")
                
        except KeyboardInterrupt:
            print("\n\n👋 System interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()