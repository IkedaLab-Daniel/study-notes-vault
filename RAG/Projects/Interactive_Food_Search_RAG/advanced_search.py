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

def perform_basic_search(collection):
    """Perform basic similarity search without filters"""
    print("\n🔍 BASIC SIMILARITY SEARCH")
    print("-" * 30)
    
    query = input("Enter search query: ").strip()
    if not query:
        print("❌ Please enter a search term")
        return
    
    print(f"\n🔍 Searching for '{query}'...")
    results = perform_similarity_search(collection, query, 5)
    
    display_search_results(results, "Basic Search Results")

def perform_cuisine_filtered_search(collection):
    """Perform cuisine-filtered similarity search"""
    print("\n🍽️ CUISINE-FILTERED SEARCH")
    print("-" * 30)
    
    # > Show available cuisines from our dataset
    cuisines = ["Italian", "Thai", "Mexican", "Indian", "Japanese", "French", 
                "Mediterranean", "American", "Health Food", "Dessert"]
    print("Available cuisines:")
    for i, cuisine in enumerate(cuisines, 1):
        print(f"  {i}. {cuisine}")
    
    query = input("\nEnter search query: ").strip()
    cuisine_choice = input("Enter cuisine number (or cuisine name): ").strip()
    
    if not query:
        print("❌ Please enter a search term")
        return
    
    # > Handle cuisine selection - accept both number and text input
    cuisine_filter = None
    if cuisine_choice.isdigit():
        idx = int(cuisine_choice) - 1
        if 0 <= idx < len(cuisines):
            cuisine_filter = cuisines[idx]
    else:
        cuisine_filter = cuisine_choice
    
    if not cuisine_filter:
        print("❌ Invalid cuisine selection")
        return
    
    print(f"\n🔍 Searching for '{query}' in {cuisine_filter} cuisine...")
    results = perform_filtered_similarity_search(
        collection, query, cuisine_filter=cuisine_filter, n_results=5
    )
    
    display_search_results(results, f"Cuisine-Filtered Results ({cuisine_filter})")

def perform_calorie_filtered_search(collection):
    """Perform calorie-filtered similarity search"""
    print("\n🔥 CALORIE-FILTERED SEARCH")
    print("-" * 30)
    
    query = input("Enter search query: ").strip()
    max_calories_input = input("Enter maximum calories (or press Enter for no limit): ").strip()
    
    if not query:
        print("❌ Please enter a search term")
        return
    
    max_calories = None
    if max_calories_input.isdigit():
        max_calories = int(max_calories_input)
    
    print(f"\n🔍 Searching for '{query}'" + 
          (f" with max {max_calories} calories..." if max_calories else "..."))
    
    results = perform_filtered_similarity_search(
        collection, query, max_calories=max_calories, n_results=5
    )
    
    calorie_text = f"under {max_calories} calories" if max_calories else "any calories"
    display_search_results(results, f"Calorie-Filtered Results ({calorie_text})")

if __name__ == "__main__":
    main()