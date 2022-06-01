import unittest
from os.path import exists
from os import remove
import json
from main.ingredients.ingredient import Ingredient
from main.ingredients.ingredient_list import IngredientList

EMPTY_TEST_LIST_FILEPATH = "test/res/test.json"
TEST_LIST_FILEPATH = "test/res/ingredients.json"
TEST_LIST_UPDATE_FILEPATH = "test/res/ingredients_update.json"

INGREDIENT_1 = {"name": "garlic", "unit": "clove"}
INGREDIENT_2 = {"name": "steak", "unit": "g"}
INGREDIENT_3 = {"name": "chicken", "unit": "mcx"}
INGREDIENT_4 = {"name": "pepper", "unit": "pinch"}
INGREDIENT_5 = {"name": "pasta", "unit": "g"}
INGREDIENT_6 = {"name": "zuchini", "unit": "mcx"}
INGREDIENT_7 = {"name": "tomato", "unit": "mcx"}
INGREDIENT_8 = {"name": "rice", "unit": "g"}
INGREDIENT_9 = {"name": "lentils", "unit": "g"}
INGREDIENT_10 = {"name": "potato", "unit": "mcx"}
INGREDIENT_11 = {"name": "onion", "unit": "mcx"}

JSON_TEST_LIST = [
    INGREDIENT_1,
    INGREDIENT_2,
    INGREDIENT_3,
    INGREDIENT_4,
    INGREDIENT_5,
    INGREDIENT_6,
    INGREDIENT_7,
    INGREDIENT_8,
    INGREDIENT_9,
    INGREDIENT_10
]

class TestIngredientListMethods(unittest.TestCase):

    def test_initialization(self):
        list = IngredientList(EMPTY_TEST_LIST_FILEPATH)
        self.assertTrue(exists(EMPTY_TEST_LIST_FILEPATH))

    def test_load_list_file(self):
        list = IngredientList(TEST_LIST_FILEPATH)
        self.assertEqual(INGREDIENT_1, list.ingredients[0].get_json_object())
        self.assertEqual(INGREDIENT_2, list.ingredients[1].get_json_object())
        self.assertEqual(INGREDIENT_3, list.ingredients[2].get_json_object())
        self.assertEqual(INGREDIENT_4, list.ingredients[3].get_json_object())
        self.assertEqual(INGREDIENT_5, list.ingredients[4].get_json_object())
        self.assertEqual(INGREDIENT_6, list.ingredients[5].get_json_object())
        self.assertEqual(INGREDIENT_7, list.ingredients[6].get_json_object())
        self.assertEqual(INGREDIENT_8, list.ingredients[7].get_json_object())
        self.assertEqual(INGREDIENT_9, list.ingredients[8].get_json_object())
        self.assertEqual(INGREDIENT_10, list.ingredients[9].get_json_object())

    def test_update_list_file(self):
        list = IngredientList(TEST_LIST_UPDATE_FILEPATH)
        list.add_ingredient(Ingredient(INGREDIENT_1))
        list.add_ingredient(Ingredient(INGREDIENT_2))
        list.add_ingredient(Ingredient(INGREDIENT_3))
        list.add_ingredient(Ingredient(INGREDIENT_4))
        list.add_ingredient(Ingredient(INGREDIENT_5))
        list.add_ingredient(Ingredient(INGREDIENT_6))
        list.add_ingredient(Ingredient(INGREDIENT_7))
        list.add_ingredient(Ingredient(INGREDIENT_8))
        list.add_ingredient(Ingredient(INGREDIENT_9))
        list.add_ingredient(Ingredient(INGREDIENT_10))
        
        with open(TEST_LIST_UPDATE_FILEPATH, 'r') as f:
            self.assertEqual(JSON_TEST_LIST, json.load(f))

    def test_get_json_object(self):
        list = IngredientList(TEST_LIST_FILEPATH)
        self.assertEqual(JSON_TEST_LIST, list.get_json_object())

    def test_ingredient_already_exists(self):
        list = IngredientList(TEST_LIST_FILEPATH)
        self.assertTrue(list.ingredient_already_exists(Ingredient(INGREDIENT_1)))

    def test_ingredient_doesnt_exists(self):
        list = IngredientList(TEST_LIST_FILEPATH)
        self.assertFalse(list.ingredient_already_exists(Ingredient(INGREDIENT_11)))

    def test_get_ingredient_exists(self):
        list = IngredientList(TEST_LIST_FILEPATH)
        self.assertEqual(INGREDIENT_1, list.get_ingredient("garlic").get_json_object())

    def test_get_ingredient_doesnt_exists(self):
        list = IngredientList(TEST_LIST_FILEPATH)
        self.assertIsNone(list.get_ingredient(Ingredient(INGREDIENT_11)))

    def test_add_ingredient(self):
        list = IngredientList(EMPTY_TEST_LIST_FILEPATH)
        list.add_ingredient(Ingredient(INGREDIENT_1))
        self.assertEqual(INGREDIENT_1, list.ingredients[0].get_json_object())

    def tearDown(self):
        if exists(EMPTY_TEST_LIST_FILEPATH):
            remove(EMPTY_TEST_LIST_FILEPATH)

        if exists(TEST_LIST_UPDATE_FILEPATH):
            remove(TEST_LIST_UPDATE_FILEPATH)

if __name__ == '__main__':
    unittest.main()