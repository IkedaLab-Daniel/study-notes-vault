"""
Service for searching online products using SerpAPI.
"""

import re
from serpapi import GoogleSearch

class SearchService:
    """
    Handles online product searches using SerpAPI.
    """
    
    def __init__(self, api_key):
        """
        Initialize the search service with the SerpAPI key.
        
        Args:
            api_key (str): SerpAPI key for authentication
        """
        self.api_key = api_key
    
    def extract_item_descriptions(self, bot_response):
        """
        Extract item descriptions from the bot's response.
        
        Args:
            bot_response (str): The response from the model
            
        Returns:
            list: Dictionaries containing item names and detailed descriptions
        """
        pattern = re.compile(
            r"\*\*(?P<item_name>.*?)\*\*\s+(is|are)\s+(?P<description>.*?\.)(?=\s*\n|\*\*|$)",
            re.DOTALL
        )

        descriptions = []
        for match in pattern.finditer(bot_response):
            item_name = match.group("item_name").strip()
            description = match.group("description").strip()
            
            descriptions.append({
                "item_name": item_name,
                "description": description
            })
        
        return descriptions
    
    def search_alternatives(self, descriptions, top_n=5):
        """
        Search for alternatives using Google Shopping via SerpAPI.
        
        Args:
            descriptions (list): Item descriptions extracted from the bot's response
            top_n (int): Number of top alternatives to return for each item
            
        Returns:
            dict: Item names mapped to lists of alternatives
        """
        alternatives = {}
        
        print("\n Starting SerpAPI search for alternatives...\n")
        
        for desc in descriptions:
            item_name = desc["item_name"]
            query = f"Search for affordable alternatives of: {desc['description']}"
            
            params = {
                "engine": "google_shopping",
                "q": query,
                "api_key": self.api_key,
            }
            
            try:
                search = GoogleSearch(params)
                search_results = search.get_dict()
                
                shopping_items = self._extract_shopping_results(search_results)
                if shopping_items:
                    print(f"Alternatives found for {item_name}.")
                else:
                    print(f"No shopping results found for {item_name} alternative.")
                
                alternatives[item_name] = shopping_items[:top_n]
            except Exception as e:
                print(f"Error querying SerpAPI for {item_name}: {e}")
                alternatives[item_name] = []
        
        return alternatives
    
    def _extract_shopping_results(self, json_response):
        """
        Extract relevant shopping results from a JSON response.
        
        Args:
            json_response (dict): The JSON response from SerpAPI
            
        Returns:
            list: Dictionaries containing product details
        """
        shopping_results = json_response.get("shopping_results", [])
        extracted_results = []
        
        for item in shopping_results:
            title = item.get("title", "No title available").strip()
            price = item.get("price", "No price available").strip()
            link = item.get("product_link", "No link available").strip()
            source = item.get("source", "Unknown source").strip()
            
            extracted_results.append({
                "title": title,
                "price": price,
                "link": link,
                "source": source
            })
        
        return extracted_results