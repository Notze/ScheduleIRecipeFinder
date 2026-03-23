from lib import *

import time


##
# START OF CONFIGRAITON
# Make your adjustments here. Changing these values impacts performance!
#

# remove products that shall not be used while mixing
available_products: list[ProductE] = {
    ProductE.OG_KUSH,
    # ProductE.SOUR_DIESEL,
    # ProductE.GREEN_CRACK,
    # ProductE.GRANDDADDY_PURPLE,
    # ProductE.METH,
}

# remove ingredients that shall not be used while mixing
available_ingredients: list[IngredientE] = {
    IngredientE.BANANA,
    IngredientE.CUKE,
    IngredientE.DONUT,
    IngredientE.PARACETAMOL,
    # IngredientE.VIAGRA,
    # IngredientE.MOUTHWASH,
    # IngredientE.FLU_MEDICINE,
    # IngredientE.GASOLINE,
    # IngredientE.ENERGY_DRINK,
    # IngredientE.MOTOR_OIL,
    # IngredientE.MEGA_BEAN,
    # IngredientE.BATTERY,
    # IngredientE.CHILI,
    # IngredientE.IODINE,
    # IngredientE.ADDY,
    # IngredientE.HORSE_SEMEN,
}

# maximum number of ingredients to try per recipe
max_ingredient_count: int = 9

# wether or not to look for the recipe with the most profit / highest sell price
find_highest_sell_price: bool = True
find_highest_profit: bool = False

# number of recipes to print beginning with the most profitable / highest sell price
output_recipes_count: int = 1

# if true, prints every new recipe that's added to the list of best recipes
verbose = False

# if true, prints a progress bar while mixing recipes
print_progress = True
# higher value leads to more frequent updates on the progress bar
# range [1:max_ingredient_count]
progress_bar_resolution = 1

##
# END OF CONFIGRAITON
#


# dictionary for looking up ingredients that can handle given effects
effect_ingredient_map: dict[EffectE, list[IngredientE]] = {}

# list with the most profitable recipes
recipes_with_highest_sell_price: list[Recipe] = [Recipe([""], [], 0, 0.0)]
recipes_with_highest_profit: list[Recipe] = [Recipe([""], [], 0, 0.0)]
# lowest sort value in current best_recipes list
least_best_recipes_sell_price: float = 0
least_best_recipes_profit: float = 0


def main():
    """Prints the recipes with the highest profit"""

    init()

    for product in available_products:
        resetTierList()
        findBestRecipeForProduct(product)
        printBestRecipes()


def init():
    """Initializes global variables."""

    global effect_ingredient_map

    for ingredient in [ingredients_map[ingredient_e] for ingredient_e in available_ingredients]:
        effects_removed_by_ingredient = [
            effect_replacement.to_remove for effect_replacement in ingredient.effect_replacements
        ]
        effects_removed_by_ingredient += [effect_switch.first for effect_switch in ingredient.effect_switches]
        effects_removed_by_ingredient += [effect_switch.second for effect_switch in ingredient.effect_switches]

        for effect_e in effects_removed_by_ingredient:
            if effect_e in effect_ingredient_map:
                if ingredient.name not in effect_ingredient_map[effect_e]:
                    effect_ingredient_map[effect_e].append(ingredient.name)
            else:
                effect_ingredient_map[effect_e] = [ingredient.name]


def resetTierList():
    """Resets the global variables wich is only necessary of experimenting with multiple products."""
    global recipes_with_highest_profit, recipes_with_highest_sell_price
    global least_best_recipes_profit, least_best_recipes_sell_price

    recipes_with_highest_profit = [Recipe([""], [], 0, 0.0)]
    recipes_with_highest_sell_price = [Recipe([""], [], 0, 0.0)]
    least_best_recipes_sell_price = 0
    least_best_recipes_profit = 0


def printBestRecipes():
    """Prints the recipes with the highest profit / highest sell price"""

    if find_highest_profit:
        print("Highest profit overall: ")
        recipes_with_highest_profit.sort(key=lambda recipe: (recipe.profit), reverse=True)
        for i in range(output_recipes_count):
            utility.prettyPrint(recipes_with_highest_profit[i])

    if find_highest_sell_price:
        print("Highest sell price overall: ")
        recipes_with_highest_sell_price.sort(key=lambda recipe: (recipe.profit), reverse=True)
        for i in range(output_recipes_count):
            utility.prettyPrint(recipes_with_highest_sell_price[i])


def findBestRecipeForProduct(product_e: ProductE):
    """Calls the recursion function for mixing ingredients into the recipe."""

    print("Product           : {}".format(product_e.name))
    print("Ingredients       : {} overall".format(len(available_ingredients)))
    print("Max Recipe Length : {} additives".format(max_ingredient_count))

    mixRecursion(starting_recipes_map[product_e])


def mixRecursion(recipe: Recipe):
    """Mixes every available ingredient into the given recipe.
    adds the resulting recipe into the best_recipes list if applicable"""

    ingredients_to_try = [  # all ingredients that can add their basic effect
        ingredient_e
        for ingredient_e in available_ingredients
        if (ingredients_map[ingredient_e].added_effect not in recipe.effects)
    ]
    for existing_effect in recipe.effects:  # all ingredients that can change an existing effect
        if existing_effect in effect_ingredient_map:
            ingredients_to_try += effect_ingredient_map[existing_effect]

    for ingredient_e in ingredients_to_try:
        new_recipe = mixer.mixOneIngredientLong(recipe, ingredient_e)

        if new_recipe.effects == recipe.effects:
            continue

        updateBestRecipesLists(new_recipe)

        if ingredientListFull(new_recipe) or recipeDead(new_recipe):
            continue

        mixRecursion(new_recipe)


def ingredientListFull(recipe: Recipe):
    return len(recipe.ingredients) >= max_ingredient_count


def recipeDead(recipe: Recipe):
    ingredients = recipe.ingredients
    if len(ingredients) < 3:
        return False
    return (ingredients[-1] == ingredients[-2]) and (ingredients[-1] == ingredients[-3])


def updateBestRecipesLists(recipe: Recipe):
    if find_highest_profit:
        updateHighestProfitList(recipe)
    if find_highest_sell_price:
        updateHighestSellPriceList(recipe)


def updateHighestProfitList(recipe: Recipe):
    """Updates the tier list if recipe is better than previous ones."""

    global recipes_with_highest_profit
    global least_best_recipes_profit

    if recipe.profit > least_best_recipes_profit:
        if output_recipes_count == 1:
            recipes_with_highest_profit = [recipe]
            least_best_recipes_profit = recipe.profit
        else:
            recipes_with_highest_profit.append(recipe)
            recipes_with_highest_profit.sort(key=lambda recipe: (recipe.profit), reverse=True)
            recipes_with_highest_profit = recipes_with_highest_profit[:output_recipes_count]
            least_best_recipes_profit = recipes_with_highest_profit[-1].profit

        if verbose:
            prettyPrint(recipe)


def updateHighestSellPriceList(recipe: Recipe):
    """Updates the tier list if recipe is better than previous ones."""

    global recipes_with_highest_sell_price
    global least_best_recipes_sell_price

    if recipe.sell_price > least_best_recipes_sell_price:
        if output_recipes_count == 1:
            recipes_with_highest_sell_price = [recipe]
            least_best_recipes_sell_price = recipe.sell_price
        else:
            recipes_with_highest_sell_price.append(recipe)
            recipes_with_highest_sell_price.sort(key=lambda recipe: (recipe.sell_price), reverse=True)
            recipes_with_highest_sell_price = recipes_with_highest_sell_price[:output_recipes_count]
            least_best_recipes_sell_price = recipes_with_highest_sell_price[-1].sell_price

        if verbose:
            prettyPrint(recipe)


start_time = time.time()
main()
elapsed_time = time.time() - start_time
print("--- elapsed time: {:.2f} seconds ---".format(elapsed_time))
