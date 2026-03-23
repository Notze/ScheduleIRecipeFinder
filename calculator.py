from lib.custom_types import Recipe
from lib.utility import prettyPrint
from lib.dataset.starting_recipes_map import starting_recipes_map
import lib.mixer as mixer

# list of ingredients beginning with the starting drug
input_recipe: list[str] = [
    "OG-Kush",
    "Viagra",
    "Addy",
    "Horse Semen",
    "Battery",
    "Battery",
    "Addy",
    "Horse Semen",
    "Mouthwash",
]

# wether or not a copy-pastable output for unit test creation shall be printed
print_unittest_dataset: bool = True


# @brief: Prints the recipes with the highest profit
# prints progress while iterating through ingredients
def main():
    global input_recipe
    unittest_set = []

    mixGivenRecipe(starting_recipes_map[input_recipe[0]], input_recipe[1:], unittest_set)

    if print_unittest_dataset:
        print("('" + str(input_recipe[0]) + "', [")
        for entry in unittest_set:
            print(str(entry) + ",")
        print("])")


def mixGivenRecipe(recipe: Recipe, ingredients: list[str], unittest_set: list[str, list[str]]):
    for ingredient_name in ingredients:
        recipe = mixer.mixOneIngredientLong(recipe, ingredient_name)
        unittest_set.append((ingredient_name, recipe.effects))

        if print_unittest_dataset:
            print(recipe.ingredients)
            print(recipe.effects)
        prettyPrint(recipe)


main()
