from lib.custom_types import Recipe, ShortRecipe
from lib.effects import multiplier_map
from lib.ingredients import ingredients_map

import copy


# @brief Mixes the given ingredient into the given recipe.
#
# @param recipe: the recipe to start with
# @param ingredient_name: the ingredient to add to the starting recipe
# @return the resulting recipe
def mixOneIngredientLong(recipe: Recipe, ingredient_name: str):
    global multiplier_map
    global ingredients_map

    new_ingredient = ingredients_map[ingredient_name]

    ingredients = recipe.ingredients + [ingredient_name]
    effects = calculateEffects(recipe.effects, new_ingredient)
    base_price = recipe.base_price
    production_cost = recipe.production_cost + new_ingredient.price
    sell_price = calculateSellPrice(base_price, effects)
    profit = calculateProfit(sell_price, production_cost)
    return Recipe(ingredients, effects, base_price, production_cost,
                  sell_price, profit)


# @brief Mixes the given ingredient into the given recipe.
#
# @param ShortRecipe: the recipe to start with
# @param ingredient_name: the ingredient to add to the starting recipe
# @return the resulting recipe
def mixOneIngredient(recipe: ShortRecipe, ingredient_name: str):
    global multiplier_map
    global ingredients_map

    new_ingredient = ingredients_map[ingredient_name]

    ingredients = recipe.ingredients + [ingredient_name]
    effects = calculateEffects(recipe.effects, new_ingredient)
    multiplikator_sum = sum([multiplier_map[effect] for effect in effects])
    return ShortRecipe(ingredients, effects, multiplikator_sum)


# @brief Calculates the effects after adding the ingredient.
def calculateEffects(effects: list[str], ingredient: str):
    new_effects = copy.copy(effects)

    replaced_an_effect = False
    for effect_replacement in ingredient.effect_replacements:
        source_effect_present = effect_replacement.to_remove in new_effects
        source_effect_not_removed_by_different_rule = effect_replacement.to_remove in new_effects
        target_effect_not_present_yet = not effect_replacement.to_add in new_effects
        if (source_effect_present
                and source_effect_not_removed_by_different_rule
                and target_effect_not_present_yet):
            new_effects.remove(effect_replacement.to_remove)
            new_effects.append(effect_replacement.to_add)
            replaced_an_effect = True

    if (replaced_an_effect):
        for effect_switch in ingredient.effect_switches:
            if (effect_switch.first in new_effects
                    and not effect_switch.second in new_effects):
                new_effects.remove(effect_switch.first)
                new_effects.append(effect_switch.second)
            elif (effect_switch.second in new_effects
                  and not effect_switch.first in new_effects):
                new_effects.remove(effect_switch.second)
                new_effects.append(effect_switch.first)

    if (len(new_effects) < 8):
        if (not ingredient.added_effect in new_effects):
            new_effects.append(ingredient.added_effect)

    new_effects.sort()
    return list(set(new_effects))


# @brief Calculates the sell price.
def calculateSellPrice(base_price: int, effects: list[str]):
    multiplier = 1 + sum([multiplier_map[effect] for effect in effects])
    return base_price * multiplier


# @brief Calculates the profit.
def calculateProfit(sell_price: int, production_cost: int):
    return sell_price - production_cost
