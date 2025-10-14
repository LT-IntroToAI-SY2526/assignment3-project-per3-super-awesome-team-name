#This line is like importing tools from a toolbox. It's bringing in special helpers called List and Tuple from Python's typing section.
from typing import List, Tuple

#recipe's chosen from Gordan Ramsay's Ultimate Cookery Course

#each 'Tuple' is a recipe that contains several variables that creates the "object"
#Tuple[
#name of the recipe, 
#list of ingredients, 
#serving size,
#cooking time,
#cooking complexity (how many steps),
#what type of meal (b,l,d),
#event to cook this meal for]
recipe_db: List[Tuple[str, List[str], int, int, int, str, str]] = [

]