"""
Main application file for the Style Finder Gradio interface.
"""

import gradio as gr
import pandas as pd
import os
from tempfile import NamedTemporaryFile

# Import local modules
from models.image_processor import ImageProcessor
from models.llm_service import LlamaVisionService
from services.search_service import SearchService
from utils.helpers import get_all_items_for_image, format_alternatives_response, process_response
import config

class StyleFinderApp:
    """
    Main application class that orchestrates the Style Finder workflow.
    """
    
    def __init__(self, dataset_path, serp_api_key=None):
        """
        Initialize the Style Finder application.
        
        Args:
            dataset_path (str): Path to the dataset file
            serp_api_key (str, optional): SerpAPI key for product searches
            
        Raises:
            FileNotFoundError: If the dataset file is not found
            ValueError: If the dataset is empty or invalid
        """
        # Load the dataset
        if not os.path.exists(dataset_path):
            raise FileNotFoundError(f"Dataset file not found: {dataset_path}")
            
        self.data = pd.read_pickle(dataset_path)
        if self.data.empty:
            raise ValueError("The loaded dataset is empty")
        
        # Initialize components
        self.image_processor = ImageProcessor(
            image_size=config.IMAGE_SIZE,
            norm_mean=config.NORMALIZATION_MEAN,
            norm_std=config.NORMALIZATION_STD
        )
        
        self.llm_service = LlamaVisionService(
            model_id=config.LLAMA_MODEL_ID,
            project_id=config.PROJECT_ID,
            region=config.REGION
        )
        
        self.search_service = SearchService(api_key=serp_api_key) if serp_api_key else None
    
    def process_image(self, image, alternatives_count=5, include_alternatives=True):
        """
        Process a user-uploaded image and generate a comprehensive response.
        
        Args:
            image: PIL image uploaded through Gradio
            alternatives_count (int): Number of alternatives to show
            include_alternatives (bool): Whether to include shopping alternatives
            
        Returns:
            str: Formatted response with fashion analysis and alternatives
        """
        # Save the image temporarily if it's not already a file path
        if not isinstance(image, str):
            temp_file = NamedTemporaryFile(delete=False, suffix=".jpg")
            image_path = temp_file.name
            image.save(image_path)
        else:
            image_path = image
        
        # Step 1: Encode the image
        user_encoding = self.image_processor.encode_image(image_path, is_url=False)
        if user_encoding['vector'] is None:
            return "Error: Unable to process the image. Please try another image."
        
        # Step 2: Find the closest match
        closest_row, similarity_score = self.image_processor.find_closest_match(user_encoding['vector'], self.data)
        if closest_row is None:
            return "Error: Unable to find a match. Please try another image."
        
        print(f"Closest match: {closest_row['Item Name']} with similarity score {similarity_score:.2f}")
        
        # Step 3: Get all related items
        all_items = get_all_items_for_image(closest_row['Image URL'], self.data)
        if all_items.empty:
            return "Error: No items found for the matched image."
        
        # Step 4: Generate fashion response
        bot_response = self.llm_service.generate_fashion_response(
            user_image_base64=user_encoding['base64'],
            matched_row=closest_row,
            all_items=all_items,
            similarity_score=similarity_score,
            threshold=config.SIMILARITY_THRESHOLD
        )
        
        # Clean up temporary file
        if not isinstance(image, str):
            try:
                os.unlink(image_path)
            except:
                pass
        
        # Step 5: If search service is available and alternatives are requested
        if self.search_service and include_alternatives:
            # Extract item descriptions
            item_descriptions = self.search_service.extract_item_descriptions(bot_response)
            
            # Search for alternatives
            alternatives = self.search_service.search_alternatives(
                item_descriptions, 
                top_n=alternatives_count
            )
            
            # Format the final response
            final_response = format_alternatives_response(
                bot_response,
                alternatives,
                similarity_score,
                config.SIMILARITY_THRESHOLD
            )
            
            return final_response
        
        return bot_response

def create_gradio_interface(app):
    """
    Create and configure the Gradio interface.
    
    Args:
        app (StyleFinderApp): Instance of the StyleFinderApp
        
    Returns:
        gr.Blocks: Configured Gradio interface
    """
    with gr.Blocks(theme=gr.themes.Soft(), title="Fashion Style Analyzer") as demo:
        gr.Markdown(
            """
            # Fashion Style Analyzer
            
            Upload an image or click on an example to analyze fashion elements and find similar items.
            This tool uses AI to analyze and describe fashion elements in images.
            """
        )
        
        with gr.Row():
            with gr.Column(scale=1):
                # Image input section
                image_input = gr.Image(type="pil", label="Upload Fashion Image")
                
                # Example images section
                gr.Markdown("### Example Images")
                with gr.Row():
                    example1 = gr.Image(
                        value="examples/casual_outfit.jpg",
                        label="Casual Outfit",
                        show_label=True,
                        elem_id="example1"
                    )
                    example2 = gr.Image(
                        value="examples/formal_dress.jpg",
                        label="Formal Dress",
                        show_label=True,
                        elem_id="example2"
                    )
                    example3 = gr.Image(
                        value="examples/streetwear.jpg",
                        label="Streetwear",
                        show_label=True,
                        elem_id="example3"
                    )
                
                # Options section
                with gr.Row():
                    include_alternatives = gr.Checkbox(
                        label="Include Shopping Alternatives", 
                        value=True,
                        info="Enable to search for similar items online"
                    )
                    
                    alt_count = gr.Slider(
                        minimum=1, 
                        maximum=10, 
                        value=5, 
                        step=1, 
                        label="Number of Alternatives",
                        visible=True
                    )
                
                submit_btn = gr.Button("Analyze Style", variant="primary")
            
            with gr.Column(scale=2):
                output = gr.Markdown(label="Style Analysis Results")
        
        # Update visibility of alt_count based on include_alternatives
        include_alternatives.change(
            fn=lambda x: gr.update(visible=x),
            inputs=[include_alternatives],
            outputs=[alt_count]
        )
        
        # Connect example images to the image input
        example1.click(
            fn=lambda x: x,
            inputs=[example1],
            outputs=[image_input]
        )
        example2.click(
            fn=lambda x: x,
            inputs=[example2],
            outputs=[image_input]
        )
        example3.click(
            fn=lambda x: x,
            inputs=[example3],
            outputs=[image_input]
        )
        
        # Connect the button to the process_image function
        submit_btn.click(
            fn=app.process_image,
            inputs=[image_input, alt_count, include_alternatives],
            outputs=output
        )
        
        gr.Markdown(
            """
            ### About This Tool
            
            This application uses advanced AI to analyze fashion elements in images:
            
            - **Image Analysis**: Converts images into numerical vectors for comparison
            - **Similarity Matching**: Finds the closest match in a database of fashion items
            - **AI Analysis**: Uses vision AI to analyze and describe fashion elements
            - **Shopping Integration**: Searches for similar items across the web
            """
        )
    
    return demo

if __name__ == "__main__":
    try:
        # Initialize the app with the dataset
        app = StyleFinderApp("swift-style-embeddings.pkl")
        
        # Create the Gradio interface
        demo = create_gradio_interface(app)
        
        # Launch the Gradio interface
        demo.launch(
            server_name="127.0.0.1",  
            server_port=5000,
            share=True  # Set to False if you don't want to create a public link
        )
    except Exception as e:
        print(f"Error starting the application: {str(e)}")