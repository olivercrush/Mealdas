import unittest
import test_scenarios

from main.ingredients.ingredient import Ingredient
from main.recipes.recipe import Recipe

def ingredient_compare(ingredient1, ingredient2, msg):
    return ingredient1.name == ingredient2.name and ingredient1.unit == ingredient2.unit

class TestIngredientMethods(unittest.TestCase):

    def setUp(self):
        self.addTypeEqualityFunc(Ingredient, ingredient_compare)

    def test_from_json_object(self):
        recipe = Recipe(test_scenarios.RECIPE_JSON_DICT)
        self.assertEqual(test_scenarios.TEST_NAME, recipe.name)
        self.assertEqual(test_scenarios.TEST_DURATION, recipe.duration_in_min)
        self.assertEqual(test_scenarios.TEST_STEPS, recipe.steps)
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_1), recipe.ingredients[0]["ingredient"])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_2), recipe.ingredients[1]["ingredient"])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_3), recipe.ingredients[2]["ingredient"])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_4), recipe.ingredients[3]["ingredient"])
        self.assertEqual(test_scenarios.AMOUNT_1, recipe.ingredients[0]["amount"])
        self.assertEqual(test_scenarios.AMOUNT_2, recipe.ingredients[1]["amount"])
        self.assertEqual(test_scenarios.AMOUNT_3, recipe.ingredients[2]["amount"])
        self.assertEqual(test_scenarios.AMOUNT_4, recipe.ingredients[3]["amount"])

    def test_get_json_object(self):
        recipe = Recipe()
        recipe.add_name(test_scenarios.TEST_NAME)
        recipe.add_duration_in_min(test_scenarios.TEST_DURATION)
        recipe.add_step(test_scenarios.STEP_1)
        recipe.add_step(test_scenarios.STEP_2)
        recipe.add_step(test_scenarios.STEP_3)
        recipe.add_step(test_scenarios.STEP_4)
        recipe.add_ingredient(Ingredient(test_scenarios.INGREDIENT_1), test_scenarios.AMOUNT_1)
        recipe.add_ingredient(Ingredient(test_scenarios.INGREDIENT_2), test_scenarios.AMOUNT_2)
        recipe.add_ingredient(Ingredient(test_scenarios.INGREDIENT_3), test_scenarios.AMOUNT_3)
        recipe.add_ingredient(Ingredient(test_scenarios.INGREDIENT_4), test_scenarios.AMOUNT_4)
        self.assertEqual(test_scenarios.RECIPE_JSON_DICT, recipe.get_json_object())

    def test_add_name(self):
        recipe = Recipe()
        recipe.add_name(test_scenarios.TEST_NAME)
        self.assertEqual(test_scenarios.TEST_NAME, recipe.name)

    def test_add_duration(self):
        recipe = Recipe()
        recipe.add_duration_in_min(test_scenarios.TEST_DURATION)
        self.assertEqual(test_scenarios.TEST_DURATION, recipe.duration_in_min)

    def test_add_step(self):
        recipe = Recipe()
        recipe.add_step(test_scenarios.STEP_1)
        recipe.add_step(test_scenarios.STEP_2)
        recipe.add_step(test_scenarios.STEP_3)
        recipe.add_step(test_scenarios.STEP_4)
        self.assertEqual(test_scenarios.TEST_STEPS, recipe.steps)

    def test_add_ingredient(self):
        recipe = Recipe()
        recipe.add_ingredient(Ingredient(test_scenarios.INGREDIENT_1), test_scenarios.AMOUNT_1)
        recipe.add_ingredient(Ingredient(test_scenarios.INGREDIENT_2), test_scenarios.AMOUNT_2)
        recipe.add_ingredient(Ingredient(test_scenarios.INGREDIENT_3), test_scenarios.AMOUNT_3)
        recipe.add_ingredient(Ingredient(test_scenarios.INGREDIENT_4), test_scenarios.AMOUNT_4)
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_1), recipe.ingredients[0]["ingredient"])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_2), recipe.ingredients[1]["ingredient"])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_3), recipe.ingredients[2]["ingredient"])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_4), recipe.ingredients[3]["ingredient"])
        self.assertEqual(test_scenarios.AMOUNT_1, recipe.ingredients[0]["amount"])
        self.assertEqual(test_scenarios.AMOUNT_2, recipe.ingredients[1]["amount"])
        self.assertEqual(test_scenarios.AMOUNT_3, recipe.ingredients[2]["amount"])
        self.assertEqual(test_scenarios.AMOUNT_4, recipe.ingredients[3]["amount"])

if __name__ == '__main__':
    unittest.main()