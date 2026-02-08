"""
Service for interacting with the Llama 3.2 Vision Instruct model.
"""

from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters

class LlamaVisionService:
    """
    Provides methods to interact with the Llama 3.2 Vision Instruct model.
    """
    
    def __init__(self, model_id, project_id, region="us-south", 
                 temperature=0.2, top_p=0.6, api_key=None):
        """
        Initialize the service with the specified model and parameters.
        
        Args:
            model_id (str): Unique identifier for the model
            project_id (str): Project ID to associate the task
            region (str): Region for the watsonx AI service
            temperature (float): Controls randomness in generation
            top_p (float): Nucleus sampling parameter
            api_key (str, optional): API key for authentication
        """
        # Set up authentication credentials
        credentials = Credentials(
            url=f"https://{region}.ml.cloud.ibm.com",
            api_key=api_key
        )
        self.client = APIClient(credentials)
        
        # Define parameters for the model's behavior
        params = TextChatParameters(
            temperature=temperature,
            top_p=top_p
        )
        
        # Initialize the model inference object
        self.model = ModelInference(
            model_id=model_id,
            credentials=credentials,
            project_id=project_id,
            params=params
        )
    
    def generate_response(self, encoded_image, prompt):
        """
        Generate a response from the model based on an image and prompt.
        
        Args:
            encoded_image (str): Base64-encoded image string
            prompt (str): Text prompt to guide the model's response
            
        Returns:
            str: Model's response
        """
        try:
            # Create the messages object
            messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": "data:image/jpeg;base64," + encoded_image,
                            }
                        }
                    ]
                }
            ]
            
            # Send the request to the model
            response = self.model.chat(messages=messages)
            
            # Return the model's response
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error generating response: {e}"
    
    def generate_fashion_response(self, user_image_base64, matched_row, all_items, 
                                 similarity_score, threshold=0.8):
        """
        Generate a fashion-specific response using role-based prompts.
        
        Args:
            user_image_base64: Base64-encoded user-uploaded image
            matched_row: The closest match row from the dataset
            all_items: DataFrame with all items related to the matched image
            similarity_score: Similarity score between user and matched images
            threshold: Minimum similarity for considering an exact match
            
        Returns:
            str: Detailed fashion response
        """
        # Generate a detailed list of items with prices and links
        items_description = "\n".join(
            f"- **{row['Item Name']}** (${row['Price']}): Buy it here: {row['Link']}"
            for _, row in all_items.iterrows()
        )

        if similarity_score >= threshold:
            # Role-based prompt for an exact match
            assistant_prompt = (
                f"You are a young and enthusiastic fashion expert who helps students learn about fashion analysis. "
                f"The matched outfit features: {matched_row['Item Name']}.\n\n"
                f"Matched outfit includes:\n{items_description}\n\n"
                "Follow these steps in your response:\n"
                "1. Introduce yourself briefly. Use an educational, engaging tone suited for students.\n"
                "2. Describe each item as a definition first (list what it is, what color it is and what pattern it has), following this format:\n"
                "   - Example: Versace 'Tweed Masculine Blazer' is a single-breasted wool-blend tweed blazer crafted in a micro windowpane pattern in red and black.\n"
                "   - Format: **Item Name** is [definition].\n"
                "3. After defining each item, include its detailed description, highlighting its type, material, pattern, and why it stands out.\n"
                "4. Describe the outfit's overall style category and explain why (e.g., casual chic, formal elegance, street style).\n"
                "5. Include a brief learning point about fashion analysis concepts used in this assessment.\n"
                "6. Summarize all the items with their prices and links at the end.\n\n"
                "Ensure your response is educational, clear, and structured for students to learn from!"
            )
        else:
            # Role-based prompt for the closest match
            assistant_prompt = (
                f"You are a fashion instructor helping students learn image analysis techniques.\n\n"
                "Follow these steps in your response:\n"
                "1. Use an educational tone suited for a course on fashion technology.\n"
                "2. Explain that while we don't have this exact outfit in our database, this is a learning opportunity about image analysis.\n"
                "3. Describe each item as a definition first (list what it is, what color it is and what pattern it has), following this format: \n"
                "   - Example: Blazer is a single-breasted wool-blend tweed blazer in red and black with a micro windowpane pattern.\n"
                "   - Format: **Item Name** is [definition].\n"
                "4. Be thorough and include details about the type of item, its color, and any patterns or textures.\n"
                "5. Include a short lesson on how AI models analyze fashion elements in images.\n"
                "6. Conclude by saying: 'Next, we'll search for similar items online to demonstrate how to recreate this look.'\n\n"
                "Make your response educational and structured for a classroom setting!"
            )

        # Send the prompt to the model
        return self.generate_response(user_image_base64, assistant_prompt)