import unittest
from main.ingredients.ingredient import Ingredient

TEST_NAME = "TEST_NAME"
TEST_UNIT = "TEST_UNIT"
JSON_OBJECT = {
    "name": TEST_NAME,
    "unit": TEST_UNIT
}

class TestIngredientMethods(unittest.TestCase):

    def test_from_json_object(self):
        ingredient = Ingredient(JSON_OBJECT)
        self.assertEqual(True, ingredient.is_valid())
        self.assertEqual(TEST_NAME, ingredient.name)
        self.assertEqual(TEST_UNIT, ingredient.unit)

    def test_get_json_object(self):
        ingredient = Ingredient()
        ingredient.add_name("TEST_NAME")
        ingredient.add_unit("TEST_UNIT")
        self.assertEqual(JSON_OBJECT, ingredient.get_json_object())

    def test_add_name(self):
        ingredient = Ingredient()
        ingredient.add_name(TEST_NAME)
        self.assertEqual(TEST_NAME, ingredient.name)

    def test_add_unit(self):
        ingredient = Ingredient()
        ingredient.add_unit(TEST_UNIT)
        self.assertEqual(TEST_UNIT, ingredient.unit)

    def test_valid_ingredient(self):
        ingredient = Ingredient()
        ingredient.add_name(TEST_NAME)
        ingredient.add_unit(TEST_UNIT)
        self.assertEqual(True, ingredient.is_valid())

    def test_no_unit_ingredient(self):
        ingredient = Ingredient()
        ingredient.add_name(TEST_NAME)
        self.assertEqual(False, ingredient.is_valid())

    def test_no_name_ingredient(self):
        ingredient = Ingredient()
        ingredient.add_unit(TEST_UNIT)
        self.assertEqual(False, ingredient.is_valid())

if __name__ == '__main__':
    unittest.main()