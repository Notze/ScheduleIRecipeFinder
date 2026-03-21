import typing
from enum import Enum


# @brief Simple dataholder object representing a recipe for the mixin station.
class ShortRecipe(typing.NamedTuple):
    ingredients: list[str]
    effects: list[str]

    multiplikator_sum: float = 0


# @brief Simple dataholder object representing a recipe for the mixin station.
class Recipe(typing.NamedTuple):
    ingredients: list[str]
    effects: list[str]
    base_price: int
    production_cost: float

    sell_price: float = 0
    profit: float = 0


# @brief Pair of two effec names representing a replacement effect of an ingredient.
class EffectReplacement(typing.NamedTuple):
    to_remove: str
    to_add: str


# @brief Pair of two effec names representing a bi-directional replacement effect of an ingredient.
class EffectSwitch(typing.NamedTuple):
    first: str
    second: str


# Player Level Ingame
class Level(Enum):
    HOODLUM_I = 1
    HOODLUM_II = 2
    HOODLUM_III = 3
    HOODLUM_IV = 4
    HOODLUM_V = 5
    PEDDLER_I = 6
    PEDDLER_II = 7
    PEDDLER_III = 8
    PEDDLER_IV = 9
    PEDDLER_V = 10
    HUSTLER_I = 11
    HUSTLER_II = 12
    HUSTLER_III = 13
    HUSTLER_IV = 14
    HUSTLER_V = 15


# @brief Simple dataholder for ingredients specific properties excluding the name
# is used in the ingredients map
class Ingredient(typing.NamedTuple):
    level: Level
    price: int
    added_effect: str
    effect_replacements: list[EffectReplacement]
    effect_switches: list[EffectSwitch] = []
