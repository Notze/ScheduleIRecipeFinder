import sys

sys.path.append('..')
import lib.mixer as mixer

from lib.custom_types import Recipe
from lib.effects import multiplier_map
from lib.ingredients import ingredients_map
from lib.recipes import starting_recipes_map


def main():
    tests: list[bool] = [
        unittest__og_kush__mix_one_ingredient("OG-Kush", [
            ("Cuke", ["Energizing", "Calming"]),
            ("Gasoline", ["Toxic", "Calming", "Euphoric"]),
            ("Cuke", ["Energizing", "Calming", "Laxative", "Euphoric"]),
            ("Mega Bean",
             ["Foggy", "Glowing", "Laxative", "Cyclopean", "Euphoric"]),
            ("Gasoline",
             ["Foggy", "Glowing", "Laxative", "Cyclopean", "Spicy", "Toxic"]),
            ("Viagra", [
                "Foggy", "Glowing", "Calming", "Cyclopean", "Spicy", "Toxic",
                "Tropic Thunder"
            ]),
            ("Banana", [
                "Energizing", "Gingeritis", "Smelly", "Sneaky", "Foggy",
                "Spicy", "Tropic Thunder", "Glowing"
            ]),
            ("Cuke", [
                "Paranoia", "Smelly", "Glowing", "Energizing", "Spicy",
                "Cyclopean", "Tropic Thunder", "Thought-Provoking"
            ]),
            ("Banana", [
                "Energizing", "Spicy", "Jennerising", "Thought-Provoking",
                "Cyclopean", "Anti-Gravity", "Tropic Thunder", "Glowing"
            ]),
        ]),
        unittest__og_kush__mix_one_ingredient("OG-Kush", [
            ("Banana", ["Gingeritis", "Sneaky"]),
            ("Gasoline", ["Smelly", "Tropic Thunder", "Toxic"]),
            ("Cuke", ["Energizing", "Euphoric", "Tropic Thunder", "Smelly"]),
            ("Gasoline",
             ["Euphoric", "Tropic Thunder", "Smelly", "Spicy", "Toxic"]),
            ("Cuke", [
                "Energizing", "Euphoric", "Tropic Thunder", "Laxative",
                "Smelly", "Spicy"
            ]),
            ("Banana", [
                "Thought-Provoking", "Anti-Gravity", "Euphoric",
                "Tropic Thunder", "Gingeritis", "Laxative", "Spicy"
            ]),
            ("Viagra", [
                "Thought-Provoking", "Anti-Gravity", "Calming",
                "Tropic Thunder", "Gingeritis", "Bright-Eyed", "Spicy"
            ]),
            ("Mega Bean", [
                "Foggy", "Anti-Gravity", "Glowing", "Tropic Thunder",
                "Gingeritis", "Bright-Eyed", "Spicy", "Energizing"
            ]),
            ("Cuke", [
                "Thought-Provoking", "Anti-Gravity", "Glowing",
                "Tropic Thunder", "Cyclopean", "Bright-Eyed", "Spicy",
                "Energizing"
            ]),
        ]),
        unittest__og_kush__mix_one_ingredient("OG-Kush", [
            ('Banana', ['Gingeritis', 'Sneaky']),
            ('Cuke', ['Energizing', 'Paranoia', 'Thought-Provoking']),
            ('Gasoline', ['Calming', 'Euphoric', 'Thought-Provoking', 'Toxic'
                          ]),
            ('Cuke', [
                'Calming', 'Energizing', 'Euphoric', 'Laxative',
                'Thought-Provoking'
            ]),
            ('Mega Bean', [
                'Cyclopean', 'Energizing', 'Euphoric', 'Foggy', 'Glowing',
                'Laxative'
            ]),
            ('Viagra', [
                'Bright-Eyed', 'Calming', 'Cyclopean', 'Energizing', 'Foggy',
                'Glowing', 'Tropic Thunder'
            ]),
            ('Mouthwash', [
                'Anti-Gravity', 'Balding', 'Bright-Eyed', 'Cyclopean',
                'Energizing', 'Foggy', 'Glowing', 'Tropic Thunder'
            ]),
        ]),
        unittest__og_kush__mix_one_ingredient('Meth', [
            ('Mega Bean', ['Foggy']),
            ('Paracetamol', ['Calming', 'Sneaky']),
            ('Cuke', ['Calming', 'Energizing', 'Paranoia']),
            ('Mega Bean', ['Cyclopean', 'Foggy', 'Glowing', 'Paranoia']),
            ('Motor Oil',
             ['Anti-Gravity', 'Cyclopean', 'Glowing', 'Slippery', 'Toxic']),
            ('Cuke', [
                'Anti-Gravity', 'Cyclopean', 'Energizing', 'Euphoric',
                'Glowing', 'Munchies'
            ]),
            ('Battery', [
                'Anti-Gravity', 'Bright-Eyed', 'Cyclopean', 'Energizing',
                'Glowing', 'Tropic Thunder', 'Zombifying'
            ]),
        ]),
        unittest__og_kush__mix_one_ingredient('Meth', [
            ('Mouthwash', ['Balding']),
            ('Motor Oil', ['Balding', 'Slippery']),
            ('Cuke', ['Balding', 'Energizing', 'Munchies']),
            ('Paracetamol', ['Anti-Gravity', 'Balding', 'Paranoia', 'Sneaky']),
            ('Gasoline', [
                'Anti-Gravity', 'Balding', 'Calming', 'Toxic', 'Tropic Thunder'
            ]),
            ('Cuke', [
                'Anti-Gravity', 'Balding', 'Calming', 'Energizing', 'Euphoric',
                'Tropic Thunder'
            ]),
            ('Mega Bean', [
                'Anti-Gravity', 'Balding', 'Cyclopean', 'Euphoric', 'Foggy',
                'Glowing', 'Tropic Thunder'
            ]),
            ('Battery', [
                'Anti-Gravity', 'Balding', 'Bright-Eyed', 'Cyclopean', 'Foggy',
                'Glowing', 'Tropic Thunder', 'Zombifying'
            ]),
        ]),
        unittest__og_kush__mix_one_ingredient('Meth', [
            ('Paracetamol', ['Sneaky']),
            ('Mega Bean', ['Calming', 'Foggy']),
            ('Motor Oil', ['Calming', 'Slippery', 'Toxic']),
            ('Cuke', ['Calming', 'Energizing', 'Euphoric', 'Munchies']),
            ('Mega Bean',
             ['Cyclopean', 'Euphoric', 'Foggy', 'Glowing', 'Munchies']),
            ('Battery', [
                'Bright-Eyed', 'Cyclopean', 'Foggy', 'Glowing',
                'Tropic Thunder', 'Zombifying'
            ]),
            ('Iodine', [
                'Bright-Eyed', 'Cyclopean', 'Glowing', 'Jennerising',
                'Paranoia', 'Tropic Thunder', 'Zombifying'
            ]),
            ('Motor Oil', [
                'Anti-Gravity', 'Bright-Eyed', 'Cyclopean', 'Glowing',
                'Jennerising', 'Slippery', 'Tropic Thunder', 'Zombifying'
            ]),
        ]),
        unittest__og_kush__mix_one_ingredient('OG-Kush', [
            ('Cuke', ['Calming', 'Energizing']),
            ('Donut', ['Calming', 'Calorie-Dense', 'Energizing']),
            ('Paracetamol',
             ['Paranoia', 'Calorie-Dense', 'Slippery', 'Sneaky']),
            ('Banana', [
                'Jennerising', 'Calorie-Dense', 'Gingeritis', 'Slippery',
                'Sneaky'
            ]),
            ('Cuke', [
                'Jennerising', 'Calorie-Dense', 'Energizing', 'Munchies',
                'Paranoia', 'Thought-Provoking'
            ]),
            ('Paracetamol', [
                'Anti-Gravity', 'Balding', 'Calorie-Dense', 'Jennerising',
                'Paranoia', 'Sneaky', 'Thought-Provoking'
            ]),
            ('Banana', [
                'Anti-Gravity', 'Balding', 'Calorie-Dense', 'Gingeritis',
                'Jennerising', 'Sneaky', 'Thought-Provoking', 'Paranoia'
            ]),
        ]),
        unittest__og_kush__mix_one_ingredient('OG-Kush', [
            ('Banana', ['Gingeritis', 'Sneaky']),
            ('Mega Bean', ['Calming', 'Foggy', 'Gingeritis']),
            ('Motor Oil', ['Calming', 'Gingeritis', 'Slippery', 'Toxic']),
            ('Cuke', [
                'Calming', 'Energizing', 'Euphoric', 'Munchies',
                'Thought-Provoking'
            ]),
            ('Battery', [
                'Bright-Eyed', 'Calming', 'Energizing', 'Thought-Provoking',
                'Tropic Thunder', 'Zombifying'
            ]),
            ('Horse Semen', [
                'Bright-Eyed', 'Calming', 'Electrifying', 'Energizing',
                'Long Faced', 'Tropic Thunder', 'Zombifying'
            ]),
            ('Mega Bean', [
                'Bright-Eyed', 'Cyclopean', 'Electrifying', 'Foggy', 'Glowing',
                'Long Faced', 'Tropic Thunder', 'Zombifying'
            ]),
        ]),
        unittest__og_kush__mix_one_ingredient('OG-Kush', [
            ('Viagra', ['Calming', 'Tropic Thunder']),
            ('Addy', ['Calming', 'Thought-Provoking', 'Tropic Thunder']),
            ('Horse Semen',
             ['Calming', 'Electrifying', 'Long Faced', 'Tropic Thunder']),
            ('Battery', [
                'Bright-Eyed', 'Calming', 'Euphoric', 'Long Faced',
                'Tropic Thunder'
            ]),
            ('Battery', [
                'Bright-Eyed', 'Calming', 'Long Faced', 'Tropic Thunder',
                'Zombifying'
            ]),
            ('Addy', [
                'Bright-Eyed', 'Calming', 'Electrifying', 'Thought-Provoking',
                'Tropic Thunder', 'Zombifying'
            ]),
            ('Horse Semen', [
                'Bright-Eyed', 'Calming', 'Electrifying', 'Long Faced',
                'Thought-Provoking', 'Tropic Thunder', 'Zombifying'
            ]),
            ('Mouthwash', [
                'Anti-Gravity', 'Balding', 'Bright-Eyed', 'Electrifying',
                'Long Faced', 'Thought-Provoking', 'Tropic Thunder',
                'Zombifying'
            ]),
        ])
    ]

    print("\nTestresults: {} out of {} tests failed".format(
        sum([1 for x in tests if x == False]), len(tests)))


def unittest__og_kush__mix_one_ingredient(
        substance: str, recipe_effects_list: list[str, list[str]]):
    print("\nTestcase: " + substance)
    recipe = starting_recipes_map[substance]
    for (ingredient_name, expected_effects) in recipe_effects_list:

        recipe = mixer.mixOneIngredient(recipe, ingredient_name)

        new_effects = recipe.effects
        new_effects.sort()
        expected_effects.sort()
        print("Expectations met after adding " + ingredient_name + ": " +
              str(new_effects == expected_effects))
        if (not new_effects == expected_effects):
            print("Expected: " + str(expected_effects))
            print("Actual  : " + str(new_effects))
            return False
    return True


main()
