from . import effect
from . import player_level
from . import ingredient

from enum import Enum
from typing import NamedTuple


class IngredientE(Enum):
    """All known mixing ingredients."""

    BANANA = 1
    CUKE = 2
    DONUT = 3
    PARACETAMOL = 4
    VIAGRA = 5
    MOUTHWASH = 6
    FLU_MEDICINE = 7
    GASOLINE = 8
    ENERGY_DRINK = 9
    MOTOR_OIL = 10
    MEGA_BEAN = 11
    BATTERY = 12
    CHILI = 13
    IODINE = 14
    ADDY = 15
    HORSE_SEMEN = 16


class Ingredient(NamedTuple):
    """Simple dataholder for ingredient specific properties"""

    name: ingredient.IngredientE
    level: player_level.PlayerLevelE
    price: int
    added_effect: effect.EffectE
    effect_replacements: list[effect.EffectReplacement]
    effect_switches: list[effect.EffectSwitch] = []
