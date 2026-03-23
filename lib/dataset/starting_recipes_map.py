from ..datamodel import ProductE, EffectE, Recipe


starting_recipes_map: dict[ProductE, Recipe] = {
    ProductE.OG_KUSH: Recipe(ProductE.OG_KUSH, [EffectE.CALMING], 35, 30 + (10 + 30) / 12),
    # Street Rat IV
    ProductE.SOUR_DIESEL: Recipe(ProductE.SOUR_DIESEL, [EffectE.REFRESHING], 35, 35),
    # Hoodlum II
    ProductE.GREEN_CRACK: Recipe(ProductE.GREEN_CRACK, [EffectE.ENERGIZING], 35, 40),
    # Hoodlum IV
    ProductE.GRANDDADDY_PURPLE: Recipe(ProductE.GRANDDADDY_PURPLE, [EffectE.SEDATING], 35, 45),
    # ???
    ProductE.METH: Recipe(ProductE.METH, [], 70, (60 + 80) / 10),
}
