import sagemaker
from sagemaker.predictor import retrieve_default
import json 
import boto3

# --- IMPORTANT --- 
# Replace this with the actual name of the deployed DeepSeek endpoint
endpoint_name = "jumpstart-dft-deepseek-llm-r1-disti-20251025-160934" 
# ----------------- 

predictor = None # Initialize predictor
try:
    print(f"Connecting to endpoint: {endpoint_name}...")
    # Use retrieve_default which automatically handles serializers/deserializers for known JumpStart containers
    predictor = retrieve_default(endpoint_name)
    print(f"Successfully connected to endpoint: {endpoint_name}")
except Exception as e:
    print(f"[Error] connecting to endpoint {endpoint_name}: {e}")
    print("Please ensure the endpoint name is correct and the endpoint is in 'InService' status.")
    # Optionally raise the error or handle it as needed
    # raise e 
