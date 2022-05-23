import unittest
from main.ingredients.ingredient import Ingredient

class TestIngredientMethods(unittest.TestCase):

    def test_from_json_object(self):
        pass

    def test_add_name(self):
        ingredient = Ingredient()
        ingredient.add_name("TEST_NAME")
        self.assertEqual(ingredient.name, "TEST_NAME")

    def test_add_unit(self):
        ingredient = Ingredient()
        ingredient.add_unit("TEST_UNIT")
        self.assertEqual(ingredient.unit, "TEST_UNIT")

    def test_valid_ingredient(self):
        ingredient = Ingredient()
        ingredient.add_name("TEST_NAME")
        ingredient.add_unit("TEST_UNIT")
        self.assertEqual(ingredient.is_valid(), True)

    def test_no_unit_ingredient(self):
        ingredient = Ingredient()
        ingredient.add_name("TEST_NAME")
        self.assertEqual(ingredient.is_valid(), False)

    def test_no_name_ingredient(self):
        ingredient = Ingredient()
        ingredient.add_unit("TEST_UNIT")
        self.assertEqual(ingredient.is_valid(), False)

if __name__ == '__main__':
    unittest.main()