from lib.types import DrugE, EffectE
from lib.datamodel import Recipe


starting_recipes_map: dict[DrugE, Recipe] = {
    DrugE.OG_KUSH: Recipe(DrugE.OG_KUSH, [EffectE.CALMING], 35, 30 + (10 + 30) / 12),
    # Street Rat IV
    DrugE.SOUR_DIESEL: Recipe(DrugE.SOUR_DIESEL, [EffectE.REFRESHING], 35, 35),
    # Hoodlum II
    DrugE.GREEN_CRACK: Recipe(DrugE.GREEN_CRACK, [EffectE.ENERGIZING], 35, 40),
    # Hoodlum IV
    DrugE.GRANDDADDY_PURPLE: Recipe(DrugE.GRANDDADDY_PURPLE, [EffectE.SEDATING], 35, 45),
    # ???
    DrugE.METH: Recipe(DrugE.METH, [], 70, (60 + 80) / 10),
}
