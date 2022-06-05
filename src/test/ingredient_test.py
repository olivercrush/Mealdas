import unittest
import test_scenarios

from main.ingredients.ingredient import Ingredient

class TestIngredientMethods(unittest.TestCase):

    def test_from_json_object(self):
        ingredient = Ingredient(test_scenarios.INGREDIENT_JSON_DICT)
        self.assertEqual(True, ingredient.is_valid())
        self.assertEqual(test_scenarios.TEST_NAME, ingredient.name)
        self.assertEqual(test_scenarios.TEST_UNIT, ingredient.unit)

    def test_get_json_object(self):
        ingredient = Ingredient()
        ingredient.add_name("TEST_NAME")
        ingredient.add_unit("TEST_UNIT")
        self.assertEqual(test_scenarios.INGREDIENT_JSON_DICT, ingredient.get_json_object())

    def test_add_name(self):
        ingredient = Ingredient()
        ingredient.add_name(test_scenarios.TEST_NAME)
        self.assertEqual(test_scenarios.TEST_NAME, ingredient.name)

    def test_add_unit(self):
        ingredient = Ingredient()
        ingredient.add_unit(test_scenarios.TEST_UNIT)
        self.assertEqual(test_scenarios.TEST_UNIT, ingredient.unit)

    def test_valid_ingredient(self):
        ingredient = Ingredient()
        ingredient.add_name(test_scenarios.TEST_NAME)
        ingredient.add_unit(test_scenarios.TEST_UNIT)
        self.assertEqual(True, ingredient.is_valid())

    def test_no_unit_ingredient(self):
        ingredient = Ingredient()
        ingredient.add_name(test_scenarios.TEST_NAME)
        self.assertEqual(False, ingredient.is_valid())

    def test_no_name_ingredient(self):
        ingredient = Ingredient()
        ingredient.add_unit(test_scenarios.TEST_UNIT)
        self.assertEqual(False, ingredient.is_valid())

if __name__ == '__main__':
    unittest.main()