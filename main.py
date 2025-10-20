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
        for i in get_ingredients(recipe):
            if i == matches[0]:
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

# dummy argument is ignored and doesn't matter
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt


# The pattern-action list for the natural language query system A list of tuples of
# pattern and action It must be declared here, after all of the function definitions
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("What should I make for % "), recipe_for_event),
    (str.split("What can I make that includes %"), ingredient_to_recipe),
    (str.split("What dish had a serving size of _"), serving_size),
    (str.split("What dish has a cooking time of _ minutes"), cook_time),

    (str.split("What dish has _ steps"), num_steps),
    (str.split("What dish can I make for %"), type_of_meal),

    (["bye"], bye_action),
]
# What dish has a cooking time of _ minutes? (Cooking time)
# What dish has _ steps? (cooking complexity/difficulty level)
# What dish can I make for %? (breakfast, lunch, dinner, dessert)

def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pat, act in pa_list:
        mat = match(pat, src)

        if mat is not None:
            answer = act(mat)
            return answer if answer else ["No answers"]
        
    return ["I don't understand"]

def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the movie database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break
    print("\nSo Long!\n")


#asserts
if __name__ == "__main__":
    assert isinstance(recipe_for_event(["Thanksgiving"]), list), "recipe_for_event not returning recipe"
    assert sorted(recipe_for_event(["Thanksgiving"])) == sorted(
        ["Holiday Lemon-Herb Chicken Thighs With A Crispy Bacon Gravy"]
    ), "failed title_by_year test"

    assert isinstance(ingredient_to_recipe(["Sirloin Steak"]), list), "ingredient_to_recipe not returning a list"
    assert sorted(ingredient_to_recipe(["Sirloin Steak"])) == sorted(
        ["Steak with Chimichurri and Potatoes"]
    ), "failed title_by_year_range test"

    assert isinstance(serving_size([5]), list), "serving_size not returning a value"
    assert sorted(serving_size([5])) == sorted(
        ["fresh prawn rolls"]
    ), "failed title_before_year test"

    assert isinstance(cook_time([90]), list), "cook_time not returning a value"
    assert sorted(cook_time([90])) == sorted(
        ["Gordon's Simple Marinara at Home"]
    ), "failed title_before_year test"

    assert isinstance(num_steps([3]), list), "num_steps not returning a value"
    assert sorted(num_steps([3])) == sorted(
        ["melted brie toast with macerated berries"]
    ), "failed title_before_year test"

    assert isinstance(type_of_meal(["Dessert"]), list), "ingredient_to_recipe not returning a list"
    assert sorted(type_of_meal(["Dessert"])) == sorted(
        ["Individual Sticky Toffee Puddings"]
    ), "failed title_by_year_range test"

    assert sorted(search_pa_list(["hi", "there"])) == sorted(
        ["I don't understand"]
    ), "failed search_pa_list test 1"
    # assert sorted(search_pa_list(["what", "should", "i", "make", "for",  "Thanksgiving"])) == sorted(
    #     ["Holiday Lemon-Herb Chicken Thighs With A Crispy Bacon Gravy"]
    # ), "failed search_pa_list test 2"
    # assert sorted(
    #     search_pa_list(["what", "has", "table"])
    # ) == sorted(["No answers"]), "failed search_pa_list test 3"

    print("All tests passed!")