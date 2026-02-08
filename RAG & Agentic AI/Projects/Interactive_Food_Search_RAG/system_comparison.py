from shared_functions import *
import time

def main():
    """Compare all three search systems with the same query"""
    print("🔬 FOOD SEARCH SYSTEMS COMPARISON")
    print("=" * 50)
    
    # Load data once for all systems
    food_items = load_food_data('./FoodDataSet.json')
    
    # Create collections for each system
    interactive_collection = create_similarity_search_collection("comparison_interactive")
    advanced_collection = create_similarity_search_collection("comparison_advanced")
    rag_collection = create_similarity_search_collection("comparison_rag")
    
    # Populate all collections
    populate_similarity_collection(interactive_collection, food_items)
    populate_similarity_collection(advanced_collection, food_items)
    populate_similarity_collection(rag_collection, food_items)
    
    # Test query
    test_query = "chocolate dessert"
    
    print(f"\n🔍 Testing query: '{test_query}'")
    print("=" * 50)
    
    # System 1: Interactive Search Style
    print("\n1️⃣ INTERACTIVE SEARCH APPROACH:")
    print("-" * 30)
    start_time = time.time()
    interactive_results = perform_similarity_search(interactive_collection, test_query, 3)
    interactive_time = time.time() - start_time
    
    for i, result in enumerate(interactive_results, 1):
        print(f"{i}. {result['food_name']} ({result['similarity_score']*100:.1f}% match)")
        print(f"   {result['food_description']}")
    print(f"⏱️ Response time: {interactive_time:.3f} seconds")
    
    # System 2: Advanced Search Style
    print("\n2️⃣ ADVANCED SEARCH APPROACH:")
    print("-" * 30)
    start_time = time.time()
    
    # Show basic search
    basic_results = perform_similarity_search(advanced_collection, test_query, 3)
    print("📋 Basic results:")
    for i, result in enumerate(basic_results, 1):
        print(f"   {i}. {result['food_name']} - {result['cuisine_type']} ({result['food_calories_per_serving']} cal)")
    
    # Show filtered search
    spicy_results = perform_filtered_similarity_search(
        advanced_collection, test_query, cuisine_filter="Indian", n_results=2
    )
    print("🌶️ Filtered for Indian cuisine:")
    for i, result in enumerate(spicy_results, 1):
        print(f"   {i}. {result['food_name']} ({result['similarity_score']*100:.1f}% match)")
    
    advanced_time = time.time() - start_time
    print(f"⏱️ Response time: {advanced_time:.3f} seconds")
    
    # System 3: RAG Chatbot Style
    print("\n3️⃣ RAG CHATBOT APPROACH:")
    print("-" * 30)
    start_time = time.time()
    
    rag_results = perform_similarity_search(rag_collection, test_query, 3)
    
    # Generate RAG-style response
    rag_response = f"Perfect! I found some excellent chocolate dessert options for you. "
    rag_response += f"I'd highly recommend the {rag_results[0]['food_name']} - it's a {rag_results[0]['similarity_score']*100:.0f}% match "
    rag_response += f"and offers that sweet, rich flavor you're craving. "
    if rag_results[0]['cuisine_type'] == 'American':
        rag_response += "American desserts are perfect for chocolate lovers! "
    rag_response += f"At {rag_results[0]['food_calories_per_serving']} calories, it's a delightful treat. "
    rag_response += f"You might also enjoy {rag_results[1]['food_name']} as an alternative."
    
    print(f"🤖 Bot: {rag_response}")
    
    rag_time = time.time() - start_time
    print(f"⏱️ Response time: {rag_time:.3f} seconds")
    
    # Comparison Summary
    print("\n📊 SYSTEM COMPARISON SUMMARY:")
    print("=" * 50)
    print("Interactive Search:")
    print("  ✅ Fast and simple")
    print("  ✅ Direct results display")
    print("  ❌ Limited context")
    
    print("\nAdvanced Search:")
    print("  ✅ Powerful filtering options")
    print("  ✅ Multiple search modes")
    print("  ✅ Precise control")
    print("  ❌ Requires user to know filter options")
    
    print("\nRAG Chatbot:")
    print("  ✅ Natural language interaction")
    print("  ✅ Contextual explanations")
    print("  ✅ Conversational experience")
    print("  ❌ More complex implementation")
    
    print(f"\n⏱️ Performance Comparison:")
    print(f"  Interactive: {interactive_time:.3f}s")
    print(f"  Advanced: {advanced_time:.3f}s")
    print(f"  RAG Chatbot: {rag_time:.3f}s")

if __name__ == "__main__":
    main()