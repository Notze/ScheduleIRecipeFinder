from typing import NamedTuple
from enum import IntEnum


class EffectE(IntEnum):
    """All known drug effects."""

    ANTI_GRAVITY = 0
    ATHLETIC = 1
    BALDING = 2
    BRIGHT_EYED = 3
    CALMING = 4
    CALORIE_DENSE = 5
    CYCLOPEAN = 6
    DISORIENTING = 7
    ELECTRIFYING = 8
    ENERGIZING = 9
    EUPHORIC = 10
    EXPLOSIVE = 11
    FOCUSED = 12
    FOGGY = 13
    GINGERITIS = 14
    GLOWING = 15
    JENNERISING = 16
    LAXATIVE = 17
    LETHAL = 18
    LONG_FACED = 19
    MUNCHIES = 20
    PARANOIA = 21
    REFRESHING = 22
    SCHIZOPHRENIC = 23
    SEDATING = 24
    SEIZURE_INDUCING = 25
    SHRINKING = 26
    SLIPPERY = 27
    SMELLY = 28
    SNEAKY = 29
    SPICY = 30
    THOUGHT_PROVOKING = 31
    TOXIC = 32
    TROPIC_THUNDER = 33
    ZOMBIFYING = 34


class EffectReplacement(NamedTuple):
    """Pair of two effects representing a replacement of the first with the second."""

    to_remove: EffectE
    to_add: EffectE


class EffectSwitch(NamedTuple):
    """Pair of two effects representing a switch of the first with the second and vice versa."""

    first: EffectE
    second: EffectE
