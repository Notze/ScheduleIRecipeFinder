from .datamodel import *
from . import dataset

import copy


def mixOneIngredientLong(recipe: Recipe, ingredient_e: IngredientE):
    """Mixes the given ingredient into the given recipe.

    @param recipe: the recipe to add the new ingredient to
    @param ingredient_e: the ingredient to add to the given recipe
    @return the resulting recipe
    """

    new_ingredient = dataset.ingredients_map[ingredient_e]

    base_product = recipe.base_product
    ingredients = recipe.ingredients + [ingredient_e]
    effects = updateEffects(recipe.effects, new_ingredient)
    base_price = recipe.base_price
    production_cost = recipe.production_cost + new_ingredient.price
    sell_price = calculateSellPrice(base_price, effects)
    profit = calculateProfit(sell_price, production_cost)
    previous_effects = copy.copy(recipe.previous_effects)
    return Recipe(base_product, effects, base_price, production_cost, ingredients, sell_price, profit, previous_effects)


# def mixOneIngredient(recipe: ShortRecipe, ingredient_e: IngredientE):
#     """Mixes the given ingredient into the given recipe.

#     @param ShortRecipe: the recipe to start with
#     @param ingredient_name: the ingredient to add to the starting recipe
#     @return the resulting recipe
#     """

#     new_ingredient = dataset.ingredients_map[ingredient_e]

#     ingredients = recipe.ingredients + [ingredient_e]
#     effects = updateEffects(recipe.effects, new_ingredient)
#     multiplikator_sum = sum([dataset.multiplier_map[effect_e] for effect_e in effects])
#     return ShortRecipe(ingredients, effects, multiplikator_sum)


def updateEffects(effects: list[EffectE], ingredient_data: Ingredient):
    """applies all ingredient effects to the effect list"""

    new_effects = copy.copy(effects)

    an_effect_was_replaced = applyReplacements(new_effects, effects, ingredient_data.effect_replacements)

    if an_effect_was_replaced:
        applySwitches(new_effects, ingredient_data.effect_switches)

    if len(new_effects) < recipe.MaxEffectCount:
        if not ingredient_data.added_effect in new_effects:
            new_effects.append(ingredient_data.added_effect)

    new_effects.sort()
    return list(set(new_effects))


def applyReplacements(
    new_effects: list[EffectE], original_effects: list[EffectE], effect_replacements: list[EffectReplacement]
):
    """applies the ingredients replacements effects"""

    replaced_an_effect = False
    for effect_replacement in effect_replacements:
        original_effect_existed = effect_replacement.to_remove in original_effects
        original_effect_not_removed_yet = effect_replacement.to_remove in new_effects
        target_effect_not_present_yet = not effect_replacement.to_add in new_effects
        if original_effect_existed and original_effect_not_removed_yet and target_effect_not_present_yet:
            new_effects.remove(effect_replacement.to_remove)
            new_effects.append(effect_replacement.to_add)
            replaced_an_effect = True
    return replaced_an_effect


def applySwitches(effects: list[EffectE], effect_switches: list[EffectSwitch]):
    """applies the ingredients switch effects"""
    for effect_switch in effect_switches:
        if effect_switch.first in effects and not effect_switch.second in effects:
            effects.remove(effect_switch.first)
            effects.append(effect_switch.second)
        elif effect_switch.second in effects and not effect_switch.first in effects:
            effects.remove(effect_switch.second)
            effects.append(effect_switch.first)


def calculateSellPrice(base_price: int, effects: list[EffectE]):
    multiplier = 1 + sum([dataset.multiplier_map[effect_e] for effect_e in effects])
    return base_price * multiplier


def calculateProfit(sell_price: int, production_cost: int):
    return sell_price - production_cost
