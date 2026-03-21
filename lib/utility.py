from lib.custom_types import Recipe, ShortRecipe
import lib.recipes as recipes, lib.ingredients as ingredients


# @brief Prints a recipe in a human readable format.
def prettyPrint(recipe: Recipe):
    effects_to_print = recipe.effects
    effects_to_print.sort()

    recipe_string = "Ingredients:\n\n"
    ingredient_number = 1
    for ingredient in recipe.ingredients[1:]:
        recipe_string += " " + str(ingredient_number) + ". " + str(
            ingredient) + "\n"
        ingredient_number += 1
    recipe_string += "\n"
    recipe_string += "Effects:\n"
    effects_printed = 0
    for effect in effects_to_print:
        if (effects_printed % 2 == 0):
            recipe_string += "\n " + str(effect)
        else:
            recipe_string += ", " + str(effect)
        effects_printed += 1
    recipe_string += "\n"
    recipe_string += "\n"
    recipe_string += "Sell Price     :  " + str(int(recipe.sell_price)) + "\n"
    recipe_string += "Production Cost:  " + str(int(
        recipe.production_cost)) + "\n"
    recipe_string += "Profit         :  " + str(int(recipe.profit))

    print_msg_box(recipe_string, title=str(recipe.ingredients[0]))


# @brief Prints a recipe in a human readable format.
def prettyPrintShort(recipe: ShortRecipe):
    effects_to_print = recipe.effects
    effects_to_print.sort()

    recipe_string = "Ingredients:\n\n"
    ingredient_number = 1
    for ingredient in recipe.ingredients[1:]:
        recipe_string += " " + str(ingredient_number) + ". " + str(
            ingredient) + "\n"
        ingredient_number += 1
    recipe_string += "\n"
    recipe_string += "Effects:\n"
    effects_printed = 0
    for effect in effects_to_print:
        if (effects_printed % 2 == 0):
            recipe_string += "\n " + str(effect)
        else:
            recipe_string += ", " + str(effect)
        effects_printed += 1

    print_msg_box(recipe_string, title=str(recipe.ingredients[0]))


def toRecipe(recipe: ShortRecipe):
    starting_recipe = recipes.starting_recipes_map[recipe.ingredients[0]]
    production_cost = starting_recipe.production_cost + sum([
        ingredients.ingredients_map[ingredient].price
        for ingredient in recipe.ingredients[1:]
    ])
    sell_price = starting_recipe.base_price * (1 + recipe.multiplikator_sum)
    return (Recipe(ingredients=recipe.ingredients,
                   effects=recipe.effects,
                   base_price=starting_recipe.base_price,
                   production_cost=production_cost,
                   sell_price=sell_price,
                   profit=sell_price - production_cost))


# stolen from here: https://stackoverflow.com/questions/39969064/how-to-print-a-message-box-in-python
def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)
