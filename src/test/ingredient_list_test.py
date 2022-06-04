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

OBJECT_TEST_LIST = [
    Ingredient(INGREDIENT_1),
    Ingredient(INGREDIENT_2),
    Ingredient(INGREDIENT_3),
    Ingredient(INGREDIENT_4),
    Ingredient(INGREDIENT_5),
    Ingredient(INGREDIENT_6),
    Ingredient(INGREDIENT_7),
    Ingredient(INGREDIENT_8),
    Ingredient(INGREDIENT_9),
    Ingredient(INGREDIENT_10)
]

def ingredient_compare(ingredient1, ingredient2, msg):
    return ingredient1.name == ingredient2.name and ingredient1.unit == ingredient2.unit

class TestIngredientListMethods(unittest.TestCase):

    def setUp(self):
        self.addTypeEqualityFunc(Ingredient, ingredient_compare)

    def test_load_list_file(self):
        list = IngredientList()
        list.load_list_file(TEST_LIST_FILEPATH)
        self.assertEqual(Ingredient(INGREDIENT_1), list.ingredients[0])
        self.assertEqual(Ingredient(INGREDIENT_2), list.ingredients[1])
        self.assertEqual(Ingredient(INGREDIENT_3), list.ingredients[2])
        self.assertEqual(Ingredient(INGREDIENT_4), list.ingredients[3])
        self.assertEqual(Ingredient(INGREDIENT_5), list.ingredients[4])
        self.assertEqual(Ingredient(INGREDIENT_6), list.ingredients[5])
        self.assertEqual(Ingredient(INGREDIENT_7), list.ingredients[6])
        self.assertEqual(Ingredient(INGREDIENT_8), list.ingredients[7])
        self.assertEqual(Ingredient(INGREDIENT_9), list.ingredients[8])
        self.assertEqual(Ingredient(INGREDIENT_10), list.ingredients[9])

    def test_update_list_file(self):
        list = IngredientList(filepath=TEST_LIST_UPDATE_FILEPATH)
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
        list = IngredientList(filepath=TEST_LIST_FILEPATH)
        self.assertEqual(JSON_TEST_LIST, list.get_json_object())

    def test_ingredient_already_exists(self):
        list = IngredientList()
        self.assertTrue(list.ingredient_already_exists(Ingredient(INGREDIENT_1)))

    def test_ingredient_doesnt_exists(self):
        list = IngredientList()
        self.assertFalse(list.ingredient_already_exists(Ingredient(INGREDIENT_11)))

    def test_get_ingredient_exists(self):
        list = IngredientList()
        self.assertEqual(INGREDIENT_1, list.get_ingredient("garlic").get_json_object())

    def test_get_ingredient_doesnt_exists(self):
        list = IngredientList()
        self.assertIsNone(list.get_ingredient(Ingredient(INGREDIENT_11)))

    def test_add_ingredient(self):
        list = IngredientList()
        list.add_ingredient(Ingredient(INGREDIENT_1))
        list.add_ingredient(Ingredient(INGREDIENT_2))
        list.add_ingredient(Ingredient(INGREDIENT_3))
        list.add_ingredient(Ingredient(INGREDIENT_4))
        list.add_ingredient(Ingredient(INGREDIENT_5))
        self.assertEqual(Ingredient(INGREDIENT_1), list.ingredients[0])
        self.assertEqual(Ingredient(INGREDIENT_2), list.ingredients[1])
        self.assertEqual(Ingredient(INGREDIENT_3), list.ingredients[2])
        self.assertEqual(Ingredient(INGREDIENT_4), list.ingredients[3])
        self.assertEqual(Ingredient(INGREDIENT_5), list.ingredients[4])

    def tearDown(self):
        if exists(EMPTY_TEST_LIST_FILEPATH):
            remove(EMPTY_TEST_LIST_FILEPATH)

        if exists(TEST_LIST_UPDATE_FILEPATH):
            remove(TEST_LIST_UPDATE_FILEPATH)

if __name__ == '__main__':
    unittest.main()