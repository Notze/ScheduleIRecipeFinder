from .effect import EffectE
from .ingredient import IngredientE
from .product import ProductE

from typing import NamedTuple


"""Maximum number of effects in a recipe.
By game design the product won't change after this amount of effects has been reached.
"""
MaxEffectCount: int = 8


class Recipe(NamedTuple):
    """Simple dataholder object representing a recipe for the mixin station."""

    base_product: ProductE
    effects: list[EffectE]
    base_price: int
    production_cost: float

    ingredients: list[IngredientE] = []
    sell_price: float = 0
    profit: float = 0
    previous_effects: list[set[EffectE]] = []


class ShortRecipe(NamedTuple):
    """Simple dataholder object representing a recipe for the mixin station."""

    base_product: ProductE
    effects: list[EffectE]

    ingredients: list[IngredientE] = []
    multiplicator_sum: float = 0
