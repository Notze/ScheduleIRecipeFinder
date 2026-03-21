import typing
import lib.types as types


class Recipe(typing.NamedTuple):
    """Simple dataholder object representing a recipe for the mixin station."""

    base_product: types.DrugE
    effects: list[types.EffectE]
    base_price: int
    production_cost: float

    ingredients: list[types.IngredientE] = []
    sell_price: float = 0
    profit: float = 0


class ShortRecipe(typing.NamedTuple):
    """Simple dataholder object representing a recipe for the mixin station."""

    base_product: types.DrugE
    effects: list[types.EffectE]

    ingredients: list[types.IngredientE] = []
    multiplicator_sum: float = 0
