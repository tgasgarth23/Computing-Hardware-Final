import json

def parse_menu_to_json(menu_text):
    """
    Parse the provided menu text and convert it into a JSON format.

    Args:
    menu_text (str): The text of the menu.

    Returns:
    dict: The parsed menu in a dictionary format.
    """
    # Split the text into lines and initialize variables
    lines = menu_text.split('\n')
    menu = {}
    current_day = ""
    current_category = ""

    for line in lines:
        if line.strip().isdigit():
            # This is a new day
            current_day = line.strip()
            menu[current_day] = []
        elif line.strip() and not line.startswith(" ") and not '-' in line:
            menu[current_day].append(line.strip())

    return menu

# Example usage with the provided menu text
menu_text = """
1
Breakfast Proteins
Cage Free Fried Egg
Apple Cinnamon Pancakes
Chorizo Sausage with Onions and Peppers
Turkey Sausage Patty
Breakfast Starches
Pan Fried Potatoes
Breakfast Simple Starts
Tofu Scramble
Beyond Meat Vegan Breakfast Patty
Cage Free Hard Boiled Egg
Quinoa
Ranchero Chickpeas
Fruit of The Day & Hot Cereals
Mango Chunks
Fresh Fruit Salad
Rolled Oats
Cream of Wheat
Pastry Selection
Val's Cider Donut
Vegan GF Maple Muffin
2
Breakfast Proteins
Cage Free Scrambled Eggs
Whole Grain French Toast Sticks
Four Pepper Chicken Sausage
Bacon
Breakfast Starches
Santa Fe Potatoes
Breakfast Simple Starts
Vegetable Tofu Scramble
Beyond Meat Vegan Breakfast Patty
Cage Free Hard Boiled Egg
Brown Rice
Bush's Vegetarian Baked Beans
Fruit of The Day & Hot Cereals
Strawberries
Rolled Oats
Cheddar Grits
Pastry Selection
Cinnamon Chip Scones
Vegan GF Cinnamon Chip Muffin
3
Breakfast Proteins
Cage Free Scrambled Eggs
Turkey Sausage Patty
Pork Breakfast Sausage Link
Breakfast Starches
Chicken Bacon Ranch Hash
Belgian Waffles
Santa Fe Potatoes
Breakfast Simple Starts
Cage Free Hard Boiled Egg
Tofu Power Scramble
Refrito Pinto Beans
Hooray Foods Plant-based Bacon
White Rice
Fruit of The Day & Hot Cereals
Grapefruit
Rolled Oats
Cream of Wheat
Pastry Selection
Assorted Mini Danish
Assorted Croissants
Vegan GF Raspberry Muffin
4
Breakfast Proteins
Cage Free Fried Egg
Chicken Sausage Patty
Pork Breakfast Sausage Patty
Breakfast Starches
Tripleberry Pancake
Pan Fried Potatoes
Breakfast Simple Starts
Cage Free Hard Boiled Egg
Berkshire Scramble
Greco Garbanzo Beans
Gardein Vegan Breakfast Patty
Quinoa
Fruit of The Day & Hot Cereals
Blackberries
Cantaloupe
Rolled Oats
Cream of Wheat
Pastry Selection
Blueberry Muffin
Vegan GF Blueberry Muffin
5
Breakfast Proteins
Cage Free Scrambled Eggs
Bacon
Four Pepper Chicken Sausage
Breakfast Starches
Belgian Waffles
Rosemary Roasted Red Potatoes
Breakfast Simple Starts
Cage Free Hard Boiled Egg
Southwest Tofu Scramble
Morning Star Vegetarian Breakfast Patty
Bush's Vegetarian Baked Beans
Jasmine Rice
Fruit of The Day & Hot Cereals
Pear
Pineapple
Rolled Oats
Cream of Wheat
Omelette Bar Protein
Eggs
JustEgg Vegan Scramble
Omelette Bar Toppings
Diced Tomatoes
Diced Green & Red Bell Peppers
Spinach
Diced Yellow Onion
Mushrooms
Daiya Vegan Shredded Cheddar "Cheese"
Shredded White Cheddar Cheese
Crumbled Bacon
Veggie Sausage of the Day
Pastry Selection
Chocolate Muffin
Vegan GF Double Chocolate Muffin
6
Breakfast Proteins
Cage Free Fried Egg
Grilled Ham Steak
Turkey Bacon
Breakfast Starches
O'Brien Potatoes
Chocolate Chip Pancakes
Breakfast Simple Starts
Cage Free Hard Boiled Egg
JustEgg Folded
Beyond Meat Vegan Breakfast Link
Brown Rice
Black Beans with Olive Oil
Fruit of The Day & Hot Cereals
Blueberries
Red Grapes
Rolled Oats
Cream of Wheat
Pastry Selection
Assorted Gourmet Pastries
Vegan GF Cranberry Orange Muffin
7
Chocolate Chip Muffin
Navy Beans & Greens
Vegan GF Chocolate Chip Muffin
Breakfast Proteins
Cage Free Scrambled Eggs
Grilled Kielbasa
Sausage Chicken and Apple
Breakfast Starches
Whole Grain French Toast Sticks
Breakfast Simple Starts
Cage Free Hard Boiled Egg
Tofu Scramble with Asparagus & Mushroom
Gardein Vegan Breakfast Patty
Basmati Rice
Fruit of The Day & Hot Cereals
Honeydew Melon
Peaches
Rolled Oats
Cream of Wheat
Omelette Bar Protein
Eggs
JustEgg Vegan Scramble
Omelette Bar Toppings
Diced Tomatoes
Spinach
Diced Yellow Onion
Mushrooms
Diced Green & Red Bell Peppers
Daiya Vegan Shredded Cheddar "Cheese"
Sliced Swiss Cheese
Crumbled Bacon
Veggie Sausage of the Day
8
Breakfast Proteins
Cage Free Fried Egg
Chorizo Sausage with Onions and Peppers
Turkey Sausage Patty
Breakfast Starches
Blueberry Pancakes
Herbed Breakfast Potatoes
Quinoa
Breakfast Simple Starts
Cage Free Hard Boiled Egg
Tofu Scramble
Ranchero Red Beans
Beyond Meat Vegan Breakfast Patty
Fruit of The Day & Hot Cereals
Mango Chunks
Fresh Fruit Salad
Rolled Oats
Cream of Wheat
Pastry Selection
Assorted Donuts
Vegan GF Apple Cider Muffin
9
Breakfast Proteins
Cage Free Scrambled Eggs
Chicken Sausage Patty
Canadian Bacon
Breakfast Starches
Belgian Waffles
Home Fries
Breakfast Simple Starts
Cage Free Hard Boiled Egg
Vegetable Tofu Scramble
Bush's Vegetarian Baked Beans
Field Roast Vegan Apple Maple Sausage
Brown Rice
Fruit of The Day & Hot Cereals
Strawberries
Rolled Oats
Omelette Bar Protein
Eggs
JustEgg Vegan Scramble
Omelette Bar Toppings
Diced Green & Red Bell Peppers
Diced Tomatoes
Mushrooms
Diced Yellow Onion
Spinach
Daiya Vegan Shredded Cheddar "Cheese"
Shredded White Cheddar Cheese
Crumbled Bacon
Veggie Sausage of the Day
Pastry Selection
Blueberry Scones
Vegan GF Blueberry Muffin
10
Breakfast Proteins
Cage Free Scrambled Eggs
Shakshuka
Turkey Sausage Patty
Pork Breakfast Sausage Link
Breakfast Starches
French Toast
O'Brien Potatoes
Breakfast Simple Starts
Tex Mex Tofu Scramble
Cage Free Hard Boiled Egg
Hooray Foods Plant-based Bacon
Refrito Red Beans
White Rice
Fruit of The Day & Hot Cereals
Grapefruit
Rolled Oats
Pastry Selection
Assorted Mini Danish
Assorted Croissants
Vegan GF Maple Muffin
11
Breakfast Proteins
Cage Free Fried Egg
Chicken Sausage Patty
Pork Breakfast Sausage Patty
Breakfast Starches
Herbed Breakfast Potatoes
Pancakes
Breakfast Simple Starts
Cage Free Hard Boiled Egg
Berkshire Scramble
Greco Pinto Beans
Gardein Vegan Breakfast Patty
Quinoa
Fruit of The Day & Hot Cereals
Blackberries
Cantaloupe
Rolled Oats
Cream of Wheat
Pastry Selection
Zucchini Muffin
Vegan GF Zucchini & Carrot Muffin
12
Breakfast Proteins
Cage Free Scrambled Eggs
Bacon
Four Pepper Chicken Sausage
Breakfast Starches
Belgian Waffles
Home Fries
Breakfast Simple Starts
Cage Free Hard Boiled Egg
Southwest Tofu Scramble
Morning Star Vegetarian Breakfast Patty
Bush's Vegetarian Baked Beans
Jasmine Rice
Fruit of The Day & Hot Cereals
Pear
Pineapple
Rolled Oats
Cream of Wheat
Omelette Bar Protein
Eggs
JustEgg Vegan Scramble
Omelette Bar Toppings
Diced Tomatoes
Mushrooms
Diced Yellow Onion
Diced Green & Red Bell Peppers
Spinach
Daiya Vegan Shredded Cheddar "Cheese"
Shredded White Cheddar Cheese
Crumbled Bacon
Veggie Sausage of the Day
Pastry Selection
Strawberry Muffin
Vegan GF Strawberry Muffin
13
Breakfast Proteins
Cage Free Fried Egg
Grilled Ham Steak
Turkey Bacon
Breakfast Starches
Pancakes
Hash Browns
Breakfast Simple Starts
Cage Free Hard Boiled Egg
JustEgg Folded
Beyond Meat Vegan Breakfast Link
Brown Rice
Chickpeas with Olive Oil
Fruit of The Day & Hot Cereals
Blueberries
Red Grapes
Rolled Oats
Cream of Wheat
Pastry Selection
Vanilla Tea Bread
Vegan GF Vanilla Bean Muffin
14
Breakfast Proteins
Cage Free Scrambled Eggs
Grilled Kielbasa
Sausage Chicken and Apple
Breakfast Starches
Whole Grain French Toast Sticks
Santa Fe Potatoes
Breakfast Simple Starts
Cage Free Hard Boiled Egg
Tofu Scramble with Asparagus & Mushroom
Basmati Rice
Black Beans & Greens
Gardein Vegan Breakfast Patty
Fruit of The Day & Hot Cereals
Honeydew Melon
Peaches
Rolled Oats
Cream of Wheat
Omelette Bar Protein
JustEgg Vegan Scramble
Eggs
Omelette Bar Toppings
Diced Tomatoes
Mushrooms
Diced Yellow Onion
Diced Green & Red Bell Peppers
Spinach
Daiya Vegan Shredded Cheddar "Cheese"
Sliced Swiss Cheese
Crumbled Bacon
Veggie Sausage of the Day
Dessert
Cinnamon Twists
Vegan GF Cherry Muffin
15
Val's Cider Donut
Dessert
Vegan GF Maple Muffin
Breakfast Proteins
Chorizo Sausage with Onions and Peppers
Turkey Sausage Patty
Breakfast Starches
Pan Fried Potatoes
Pancakes
Breakfast Simple Starts
Cage Free Hard Boiled Egg
Tofu Scramble
Ranchero Navy Beans
Beyond Meat Vegan Breakfast Patty
Quinoa
Fruit of The Day & Hot Cereals
Mango Chunks
Fresh Fruit Salad
Rolled Oats
Cream of Wheat
16
Vegan GF Blackberry Muffin
Breakfast Proteins
Cage Free Scrambled Eggs
Bacon
Chicken Sausage Patty
Breakfast Starches
Whole Grain French Toast Sticks
Rosemary Roasted Red Potatoes
Breakfast Simple Starts
Cage Free Hard Boiled Egg
Vegetable Tofu Scramble
Brown Rice
Bush's Vegetarian Baked Beans
Field Roast Vegan Apple Maple Sausage
Fruit of The Day & Hot Cereals
Strawberries
Rolled Oats
Omelette Bar Protein
Eggs
JustEgg Vegan Scramble
Omelette Bar Toppings
Spinach
Diced Tomatoes
Mushrooms
Diced Yellow Onion
Diced Green & Red Bell Peppers
Crumbled Bacon
Daiya Vegan Shredded Cheddar "Cheese"
Shredded White Cheddar Cheese
Veggie Sausage of the Day
Pastry Selection
Assorted Croissants
Cinnamon Chip Scones
17
Breakfast Proteins
Cage Free Scrambled Eggs
Turkey Sausage Patty
Pork Breakfast Sausage Link
Breakfast Starches
French Toast
Santa Fe Potatoes
Breakfast Simple Starts
Cage Free Hard Boiled Egg
Refrito Cannellini Beans
Tofu Power Scramble
Hooray Foods Plant-based Bacon
Refrito Navy Beans
White Rice
Fruit of The Day & Hot Cereals
Grapefruit
Rolled Oats
Pastry Selection
Assorted Mini Danish
Assorted Croissants
Vegan GF Cinnamon Muffin
"""

# Parse the menu
parsed_menu = parse_menu_to_json(menu_text)

# Write the parsed menu to a JSON file
file_path = 'src/val_menu/december_breakfast.json'
with open(file_path, 'w') as file:
    json.dump(parsed_menu, file, indent=4)

