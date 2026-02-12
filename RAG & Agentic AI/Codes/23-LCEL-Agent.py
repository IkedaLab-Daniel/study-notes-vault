import numpy as np
import pandas as pd
import matplotlib
import seaborn
import sklearn
import langchain
import langchain_openai

import glob
import os
from typing import List, Optional, Dict, Any
from dotenv import load_dotenv

from langchain_core.tools import tool

load_dotenv()

@tool
def list_csv_files() -> Optional[List[str]]:
    """List all CSV file names in the local directory.

    Returns:
        A list containing CSV file names.
        If no CSV files are found, returns None.
    """
    csv_files = glob.glob(os.path.join(os.getcwd(), "*.csv"))
    if not csv_files:
        return None
    return [os.path.basename(file) for file in csv_files]

print("Tool Name:", list_csv_files.name)
print("Tool Description:", list_csv_files.description)
print("Tool Arguments:", list_csv_files.args)

### -- LLM Setup -- ###
groq_llm = langchain_openai.ChatOpenAI(
     model="llama-3.1-8b-instant",  # Fast, reliable, good for function calling
     api_key=os.getenv('GROQ_API'),  # Get from https://console.groq.com
     base_url="https://api.groq.com/openai/v1"
 )

### -- Dataset caching tool -- ###
DATAFRAME_CACHE = {}

@tool 
def preload_datasets(paths: List[str]) -> str:
    """
    Loads CSV files into a global cache if not already loaded.
    
    This function helps to efficiently manage datasets by loading them once
    and storing them in memory for future use. Without caching, you would
    waste tokens describing dataset contents repeatedly in agent responses.
    
    Args:
        paths: A list of file paths to CSV files.

    Returns:
        A message summarizing which datasets were loaded or already cached.
    """
    loaded = []
    cached = []

    for path in paths:
        if path not in DATAFRAME_CACHE:
            DATAFRAME_CACHE[path] = pd.read_csv(path)
            loaded.append(path)
        else:
            cached.append(path)
    
    return (
        f"Loaded datasets: {loaded}\n"
        f"Already cached: {cached}" 
    )

### -- Summarization tool -- ###
@tool
def get_dataset_summaries(dataset_paths: List[str]) -> List[Dict[str, Any]]:
    """
    Analyze multiple CSV files and return metadata summaries for each.

    Args:
        dataset_paths (List[str]): 
            A list of file paths to CSV datasets.

    Returns:
        List[Dict[str, Any]]: 
            A list of summaries, one per dataset, each containing:
            - "file_name": The path of the dataset file.
            - "column_names": A list of column names in the dataset.
            - "data_types": A dictionary mapping column names to their data types (as strings).
    """
    summaries = []

    for path in dataset_paths:
        # > Load and cache dataset if not already cached
        if path not in DATAFRAME_CACHE:
            DATAFRAME_CACHE[path] = pd.read_csv(path)
        
        df = DATAFRAME_CACHE[path]

        # > Build summary
        summary = {
            "file_name": path,
            "column_names": df.columns.tolist(),
            "data_types": df.dtypes.ast
        }

        summaries.append(summary)
    
    return summaries

### -- DataFrame method execution tool -- ###
@tool
def call_dataframe_method(file_name: str, method: str) -> str:
    """
    Execute a method on a DataFrame and return the result.
    This tool lets you run simple DataFrame methods like 'head', 'tail', or 'describe' 
    on a dataset that has already been loaded and cached using 'preload_datasets'.
    Args:
        file_name (str): The path or name of the dataset in the global cache.
        method (str): The name of the method to call on the DataFrame. Only no-argument 
                        methods are supported (e.g., 'head', 'describe', 'info').
    Returns:
        str: The output of the method as a formatted string, or an error message if 
                the dataset is not found or the method is invalid.
    Example:
        call_dataframe_method(file_name="data.csv", method="head")
    """

    # > Try to get the DataFrame from cache, or load it if not already cache
    if file_name not in DATAFRAME_CACHE:
        try:
           DATAFRAME_CACHE[file_name] = pd.read_csv(file_name)
        except FileNotFoundError:
           return f"DataFrame '{file_name}' not found in cache or on disk"
        except Exception as Ice:
            return f"Error loading '{file_name}' : {str(Ice)}"
        
    df = DATAFRAME_CACHE[file_name]
    func = getattr(df, method, None)
    if not callable(func):
        return f"'{method}' is not a valid method of DataFrame"

    try:
        result = func()
        return str(result)
    except Exception as Ice:
        return f"Error calling '{method}' on '{file_name}': {str(Ice)}"
    
### -- Model evaluation tools -- ###
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

@tool
def evaluate_classfication_dataset(file_name: str, target_column: str) -> Dict[str, float]:
    """
    Train and evaluate a classifier on a dataset using the specified target column.
    Args:
        file_name (str): The name or path of the dataset stored in DATAFRAME_CACHE.
        target_column (str): The name of the column to use as the classification target.
    Returns:
        Dict[str, float]: A dictionary with the model's accuracy score.
    """
    # > Try to get the DataFrame from cache, or load itr if not already caached
    if file_name not in DATAFRAME_CACHE:
        try:
            DATAFRAME_CACHE[file_name] = pd.read_csv(file_name)
        except FileNotFoundError:
            return {"error": f"DataFrame '{file_name}' not found in cache or on disk"}
        except Exception as ICE:
            return {"error": f"Error loading '{file_name}': {str(ICE)}"}
        
        df = DATAFRAME_CACHE[file_name]
        if target_column not in df.columns:
            return {"error": f"Target column '{target_column}' not found in '{file_name}'"}
        
        X = df.drop(columns=[target_column])
        Y = df[target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        return {"accuracy": acc}