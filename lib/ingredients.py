# https://hardcoregamer.com/schedule-1-every-ingredient-effects/
# https://prodigygamers.com/2025/04/18/schedule-1-all-effects-chart-list-each-mixers-result-guide/

from lib.custom_types import Ingredient, EffectReplacement, EffectSwitch, Level

ingredients_map: dict[str, Ingredient] = {
    # Hoodlum I
    "Banana":
    Ingredient(Level.HOODLUM_I, 2, "Gingeritis", [
        EffectReplacement("Calming", "Sneaky"),
        EffectReplacement("Cyclopean", "Thought-Provoking"),
        EffectReplacement("Disorienting", "Focused"),
        EffectReplacement("Focused", "Seizure-Inducing"),
        EffectReplacement("Long Faced", "Refreshing"),
        EffectReplacement("Paranoia", "Jennerising"),
        EffectReplacement("Smelly", "Anti-Gravity"),
        EffectReplacement("Toxic", "Smelly"),
    ], [
        EffectSwitch("Thought-Provoking", "Energizing"),
    ]),
    "Cuke":
    Ingredient(Level.HOODLUM_I, 2, "Energizing", [
        EffectReplacement("Euphoric", "Laxative"),
        EffectReplacement("Foggy", "Cyclopean"),
        EffectReplacement("Gingeritis", "Thought-Provoking"),
        EffectReplacement("Munchies", "Athletic"),
        EffectReplacement("Slippery", "Munchies"),
        EffectReplacement("Sneaky", "Paranoia"),
        EffectReplacement("Toxic", "Euphoric")
    ]),
    "Donut":
    Ingredient(Level.HOODLUM_I, 3, "Calorie-Dense", [
        EffectReplacement("Anti-Gravity", "Slippery"),
        EffectReplacement("Balding", "Sneaky"),
        EffectReplacement("Calorie-Dense", "Explosive"),
        EffectReplacement("Focused", "Euphoric"),
        EffectReplacement("Jennerising", "Gingeritis"),
        EffectReplacement("Shrinking", "Energizing")
    ]),
    "Paracetamol":
    Ingredient(Level.HOODLUM_I, 3, "Sneaky", [
        EffectReplacement("Calming", "Slippery"),
        EffectReplacement("Electrifying", "Athletic"),
        EffectReplacement("Focused", "Gingeritis"),
        EffectReplacement("Foggy", "Calming"),
        EffectReplacement("Glowing", "Toxic"),
        EffectReplacement("Munchies", "Anti-Gravity"),
        EffectReplacement("Paranoia", "Balding"),
        EffectReplacement("Energizing", "Paranoia"),
        EffectReplacement("Spicy", "Bright-Eyed"),
        EffectReplacement("Toxic", "Tropic Thunder")
    ]),
    "Viagra":
    Ingredient(
        Level.HOODLUM_II,
        4,
        "Tropic Thunder",
        [
            EffectReplacement("Athletic", "Sneaky"),
            EffectReplacement("Disorienting", "Toxic"),
            EffectReplacement("Euphoric", "Bright-Eyed"),
            EffectReplacement("Laxative", "Calming"),
            # EffectReplacement("Energizing", "Thought-Provoking"),
        ]),
    "Mouthwash":
    Ingredient(Level.HOODLUM_III, 4, "Balding", [
        EffectReplacement("Calming", "Anti-Gravity"),
        EffectReplacement("Calorie-Dense", "Sneaky"),
        EffectReplacement("Explosive", "Sedating"),
        EffectReplacement("Focused", "Jennerising")
    ]),
    "Flu Medicine":
    Ingredient(Level.HOODLUM_IV, 5, "Sedating", [
        EffectReplacement("Athletic", "Munchies"),
        EffectReplacement("Calming", "Bright-Eyed"),
        EffectReplacement("Cyclopean", "Foggy"),
        EffectReplacement("Electrifying", "Refreshing"),
        EffectReplacement("Euphoric", "Toxic"),
        EffectReplacement("Focused", "Calming"),
        EffectReplacement("Laxative", "Euphoric"),
        EffectReplacement("Munchies", "Slippery"),
        EffectReplacement("Shrinking", "Paranoia"),
        EffectReplacement("Thought-Provoking", "Gingeritis")
    ]),
    "Gasoline":
    Ingredient(Level.HOODLUM_V, 5, "Toxic", [
        EffectReplacement("Disorienting", "Glowing"),
        EffectReplacement("Electrifying", "Disorienting"),
        EffectReplacement("Euphoric", "Spicy"),
        EffectReplacement("Energizing", "Euphoric"),
        EffectReplacement("Energizing", "Spicy"),
        EffectReplacement("Gingeritis", "Smelly"),
        EffectReplacement("Jennerising", "Sneaky"),
        EffectReplacement("Laxative", "Foggy"),
        EffectReplacement("Munchies", "Sedating"),
        EffectReplacement("Paranoia", "Calming"),
        EffectReplacement("Shrinking", "Focused"),
        EffectReplacement("Sneaky", "Tropic Thunder"),
    ]),
    "Energy Drink":
    Ingredient(Level.PEDDLER_I, 6, "Athletic", [
        EffectReplacement("Disorienting", "Electrifying"),
        EffectReplacement("Euphoric", "Energizing"),
        EffectReplacement("Focused", "Shrinking"),
        EffectReplacement("Foggy", "Laxative"),
        EffectReplacement("Glowing", "Disorienting"),
        EffectReplacement("Schizophrenic", "Balding"),
        EffectReplacement("Sedating", "Munchies"),
        EffectReplacement("Spicy", "Euphoric"),
        EffectReplacement("Tropic Thunder", "Sneaky")
    ]),
    "Motor Oil":
    Ingredient(Level.PEDDLER_II, 6, "Slippery", [
        EffectReplacement("Energizing", "Munchies"),
        EffectReplacement("Euphoric", "Sedating"),
        EffectReplacement("Foggy", "Toxic"),
        EffectReplacement("Munchies", "Schizophrenic"),
        EffectReplacement("Paranoia", "Anti-Gravity")
    ]),
    "Mega Bean":
    Ingredient(Level.PEDDLER_III, 7, "Foggy", [
        EffectReplacement("Athletic", "Laxative"),
        EffectReplacement("Calming", "Glowing"),
        EffectReplacement("Energizing", "Cyclopean"),
        EffectReplacement("Focused", "Disorienting"),
        EffectReplacement("Jennerising", "Paranoia"),
        EffectReplacement("Seizure-Inducing", "Focused"),
        EffectReplacement("Shrinking", "Electrifying"),
        EffectReplacement("Slippery", "Toxic"),
        EffectReplacement("Sneaky", "Calming"),
        EffectReplacement("Thought-Provoking", "Energizing")
    ]),
    "Battery":
    Ingredient(Level.PEDDLER_IV, 8, "Bright-Eyed", [
        EffectReplacement("Euphoric", "Zombifying"),
        EffectReplacement("Electrifying", "Euphoric"),
        EffectReplacement("Laxative", "Calorie-Dense"),
        EffectReplacement("Munchies", "Tropic Thunder"),
        EffectReplacement("Shrinking", "Munchies"),
    ]),
    "Chili":
    Ingredient(Level.PEDDLER_V, 7, "Spicy", [
        EffectReplacement("Athletic", "Euphoric"),
        EffectReplacement("Anti-Gravity", "Tropic Thunder"),
        EffectReplacement("Laxative", "Long Faced"),
        EffectReplacement("Munchies", "Toxic"),
        EffectReplacement("Shrinking", "Refreshing"),
        EffectReplacement("Sneaky", "Bright-Eyed"),
    ]),
    "Iodine":
    Ingredient(Level.HUSTLER_I, 8, "Jennerising", [
        EffectReplacement("Calming", "Balding"),
        EffectReplacement("Calorie-Dense", "Gingeritis"),
        EffectReplacement("Euphoric", "Seizure-Inducing"),
        EffectReplacement("Foggy", "Paranoia"),
        EffectReplacement("Refreshing", "Thought-Provoking"),
        EffectReplacement("Toxic", "Sneaky"),
    ]),
    "Addy":
    Ingredient(Level.HUSTLER_II, 9, "Thought-Provoking", [
        EffectReplacement("Explosive", "Euphoric"),
        EffectReplacement("Foggy", "Energizing"),
        EffectReplacement("Glowing", "Refreshing"),
        EffectReplacement("Long Faced", "Electrifying"),
        EffectReplacement("Sedating", "Gingeritis"),
    ]),
    "Horse Semen":
    Ingredient(Level.HUSTLER_III, 9, "Long Faced", [
        EffectReplacement("Anti-Gravity", "Calming"),
        EffectReplacement("Gingeritis", "Refreshing"),
        EffectReplacement("Thought-Provoking", "Electrifying"),
    ]),
}
