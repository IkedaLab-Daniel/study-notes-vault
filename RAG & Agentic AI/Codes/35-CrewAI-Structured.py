from leftover import LeftoversCrew

from dotenv import load_dotenv
load_dotenv()
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

llm = LLM(
    #model="groq/llama-3.1-8b-instant",
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API"),
    max_tokens=1000
)

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

## -- Creating and Running Our Meal Planning Crew -- ##

meal_planner_crew = Crew(
    agents=[meal_planner],
    tasks=[meal_planning_task],
    process=Process.sequential,
    verbose=True
)

# meal_planner_result = meal_planner_crew.kickoff(
#     inputs={
#         "meal_name": "Chicken Stir Fry",
#         "servings": 4,
#         "budget": "$25",                           
#         "dietary_restrictions": ["no nuts"],       
#         "cooking_skill": "beginner"          
#     }
# )

# print("✅ Single meal planning completed!")
# print("📋 Single Meal Results:")
# print(meal_planner_result)

## -- Creating Our Shopping Organization Agent -- ##

shopping_organizer = Agent(
    role="Shopping Organizer",
    goal="Organize grocery lists by store sections efficiently",
    backstory="An experienced shopper who knows how to organize lists for quick store trips and considers dietary restrictions.",
    tools=[],
    llm=llm,
    verbose=False
)

shopping_task = Task(
    description=(
        "Organize the ingredients from the '{meal_name}' meal plan into a grocery shopping list. "
        "Group items by store sections and estimate quantities for {servings} people. "
        "Consider dietary restrictions: {dietary_restrictions} and cooking skill: {cooking_skill}. "
        "Stay within budget: {budget}."
    ),
    expected_output="An organized shopping list grouped by store sections with quantities and prices.",
    agent=shopping_organizer,
    context=[meal_planning_task],
    output_pydantic=GroceryShoppingPlan,
    output_file="shopping_list.json"
)

## -- Building Our Two-Agent Grocery Crew -- ##

two_agent_grocery_crew = Crew(
    agents=[meal_planner, shopping_organizer],
    tasks=[meal_planning_task, shopping_task],
    process=Process.sequential,
    verbose=True
)

# Run the crew
shopping_result = two_agent_grocery_crew.kickoff(
    inputs={
        "meal_name": "Chicken Stir Fry",
        "servings": 4,
        "budget": "$25",                           
        "dietary_restrictions": ["no nuts"],      
        "cooking_skill": "beginner"             
    }
)

# ANSI colors
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"

def print_shopping_results(data):
    print(f"{BOLD}{CYAN}📋 Shopping Results{RESET}")
    print(f"{YELLOW}Budget:{RESET} {data.total_budget}\n")

    # Meal Plans
    print(f"{BOLD}{MAGENTA}🍽 Meal Plans{RESET}")
    for meal in data.meal_plans:
        print(f"  {GREEN}- {meal.meal_name}{RESET}")
        print(f"    Difficulty: {meal.difficulty_level}")
        print(f"    Servings: {meal.servings}")
        print(f"    Ingredients:")
        for ing in meal.researched_ingredients:
            print(f"      • {ing}")
        print()

    # Shopping Sections
    print(f"{BOLD}{MAGENTA}🛒 Shopping List{RESET}")
    for section in data.shopping_sections:
        print(f"\n  {CYAN}{section.section_name}{RESET} ({section.estimated_total})")
        for item in section.items:
            print(f"    {GREEN}- {item.name}{RESET}")
            print(f"      Qty: {item.quantity}")
            print(f"      Price: {item.estimated_price}")

    # Tips
    print(f"\n{BOLD}{MAGENTA}💡 Tips{RESET}")
    for tip in data.shopping_tips:
        print(f"  {YELLOW}- {tip}{RESET}")

def extract_shopping_plan(result) -> GroceryShoppingPlan:
    # CrewAI kickoff returns a CrewOutput wrapper; prefer the structured Pydantic payload.
    if isinstance(result, GroceryShoppingPlan):
        return result

    pydantic_result = getattr(result, "pydantic", None)
    if isinstance(pydantic_result, GroceryShoppingPlan):
        return pydantic_result

    task_outputs = getattr(result, "tasks_output", None) or []
    for task_output in reversed(task_outputs):
        task_pydantic = getattr(task_output, "pydantic", None)
        if isinstance(task_pydantic, GroceryShoppingPlan):
            return task_pydantic

    raise TypeError(
        "Crew output does not contain GroceryShoppingPlan in `.pydantic` or `tasks_output`."
    )


shopping_plan = extract_shopping_plan(shopping_result)
print_shopping_results(shopping_plan)

## -- Adding Financial Intelligence with Budget Advisor Agent -- ##

budget_advisor = Agent(
    role="Budget Advisor",
    goal="Provide cost estimates and money-saving tips",
    backstory="A budget-conscious shopper who helps families save money on groceries while respecting dietary needs.",
    tools=[SerperDevTool()],
    llm=llm,
    verbose=False
)

budget_task = Task(
    description=(
        "Analyze the shopping plan for '{meal_name}' serving {servings} people. "
        "Ensure total cost stays within {budget}. Consider dietary restrictions: {dietary_restrictions}. "
        "Provide practical money-saving tips and alternative ingredients if needed to meet budget."
    ),
    expected_output="A complete shopping guide with detailed prices, budget analysis, and money-saving tips.",
    agent=budget_advisor,
    context=[meal_planning_task, shopping_task],
    output_file="shopping_guide.md"
)

## -- Using CrewBase and Decorators with CrewAI -- ##

from leftover import LeftoversCrew

leftovers_cb = LeftoversCrew(llm=llm)
yaml_leftover_manager = leftovers_cb.leftover_manager()
yaml_leftover_task    = leftovers_cb.leftover_task()
