import lib.types as types


class IngredientData(typing.NamedTuple):
    """Simple dataholder for ingredients specific properties excluding the name"""

    level: types.PlayerLevelE
    price: int
    added_effect: types.EffectE
    effect_replacements: list[types.EffectReplacement]
    effect_switches: list[types.EffectSwitch] = []
