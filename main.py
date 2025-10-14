# THINGS TO ASK THE RECIPE CHAT BOT:
# What should I make for % ? (event)
# How can I make %? (specific recipe name)
# What can I make that includes %? (specific ingredient)
# What dish had a serving size of _? (serving size)
# What dish has a cooking time under/over _? (Cooking time)
# What dish has under/over _ steps? (cooking complexity/difficulty level)
# What dish can I make for %? (breakfast, lunch, dinner)
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
    # ["thanksgiving"]

    result = []
    for recipe in recipe_db:
        if get_event(recipe) == matches[0]:
            result.append(get_name(recipe))
    return result

def title_by_year(matches: List[str]) -> List[str]:
    """Finds all movies made in the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of movie titles made in the passed in year
    """
    # ["1974"]
    year = int(matches[0])
    result = []
    for movie in movie_db:
        if get_year(movie) == year:
            result.append(get_title(movie))
    return result

