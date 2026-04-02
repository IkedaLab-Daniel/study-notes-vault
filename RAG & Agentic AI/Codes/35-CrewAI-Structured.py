from leftover import LeftoversCrew

from dotenv import load_dotenv
import os

from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

## -- Creating the Grocery Shopping Assistant Structure -- ##

class GroceryItem(BaseModel):
    """Individual grocery item"""
    name: str = Field(description="Name of the grocery item")
    quantity: str = Field(description="Quantity needed (for example, '2 lbs', '1 gallon')")
    estimated_price: str = Field(description="Estimated price (for example, '$3-5')")
    category: str = Field(description="Store section (for example, 'Produce', 'Dairy')")