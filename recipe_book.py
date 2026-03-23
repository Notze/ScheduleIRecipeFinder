from lib.custom_types import Recipe
from lib.dataset.multiplier_map import multiplier_map
from lib.dataset.ingredients_map import ingredients_map
from lib.utility import prettyPrint
from lib.dataset.starting_recipes_map import starting_recipes_map


def resetTierList():
    global best_recipes
    global best_recipes_count
    global least_best_recipes_profit
    best_recipes = [ShortRecipe([], [])]
    best_recipes_count = 1
    least_best_recipes_profit = 0


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
            best_recipes_by_profit.sort(key=lambda recipe: (recipe.profit), reverse=True)
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
            best_recipes_by_sell_price.sort(key=lambda recipe: (recipe.sell_price), reverse=True)
            best_recipes_by_sell_price = best_recipes_by_sell_price[:best_recipes_count]
            least_best_recipes_sell_price = best_recipes_by_sell_price[-1].sell_price
        if verbose:
            long_recipe = best_recipes_by_sell_price[0]
            print(long_recipe.ingredients)
            prettyPrint(long_recipe)
            if print_progress:
                progress_bar.start()
                progress_bar.update(progress_counter)
