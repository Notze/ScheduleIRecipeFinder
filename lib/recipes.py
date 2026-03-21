import lib.custom_types as custom_types

starting_recipes_map: dict[str, custom_types.Recipe] = {
    "OG-Kush":
    custom_types.Recipe(["OG-Kush"], ["Calming"], 35, 30 + (10 + 30) / 12),
    # Street Rat IV
    "Sour-Diesel":
    custom_types.Recipe(["Sour-Diesel"], ["Refreshing"], 35, 35),
    # Hoodlum II
    "Green-Crack":
    custom_types.Recipe(["Green-Crack"], ["Energizing"], 35, 40),
    # Hoodlum IV
    "Granddaddy-Purple":
    custom_types.Recipe(["Granddaddy-Purple"], ["Sedating"], 35, 45),
    # ???
    "Meth":
    custom_types.Recipe(["Meth"], [], 70, (60 + 80) / 10),
}
