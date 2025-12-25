from shared_functions import *
from typing import List, Dict, Any
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watsonx_ai.foundation_models import ModelInference
import json
from dotenv import load_dotenv
import os
from utils import print_agent

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
        enchanced_rag_food_chatbot(collection)

    except Exception as Ice:
        print("Error", Ice)

def prepare_context_for_llm(query: str, search_results: List[Dict]) -> str:
    """Prepare structured context from search results for LLM"""
    if not search_results:
        return "No relevant food items found in the database."

    context_parts = []
    context_parts.append("Based on your query, here are the mnost relevant food options from out database:")
    context_parts.append("")

    for i, result in enumerate(search_results[:3], 1):
        food_context = []
        food_context.append(f"Option {i}: {result['food_name']}")
        food_context.append(f"  - Description: {result['food_description']}")
        food_context.append(f"  - Cuisine: {result['cuisine_type']}")
        food_context.append(f"  - Calories: {result['food_calories_per_serving']} per serving")

        if result.get('food_health_benefits'):
            ingredients = result['food_ingredients']
            if isinstance(ingredients, list):
                food_context.append(f"  - Key ingredients: {', '.join(ingredients[:5])}")
            else:
                food_context.append(f"  - Key ingredients: {ingredients}")

        if result.get('food_health_benefits'):
            food_context.append(f"  - Health benefits: {result['food_health_benefits']}")
        
        if result.get('cooking_method'):
            food_context.append(f"  - Cooking method: {result['cooking_method']}")
        
        if result.get('taste_profile'):
            food_context.append(f"  - Taste profile: {result['taste_profile']}")
        
        food_context.append(f"  - Similarity score: {result['similarity_score']*100:.1f}%")
        food_context.append("")

        context_parts.extend(food_context)
    
    return "\n".join(context_parts)

def generate_llm_rag_response(query: str, search_results: List[Dict]) -> str:
    """Generate response using IBM Granite with retrieved context"""
    try:
        # > Prepare context from search result
        context = prepare_context_for_llm(query, search_results)

        # > Build the prompt for the LLM
        prompt = f'''You are a helpful food recommendation assistant. A user is asking for food recommendations, and I've retrieved relevant options from a food database.
User Query: "{query}"
Retrieved Food Information:
{context}
Please provide a helpful, short response that:
1. Acknowledges the user's request
2. Recommends 2-3 specific food items from the retrieved options
3. Explains why these recommendations match their request
4. Includes relevant details like cuisine type, calories, or health benefits
5. Uses a friendly, conversational tone
6. Keeps the response concise but informative
Response:'''
        
        # > Generate respoonse using IBM Granite
        generated_response = model.generate(prompt=prompt, params=None)

        # > Extract the generated text
        if generated_response and "results" in generated_response:
            response_text = generated_response["results"][0]["generated_text"]

            # > Clean up the response if needed
            response_text = response_text.strip()

            # > If response is too short, provide a fallback
            if len(response_text) < 50:
                return generate_fallback_response(query, search_results)
            
            return response_text

    except Exception as Ice:
        print("Error generating LLM response:", Ice)
        return generate_fallback_response(query, search_results)

def generate_fallback_response(query: str, search_results: List[Dict]) -> str:
    """Generate fallback response when LLM fails"""
    if not search_results:
        return "I couldn't find any food items matching your request. Try describing what you're in the mood for with different words!"
    
    top_result = search_results[0]
    response_parts = []

    response_parts.append(f"Based on your request for '{query}', I'd recommend {top_result['food_name']}.")
    response_parts.append(f"It's a {top_result['cuisine_type']} dish with {top_result['food_calories_per_serving']} calories per serving.")
    
    if len(search_results) > 1:
        second_choice = search_results[1]
        response_parts.append(f"Another great option would be {second_choice['food_name']}.")
    
    return " ".join(response_parts)

def enchanced_rag_food_chatbot(collection):
    """Enhanced RAG-powered conversational food chatbot with IBM Granite"""

    # Clear the terminal for a clean start
    os.system('cls' if os.name == 'nt' else 'clear')

    # Show agent header (if available)
    try:
        print_agent()
    except Exception:
        pass
    print("\n" + "="*70)
    print("🤖 ENHANCED RAG FOOD RECOMMENDATION CHATBOT")
    print("   Powered by IBM's Granite Model")
    print("="*70)
    print("💬 Ask me about food recommendations using natural language!")
    print("\nExample queries:")
    print("  • 'I want something spicy and healthy for dinner'")
    print("  • 'What Italian dishes do you recommend under 400 calories?'")
    print("  • 'I'm craving comfort food for a cold evening'")
    print("  • 'Suggest some protein-rich breakfast options'")
    print("\nCommands:")
    print("  • 'help' - Show detailed help menu")
    print("  • 'compare' - Compare recommendations for two different queries")
    print("  • 'quit' - Exit the chatbot")
    print("-" * 70)

    conversation_history = []

    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            
            if not user_input:
                print_agent()
                print(" >> Please tell me what kind of food you're looking for!")
                continue

            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n\n")
                print_agent()
                print(" >> Thank you for using the Enhanced RAG Food Chatbot!")
                print(" >> Hope you found some delicious recommendations! 👋")
                break

            elif user_input.lower() in ['help', 'h']:
                show_enhanced_rag_help()

            else:
                # > Process the food query with enchanced RAG
                handle_enhanced_rag_query(collection, user_input, conversation_history)
                conversation_history.append(user_input)

                # > Keep conversation history Manageable
                if len(conversation_history) > 5:
                    conversation_history = conversation_history[-3:]

        except KeyboardInterrupt:
            print_agent
            print(" >> Goodbye! Hope you find something delicious! 👋")
            break

        except Exception as Ice:
            print_agent()
            print(" >> Error:", Ice)

if __name__ == "__main__":
    main()
    print(" --- End --- ")