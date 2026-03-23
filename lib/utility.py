from lib.datamodel import Recipe, ShortRecipe

import lib.dataset as dataset


def prettyPrint(recipe: Recipe):
    """Prints a recipe in a human readable format."""
    effects_to_print = recipe.effects
    effects_to_print.sort()

    recipe_string = "Ingredients:\n\n"
    current_ingredient_number = 1
    for ingredient_e in recipe.ingredients:
        recipe_string += " " + str(current_ingredient_number) + ". " + str(ingredient_e.name) + "\n"
        current_ingredient_number += 1
    recipe_string += "\n"

    recipe_string += "Effects:\n"
    effects_printed = 0
    for effect_e in effects_to_print:
        if effects_printed % 2 == 0:
            recipe_string += "\n " + str(effect_e.name)
        else:
            recipe_string += ", " + str(effect_e.name)
        effects_printed += 1
    recipe_string += "\n\n"

    recipe_string += "Sell Price     :  " + str(int(recipe.sell_price)) + "\n"
    recipe_string += "Production Cost:  " + str(int(recipe.production_cost)) + "\n"
    recipe_string += "Profit         :  " + str(int(recipe.profit))

    print_msg_box(recipe_string, title=str(recipe.base_product.name))


def prettyPrintShort(short_recipe: ShortRecipe):
    """Prints a short recipe in a human readable format."""
    effects_to_print = short_recipe.effects
    effects_to_print.sort()

    recipe_string = "Ingredients:\n\n"
    current_ingredient_number = 1
    for ingredient_e in short_recipe.ingredients:
        recipe_string += " " + str(current_ingredient_number) + ". " + str(ingredient_e.name) + "\n"
        current_ingredient_number += 1
    recipe_string += "\n"

    recipe_string += "Effects:\n"
    effects_printed = 0
    for effect_e in effects_to_print:
        if effects_printed % 2 == 0:
            recipe_string += "\n " + str(effect_e.name)
        else:
            recipe_string += ", " + str(effect_e.name)
        effects_printed += 1

    print_msg_box(recipe_string, title=str(short_recipe.base_product.name))


def toRecipe(short_recipe: ShortRecipe):
    """Convert a short recipe to a recipe"""
    starting_recipe = dataset.starting_recipes_map[short_recipe.base_product]
    production_cost = starting_recipe.production_cost + sum(
        [dataset.ingredients_map[ingredient_e].price for ingredient_e in short_recipe.ingredients]
    )
    sell_price = starting_recipe.base_price * (1 + short_recipe.multiplicator_sum)

    return Recipe(
        ingredients=short_recipe.ingredients,
        effects=short_recipe.effects,
        base_price=starting_recipe.base_price,
        production_cost=production_cost,
        sell_price=sell_price,
        profit=sell_price - production_cost,
    )


def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    # stolen from here: https://stackoverflow.com/questions/39969064/how-to-print-a-message-box-in-python
    lines = msg.split("\n")
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f"║{space}{title:<{width}}{space}║\n"  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += "".join([f"║{space}{line:<{width}}{space}║\n" for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)


def updateEffectHistory(recipe: Recipe):
    """Adds the current list of effects to the history. Returns False if history already contains the current set of effects"""

    current_effects = set(recipe.effects)

    if current_effects in recipe.previous_effects:
        return False

    recipe.previous_effects.append(current_effects)
    return True
