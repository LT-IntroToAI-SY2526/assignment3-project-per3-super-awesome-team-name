# THINGS TO ASK THE RECIPE CHAT BOT:
# What should I make for % ? (event)
# What can I make that includes %? (specific ingredient)
# What dish had a serving size of _? (serving size)
# What dish has a cooking time under/over _? (Cooking time)
# What dish has under/over _ steps? (cooking complexity/difficulty level)
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

