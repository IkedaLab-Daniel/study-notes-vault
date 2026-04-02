from tabnanny import verbose

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

class MealPlan(BaseModel):
    """Simple meal plan"""
    meal_name: str = Field(description="Name of the meal")
    difficulty_level: str = Field(description="'Easy', 'Medium', 'Hard'")
    servings: int = Field(description="Number of people it serves")
    researched_ingredients: List[str] = Field(description="Ingredients found through research")

class ShoppingCategory(BaseModel):
    """Store section with items"""
    section_name: str = Field(description="Store section (for example, 'Produce', 'Dairy')")
    items: List[GroceryItem] = Field(description="Items in this section")
    estimated_total: str = Field(description="Estimated cost for this section")

class GroceryShoppingPlan(BaseModel):
    """Complete simplified shopping plan"""
    total_budget: str = Field(description="Total planned budget")
    meal_plans: List[MealPlan] = Field(description="Planned meals")
    shopping_sections: List[ShoppingCategory] = Field(description="Organized by store sections")
    shopping_tips: List[str] = Field(description="Money-saving and efficiency tips")

## -- Setting Up our LLM and Essential Tools -- ##

from crewai_tools import SerperDevTool
from crewai import Agent, Task, Crew,  Process, LLM

# Set Watsonx environment variables
os.environ["WATSONX_API_BASE"] = "https://us-south.ml.cloud.ibm.com"
os.environ["WX_PROJECT_ID"] = "skills-network"


# Initialize LLM using Watsonx Granite
llm = LLM(model="watsonx/ibm/granite-3-3-8b-instruct")

## -- Setup SerperDevTool -- ##

SERPER_API = os.getenv('SERPER_API')
os.environ['SERPER_API_KEY'] = SERPER_API


## -- Creating Our AI Agent Workflow with CrewAI -- ##

# > Meal Planner Agent
meal_planner = Agent(
    role="Meal Planner & Recipe Researcher",
    goal="Search for optimal recipes and create detailed meal plans",
    backstory="A skilled meal planner who researches the best recipes online, considering dietary needs, cooking skill levels, and budget constraints.",
    tools=[SerperDevTool()],
    llm=llm,
    verbose=False
)

# > Meal Planning Task
meal_planning_task = Task(
    description=(
        "Search for the best '{meal_name}' recipe for {servings} people within a {budget} budget. "
        "Consider dietary restrictions: {dietary_restrictions} and cooking skill level: {cooking_skill}. "
        "Find recipes that match the skill level and provide complete ingredient lists with quantities."
    ),
    expected_output="A detailed meal plan with researched ingredients, quantities, and cooking instructions appropriate for the skill level.",
    agent=meal_planner,
    output_pydantic=MealPlan,
    output_file="meals.json"
)