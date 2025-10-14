#This line is like importing tools from a toolbox. It's bringing in special helpers called List and Tuple from Python's typing section.
from typing import List, Tuple

#recipe's chosen from Gordan Ramsay's Ultimate Cookery Course https://www.gordonramsay.com/gr/recipes/brietoastwithberries/

#each 'Tuple' is a recipe that contains several variables that creates the "object"
#Tuple[
#name of the recipe, 
#list of ingredients, 
#serving size,
#cooking time,
#cooking complexity (how many steps),
#what type of meal  (breakfast, lunch, dinner, dessert),
#event to cook this meal for]
recipe_db: List[Tuple[str, List[str], int, int, int, str, str]] = [
    (
        "melted brie toast with macerated berries",
        ["3 cups mixed berries, divided", 
         "1/4th cup (50g) sugar",
         "Zest of 1/2th Lemon",
         "1 tablespoon lemon juice"
         ],
         "2",
         "120",
         "3",
         "Breakfast",
         "No Event"
    ),
    (
        "texas hanger steak tacos with pico de gallo",
        ["1 hanger steak",
         "kosher salt",
         "black pepper",
         "olive oil",
         "1 cleaned cactus pad(napal)",
         "1 diced small red onion",
         "1 lime",
         "1 frescno chile sliced",
         "3 scallions sliced thick, discarded roots",
         "1 bunch cilantro, roughly chopped",
         "1 diced tomato",
         "1 clove garlic",
         "1 avocado, sliced thick",
         "4 corn tortillas",
         "mexican crema or sour cream"
         ],
         "1",
         "30",
         "8",
         "Lunch",
         "No Event"
    ),
    (
        "fresh prawn rolls",
        ["200g dried vermicelli or fine rice noodles",
         "500g cooked king prawns, peeled, deveined and roughly chopped",
         "2 baby gem lettuces, shredded",
         "4 spring onions, trimmed and chopped",
         "2 large carrots, peeled and grated",
         "4 tbsp chopped coriander",
         "4 tbsp chopped Thai basil",
         "4 tbsp chopped mint",
         "Juice of 2 limes",
         "26 round rice paper sheets (16cm diameter)"
         ],
         "5",
         "30",
         "5",
         "Lunch",
         "No Event"
     ),
     (
         "beef wellington",
         ["2 x 400g beef fillets",
          "Olive oil, for frying",
          "500g mixture of wild mushrooms, cleaned",
          "1 thyme sprig, leaves only",
          "500g puff pastry",
          "8 slices of Parma ham",
          "2 egg yolks, beaten with 1 tbsp water and a pinch of salt",
          "Sea salt and freshly ground black pepper",
          "200g beef trimmings (ask the butcher to reserve these when trimming the fillet)",
          "4 large shallots, peeled and sliced",
          "12 black peppercorns",
          "1 bay leaf",
          "1 thyme sprig",
          "Splash of red wine vinegar",
          "1 x 750ml bottle red wine",
          "750ml beef stock"
         ],
         "4",
         "120",
         "11",
         "Dinner",
         "No Event"
     ),
     (
         "potato and butternut squash gratin with crispy shallots",
         ["3 shallots, peeled",
          "2 cups neutral oil such as canola",
          "Kosher salt",
          "1 ½ pounds butternut squash, neck only, ideally less than 3” diameter",
          "1 ½ pounds large waxy potatoes, such as red, about 3 medium potatoes",
          "16 oz (2 cups) whole milk",
          "16 oz (2 cups) heavy cream",
          "4 large garlic cloves, smashed",
          "2 sprigs thyme",
          "2 bay leaves",
          "4 ounces gruyere cheese, finely grated",
          "1 tablespoon kosher salt",
          "A few cracks of freshly ground black pepper",
          "Butter, for greasing"
         ],
         "7",
         "120",
         "11",
         "Dinner",
         "Christmas"
     ),
     (
         "https://www.gordonramsay.com/gr/recipes/chickenthighswithbacongravy/"
     ),
     (
        "https://www.gordonramsay.com/gr/recipes/stickytoffee-pudding/"
      ),
      (
        "https://www.gordonramsay.com/gr/recipes/lobsterblt/"  
      ),
      (
          "https://www.gordonramsay.com/gr/recipes/simplemarinara/"
      ),
      (
          "https://www.gordonramsay.com/gr/recipes/steak-with-chimichurri-and-potatoes-from-ramsay-in-10-live/"
      )
]