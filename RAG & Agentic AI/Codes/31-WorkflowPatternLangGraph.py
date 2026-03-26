from langgraph.graph import StateGraph, END, START
from langgraph.types import Send

from typing import TypedDict, Annotated, List, Literal
from pydantic import BaseModel, Field, field_validator
import operator
from pprint import pprint

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os

## --- Init LLM -- ##

load_dotenv()
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    # model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API")
)

## --- Dish Schemas -- ##
# for a single dish
class Dish(BaseModel):
    name: str = Field(
        description="Name of the dish (for example, Spaghetti Bolognese, Chicken Curry)."
    )
    ingredients: List[str] = Field(
        description="List of ingredients needed for this dish as an array of strings."
    )
    location: str = Field(
        description="The cuisine or cultural origin of the dish (for example, Italian, Indian, Mexican)."
    )

    @field_validator("ingredients", mode="before")
    @classmethod
    def normalize_ingredients(cls, value):
        # Accept comma-separated ingredient strings and convert them to a list.
        if isinstance(value, str):
            return [item.strip() for item in value.split(",") if item.strip()]
        return value

# for a list of Dish objects
class Dishes(BaseModel):
    sections: List[Dish] = Field(
        description="A list of grocery sections, one for each dish, with ingredients."
    )

# construct a prompt template
dish_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an assistant that generates a structured grocery list.\n\n"
        "The user wants to prepare the following meals: {meals}\n\n"
        "For each meal, return a section with:\n"
        "- the name of the dish\n"
        "- a JSON array of ingredient strings needed for that dish (not a comma-separated string).\n"
        "- the cuisine or cultural origin of the food"
    )
])

# planner
planner_pipe = dish_prompt | llm.with_structured_output(Dishes)

# invoke the planner_pile with example meals
result = planner_pipe.invoke({"meals": ["banana smoothie", "carrot cake"]})
print(result)

## -- State -- ##
class State(TypedDict):
    meals: str # user input
    sections: List[Dish] # One section per meal/dish with ingredients
    completed_menu: Annotated[List[str], operator.add] # wworker written dish guide chinks
    final_meal_guide: str # fully compiled, readable menu

## -- Test -- ##
dummy_state: State = {
    "meals": "Spaghetti Bolognese and Chicken Stir Fry",
    "sections": [],
    "completed_menu": [],
    "final_meal_guide": ""
}

report_sections = planner_pipe.invoke({"meals": dummy_state["meals"]})

for i, section in enumerate(report_sections.sections):
    print(f"Dish {i+1}\n")
    # add each dish to our dummy state
    dummy_state["sections"].append(section)
    print(f"Item Name: {section.name}")
    print(f"Location/Cuisine: {section.location}")
    print(f"Ingredients: {', '.join(section.ingredients)}.")