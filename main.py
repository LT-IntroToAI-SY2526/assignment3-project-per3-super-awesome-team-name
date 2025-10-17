# THINGS TO ASK THE RECIPE CHAT BOT:
# What should I make for % ? (event)
# What can I make that includes %? (specific ingredient)
# What dish had a serving size of _? (serving size)
# What dish has a cooking time of _ minutes? (Cooking time)
# What dish has _ steps? (cooking complexity/difficulty level)
# What dish can I make for %? (breakfast, lunch, dinner, dessert)
# bye

from recipe import recipe_db
from match import match
from typing import List, Tuple, Callable, Any

# The projection functions, that give us access to certain parts of a "recipe" (a tuple)
def get_name(recipe: Tuple[str, List[str], int, int, int, str, str]) -> str:
    return recipe[0]


def get_ingredients(recipe: Tuple[str, List[str], int, int, int, str, str]) -> List[str]:
    return recipe[1]


def get_size(recipe: Tuple[str, List[str], int, int, int, str, str]) -> int:
    return recipe[2]


def get_time(recipe: Tuple[str, List[str], int, int, int, str, str]) -> int:
    return recipe[3]


def get_steps(recipe: Tuple[str, List[str], int, int, int, str, str]) -> int:
    return recipe[4]


def get_mealType(recipe: Tuple[str, List[str], int, int, int, str, str]) -> str:
    return recipe[5]


def get_event(recipe: Tuple[str, List[str], int, int, int, str, str]) -> str:
    return recipe[6]


#functions based on the questions
def recipe_for_event(matches: List[str]) -> List[str]:
    """Finds all recipe's for a specific event

    Args:
        matches - a list of 1 string, just the event.

    Returns:
        a list of recipe names made for the specific event
    """
    # ["Thanksgiving"]

    result = []
    for recipe in recipe_db:
        if get_event(recipe) == matches[0]:
            result.append(get_name(recipe))
    return result

def ingredient_to_recipe(matches: List[str]) -> List[str]:
    """After getting the input of a specific recipe name
    
    Args:
        matches - a list of 1 string, just the ingredient .
        
    Returns:
            a list of recipes that use that ingredient"""
    result = []
    for recipe in recipe_db:
        if get_ingredients(recipe) == matches[0]:
            result.append(get_name(recipe))
    return result

def serving_size(matches: List[str]) -> List[str]:
    """After getting the input of a specififc serving size return the name of all dishes that match that serving size
    
        Args:
        matches - a list of 1 string, just the serving size . Make sure to convert str -> int
        
    Returns:
            a list of recipes that have that serving size"""
    
    result = []
    size = int(matches[0])

    for recipe in recipe_db:
        if get_size(recipe) == size:
            result.append(get_name(recipe))
    return result

def cook_time(matches: List[str]) -> List[str]:
    """After getting the input of a specififc time (in minutes) return the name of all dishes that match that cook time
    
        Args:
        matches - a list of 1 string, just the cooking time . Make sure to convert str -> int
        
    Returns:
            a list of recipes that have that cookin time"""
    
    result = []
    time = int(matches[0])

    for recipe in recipe_db:
        if get_time(recipe) == time:
            result.append(get_name(recipe))
    return result

def num_steps(matches: List[str]) -> List[str]:
    """After getting the input of a specififc number of steps return the name of all dishes that match that number of steps
    
        Args:
        matches - a list of 1 string, just the number of steps. Make sure to convert str -> int
        
    Returns:
            a list of recipes that have that number of steps"""
    
    result = []
    steps = int(matches[0])

    for recipe in recipe_db:
        if get_steps(recipe) == steps:
            result.append(get_name(recipe))
    return result

def type_of_meal(matches:List[str]) -> List[str]:
    """After getting the input of a specififc type of meal (breakfast, lunch, dinner, dessert) return the name of all dishes that match
    
        Args:
        matches - a list of 1 string, just the type of meal
        
    Returns:
            a list of recipes that are that type of meal"""
    
    result = []

    for recipe in recipe_db:
        if get_mealType(recipe) == matches[0]:
            result.append(get_name(recipe))
    return result