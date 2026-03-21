from lib.custom_types import ShortRecipe
from lib.custom_types import Ingredients, Recipe
from lib.datamodel.multiplier_map import multiplier_map
from lib.ingredients import ingredients_map
from lib.utility import prettyPrint
from lib.datamodel.starting_recipes import starting_recipes_map
import lib.mixer as mixer

import progressbar
import time
import datetime
from enum import Enum

# drugs to start mixing with
available_drugs: dict[str, bool] = {
    "OG-Kush": True,
    # "Sour-Diesel": True,
    # "Green-Crack": True,
    # "Granddaddy-Purple": True,
    # "Meth": True,
}
# ingredients to mix with [ingredient_name, is_ingredient_available]
available_ingredients: dict[Ingredients, bool] = {
    Ingredients.BANANA: True,
    Ingredients.CUKE: True,
    Ingredients.DONUT: True,
    Ingredients.PARACETAMOL: True,
    Ingredients.VIAGRA: True,
    # IngredientName.MOUTHWASH: True,
    # IngredientName.FLU_MEDICINE: True,
    # IngredientName.GASOLINE: True,
    # IngredientName.ENERGY_DRINK: True,
    # IngredientName.MOTOR_OIL: True,
    # IngredientName.MEGA_BEAN: True,
    # IngredientName.BATTERY: True,
    # IngredientName.CHILI: True,
    # IngredientName.IODINE: True,
    # IngredientName.ADDY: True,
    # IngredientName.HORSE_SEMEN: True,
}
# max length of the recipe
max_ingredient_count = 8
# print the currently best recipe everytime a better one is found
verbose = False
# value for time estimation
nano_seconds_per_iterations = 150
# wenn bei mehr iterationen der spmi sinkt, ist der wert zu klein
time_overhead_constant = 0.75  # .5 <> 1

# wether or not to print progress while experimenting with recipes
print_progress = True
# higher value leads to more frequent updates on the progress bar
# this impacts the performance
# range [1:max_ingredient_count]
progress_bar_resolution = 1
# progress bar object for printing during iterations
progress_bar = progressbar.ProgressBar(
    maxval=len(available_ingredients) ** progress_bar_resolution
)
# update variable for progress bar
progress_counter = 0

# list with the most profitable recipes
best_recipes_by_sell_price: list[Recipe] = [Recipe([""], [], 0, 0.0)]
best_recipes_by_profit: list[Recipe] = [Recipe([""], [], 0, 0.0)]
# number of recipes to print beginning with the most profitable
best_recipes_count: int = 1
# lowest sort value in current best_recipes list
least_best_recipes_sell_price: float = 0
least_best_recipes_profit: float = 0


class Timestamp(Enum):
    UNKNOWN = 1
    INGREDIENT_BANANA_START = 1
    INGREDIENT_Cuke_START = 2
    INGREDIENT_Donut_START = 3
    INGREDIENT_Paracetamol_START = 4
    INGREDIENT_Viagra_START = 5
    INGREDIENT_Mouthwash_START = 6
    INGREDIENT_Flu_Medicine_START = 7
    INGREDIENT_Gasoline_START = 8
    INGREDIENT_Energy_Drink_START = 9
    INGREDIENT_Motor_Oil_START = 10
    INGREDIENT_Mega_Bean_START = 11
    INGREDIENT_Battery_START = 12
    INGREDIENT_Chili_START = 13
    INGREDIENT_Iodine_START = 14
    INGREDIENT_Addy_START = 15
    INGREDIENT_Horse_Semen_START = 16
    START = 17
    END = 18


start_time = 0
statistics_timestamps: dict[str, int] = {}
statistics_runtimes: dict[str, int] = {}


# @brief: Prints the recipes with the highest profit
# prints progress while iterating through ingredients
def main():
    starting_recipes = [
        starting_recipes_map[drug] for drug in available_drugs if (available_drugs[drug] == True)
    ]
    findBestRecipes(starting_recipes)


def findBestRecipes(starting_recipes):
    global best_recipes_by_profit, best_recipes_by_sell_price
    global progress_bar
    global progress_counter
    global available_ingredients
    sanityCheck()
    available_ingredient_names = [
        name for name in available_ingredients if available_ingredients[name] == True
    ]
    number_of_iterations = len(available_ingredient_names) ** max_ingredient_count
    time_estimation_in_seconds = time_overhead_constant + (
        number_of_iterations * nano_seconds_per_iterations
    ) / (1000000000)
    print("Drugs         : {}".format(len(starting_recipes)))
    print("Ingredients   : {}".format(len(available_ingredient_names)))
    print("Recipe Length : {} ingredients".format(max_ingredient_count))
    print("Iterations    : {}".format(number_of_iterations))
    print(
        "Est. Time     : {}".format(
            datetime.timedelta(seconds=time_estimation_in_seconds)
        )
    )
    output_recipes_by_profit: list[Recipe] = []
    output_recipes_by_sell_price: list[Recipe] = []

    more_than_one_starting_recipe = len(starting_recipes) > 1
    for recipe in starting_recipes:
        if more_than_one_starting_recipe:
            print("Experiementing with: " + recipe.ingredients[0])

        if print_progress:
            progress_bar.start()
        resetTierList()
        mixRecursion(recipe, available_ingredient_names)
        output_recipes_by_profit += best_recipes_by_profit
        output_recipes_by_sell_price += best_recipes_by_sell_price
        if print_progress:
            progress_bar.finish()
        progress_counter = 0

        if more_than_one_starting_recipe:
            print("{} recipe with highest sell price: ".format(recipe.ingredients[0]))
            best_recipes_by_sell_price.sort(
                key=lambda recipe: (recipe.profit), reverse=True
            )
            print(best_recipes_by_sell_price[0].ingredients)
            prettyPrint(best_recipes_by_sell_price[0])
            print("{} recipe with highest profit: ".format(recipe.ingredients[0]))
            output_recipes_by_profit.sort(
                key=lambda recipe: (recipe.profit), reverse=True
            )
            print(output_recipes_by_profit[0].ingredients)
            prettyPrint(output_recipes_by_profit[0])

    print("Highest sell price recipe overall: ")
    output_recipes_by_sell_price.sort(key=lambda recipe: (recipe.profit), reverse=True)
    print(output_recipes_by_sell_price[0].ingredients)
    prettyPrint(output_recipes_by_sell_price[0])
    print("Highest profit recipe overall: ")
    output_recipes_by_profit.sort(key=lambda recipe: (recipe.profit), reverse=True)
    print(output_recipes_by_profit[0].ingredients)
    prettyPrint(output_recipes_by_profit[0])

    for runtime_ingredient in sorted(
        statistics_runtimes, key=lambda entry: (statistics_runtimes[entry])
    ):
        print(
            str(runtime_ingredient)
            + ": "
            + str(statistics_runtimes[runtime_ingredient])
        )


# @brief Checks the imported ingredients and effect map on spelling errors.
#
# @throws KeyError on first spelling error
def sanityCheck():
    global ingredients_map
    global multiplier_map
    for ingredient_name in ingredients_map:
        ingredient = ingredients_map[ingredient_name]
        multiplier_map[ingredient.added_effect]
        for effect_replacement in ingredient.effect_replacements:
            multiplier_map[effect_replacement.to_remove]
            multiplier_map[effect_replacement.to_add]


# @brief  Mixes every available ingredient into the given recipe.
# adds the resulting recipe into the best_recipes list if applicable
#
# @param recipe
# @param progress_bar a progressbar.ProgressBar object to update if applicable
def mixRecursion(recipe: Recipe, available_ingredient_names: list[str]):
    global ingredients_map
    global progress_bar
    global progress_counter
    global start_time
    global statistics_runtimes
    for ingredient_name in available_ingredient_names:
        if print_progress and len(recipe.ingredients) == progress_bar_resolution:
            if progress_counter >= 1:
                logTimestamp(Timestamp(progress_counter))
                elapsed_time = time.time() - start_time
                print(
                    "Est. Time {}   : {} ({:.0f} seconds / {} steps * {} steps_max)".format(
                        progress_counter,
                        datetime.timedelta(
                            seconds=(
                                (elapsed_time / progress_counter) * progress_bar.maxval
                            )
                        ),
                        elapsed_time,
                        progress_counter,
                        progress_bar.maxval,
                    )
                )
                statistics_runtimes[
                    available_ingredient_names[progress_counter - 1]
                ] = elapsed_time
                progress_bar.start()
            progress_bar.update(progress_counter)
            progress_counter += 1
        new_recipe = mixer.mixOneIngredientLong(recipe, ingredient_name)
        if new_recipe.effects == recipe.effects:
            continue

        updateBestRecipesList(new_recipe)
        if not ingredientListFull(new_recipe) and not recipeDead(new_recipe):
            mixRecursion(new_recipe, available_ingredient_names)


def ingredientListFull(recipe: Recipe):
    global max_ingredient_count
    return len(recipe.ingredients) - 1 >= max_ingredient_count


def recipeDead(recipe: Recipe):
    ingredients = recipe.ingredients
    if len(ingredients) < 3:
        return False
    return (ingredients[-1] == ingredients[-2]) and (ingredients[-1] == ingredients[-3])


def logTimestamp(key: str):
    global start_time
    global statistics_timestamps, statistics_runtimes
    current_time = time.time()
    statistics_timestamps[key] = current_time
    if key == "start_time":
        start_time = current_time


# def mixRecursion(recipe: ShortRecipe, available_ingredient_names: list[str]):
#     global ingredients_map
#     global progress_bar
#     global progress_counter
#     global start_time
#     for ingredient_name in available_ingredient_names:
#         if (print_progress
#                 and len(recipe.ingredients) == progress_bar_resolution):
#             if (progress_counter != 0 and math.floor(
#                     progress_bar.maxval * 100 / progress_counter) == 50):
#                 elapsed_time = time.time() - start_time
#                 print("Est. Time     : {} // {} - {} - {}".format(
#                     datetime.timedelta(seconds=(elapsed_time *
#                                                 progress_bar.maxval /
#                                                 progress_counter)),
#                     elapsed_time, progress_counter, progress_bar.maxval))
#                 progress_bar.start()
#             progress_bar.update(progress_counter)
#             progress_counter += 1
#         new_recipe = mixer.mixOneIngredient(recipe, ingredient_name)
#         if (new_recipe.effects == recipe.effects):
#             continue

#         updateBestRecipesList(new_recipe)
#         if (len(new_recipe.ingredients) - 1 < max_ingredient_count):
#             mixRecursion(new_recipe, available_ingredient_names)


#
def resetTierList():
    global best_recipes
    global best_recipes_count
    global least_best_recipes_profit
    best_recipes = [ShortRecipe([], [])]
    best_recipes_count = 1
    least_best_recipes_profit = 0


# @brief Adds recipe to best_recipes list if applicable.
#
# @param recipe the recipe to add
# def updateBestRecipesList(recipe: ShortRecipe):
#     global best_recipes
#     global least_best_recipes_profit
#     global progress_bar
#     global progress_counter
#     if (recipe.multiplikator_sum > least_best_recipes_profit):
#         if (best_recipes_count == 1):
#             best_recipes = [recipe]
#             least_best_recipes_profit = recipe.multiplikator_sum
#         else:
#             best_recipes.append(recipe)
#             best_recipes.sort(key=lambda recipe: (recipe.multiplikator_sum),
#                               reverse=True)
#             best_recipes = best_recipes[:best_recipes_count]
#             least_best_recipes_profit = best_recipes[-1].multiplikator_sum
#         if (verbose):
#             long_recipe = toRecipe(best_recipes[0])
#             print(long_recipe.ingredients)
#             prettyPrint(long_recipe)
#             if (print_progress):
#                 progress_bar.start()
#                 progress_bar.update(progress_counter)
def updateBestRecipesList(recipe: Recipe):
    global best_recipes_by_profit, best_recipes_by_sell_price
    global least_best_recipes_profit, least_best_recipes_sell_price
    global progress_bar, progress_counter
    if recipe.profit > least_best_recipes_profit:
        if best_recipes_count == 1:
            best_recipes_by_profit = [recipe]
            least_best_recipes_profit = recipe.profit
        else:
            best_recipes_by_profit.append(recipe)
            best_recipes_by_profit.sort(
                key=lambda recipe: (recipe.profit), reverse=True
            )
            best_recipes_by_profit = best_recipes_by_profit[:best_recipes_count]
            least_best_recipes_profit = best_recipes_by_profit[-1].profit
        if verbose:
            long_recipe = best_recipes_by_profit[0]
            print(long_recipe.ingredients)
            prettyPrint(long_recipe)
            if print_progress:
                progress_bar.start()
                progress_bar.update(progress_counter)
    if recipe.sell_price > least_best_recipes_sell_price:
        if best_recipes_count == 1:
            best_recipes_by_sell_price = [recipe]
            least_best_recipes_sell_price = recipe.sell_price
        else:
            best_recipes_by_sell_price.append(recipe)
            best_recipes_by_sell_price.sort(
                key=lambda recipe: (recipe.sell_price), reverse=True
            )
            best_recipes_by_sell_price = best_recipes_by_sell_price[:best_recipes_count]
            least_best_recipes_sell_price = best_recipes_by_sell_price[-1].sell_price
        if verbose:
            long_recipe = best_recipes_by_sell_price[0]
            print(long_recipe.ingredients)
            prettyPrint(long_recipe)
            if print_progress:
                progress_bar.start()
                progress_bar.update(progress_counter)


logTimestamp(Timestamp.START)
main()
number_of_ingredients = sum([1 for name in available_ingredients if available_ingredients[name] == True])
number_of_drugs = sum([1 for name in available_drugs if available_drugs[name] == True])
number_of_iterations = number_of_ingredients**max_ingredient_count * number_of_drugs
logTimestamp(Timestamp.END)
elapsed_time = time.time() - start_time
nano_seconds_per_iterations = (
    (elapsed_time - time_overhead_constant) * 1000000000 / number_of_iterations
)
print(
    "--- {:.2f} seconds // {} // {:.0f} ---".format(
        elapsed_time, time_overhead_constant, nano_seconds_per_iterations
    )
)
