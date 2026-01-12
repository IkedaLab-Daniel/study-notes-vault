"""
Utility functions for the Style Finder application.
"""

def get_all_items_for_image(image_url, dataset):
    """
    Get all items related to a specific image from the dataset.
    
    Args:
        image_url (str): The URL of the matched image
        dataset (DataFrame): Dataset containing outfit information
        
    Returns:
        DataFrame: All items related to the image
    """
    return dataset[dataset['Image URL'] == image_url]

def format_alternatives_response(user_response, alternatives, similarity_score, threshold=0.8):
    """
    Append alternatives to the user response in a formatted way.
    
    Args:
        user_response (str): Original response from the model
        alternatives (dict): Dictionary of alternatives for each item
        similarity_score (float): Similarity score of the match
        threshold (float): Threshold for determining match quality
        
    Returns:
        str: Enhanced response with alternatives
    """
    if similarity_score >= threshold:
        enhanced_response = user_response + "\n\n## Similar Items Found\n\nHere are some similar items we found:\n"
    else:
        enhanced_response = user_response + "\n\n## Similar Items Found\n\nHere are some visually similar items:\n"
    
    for item, alts in alternatives.items():
        enhanced_response += f"\n### {item}:\n"
        if alts:
            for alt in alts:
                enhanced_response += f"- {alt['title']} for {alt['price']} from {alt['source']} (Buy it here: {alt['link']})\n"
        else:
            enhanced_response += "- No alternatives found.\n"
    
    return enhanced_response

def process_response(response: str) -> str:
    """
    Process and escape problematic characters in the response.
    
    Args:
        response (str): The original response text
        
    Returns:
        str: Processed response with escaped characters
    """
    # Escape all $ signs for Markdown
    return response.replace("$", "\\$")
