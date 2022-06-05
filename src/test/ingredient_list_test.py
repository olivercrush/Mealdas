import unittest
import test_scenarios

from os.path import exists
from os import remove
import json

from main.ingredients.ingredient import Ingredient
from main.ingredients.ingredient_list import IngredientList

def ingredient_compare(ingredient1, ingredient2, msg):
    return ingredient1.name == ingredient2.name and ingredient1.unit == ingredient2.unit

class TestIngredientListMethods(unittest.TestCase):

    def setUp(self):
        self.addTypeEqualityFunc(Ingredient, ingredient_compare)

    def test_load_list_file(self):
        list = IngredientList()
        list.load_list_file(test_scenarios.TEST_LIST_FILEPATH)
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_1), list.ingredients[0])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_2), list.ingredients[1])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_3), list.ingredients[2])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_4), list.ingredients[3])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_5), list.ingredients[4])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_6), list.ingredients[5])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_7), list.ingredients[6])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_8), list.ingredients[7])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_9), list.ingredients[8])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_10), list.ingredients[9])

    def test_update_list_file(self):
        list = IngredientList(filepath=test_scenarios.TEST_LIST_UPDATE_FILEPATH)
        list.add_ingredient(Ingredient(test_scenarios.INGREDIENT_1))
        list.add_ingredient(Ingredient(test_scenarios.INGREDIENT_2))
        list.add_ingredient(Ingredient(test_scenarios.INGREDIENT_3))
        list.add_ingredient(Ingredient(test_scenarios.INGREDIENT_4))
        list.add_ingredient(Ingredient(test_scenarios.INGREDIENT_5))
        list.add_ingredient(Ingredient(test_scenarios.INGREDIENT_6))
        list.add_ingredient(Ingredient(test_scenarios.INGREDIENT_7))
        list.add_ingredient(Ingredient(test_scenarios.INGREDIENT_8))
        list.add_ingredient(Ingredient(test_scenarios.INGREDIENT_9))
        list.add_ingredient(Ingredient(test_scenarios.INGREDIENT_10))
        
        with open(test_scenarios.TEST_LIST_UPDATE_FILEPATH, 'r') as f:
            self.assertEqual(test_scenarios.INGREDIENT_LIST_JSON, json.load(f))

    def test_get_json_object(self):
        list = IngredientList(filepath=test_scenarios.TEST_LIST_FILEPATH)
        self.assertEqual(test_scenarios.INGREDIENT_LIST_JSON, list.get_json_object())

    def test_ingredient_already_exists(self):
        list = IngredientList()
        self.assertTrue(list.ingredient_already_exists(Ingredient(test_scenarios.INGREDIENT_1)))

    def test_ingredient_doesnt_exists(self):
        list = IngredientList()
        self.assertFalse(list.ingredient_already_exists(Ingredient(test_scenarios.INGREDIENT_11)))

    def test_get_ingredient_exists(self):
        list = IngredientList()
        self.assertEqual(test_scenarios.INGREDIENT_1, list.get_ingredient(test_scenarios.INGREDIENT_1["name"]).get_json_object())

    def test_get_ingredient_doesnt_exists(self):
        list = IngredientList()
        self.assertIsNone(list.get_ingredient(Ingredient(test_scenarios.INGREDIENT_11)))

    def test_add_ingredient(self):
        list = IngredientList()
        list.add_ingredient(Ingredient(test_scenarios.INGREDIENT_1))
        list.add_ingredient(Ingredient(test_scenarios.INGREDIENT_2))
        list.add_ingredient(Ingredient(test_scenarios.INGREDIENT_3))
        list.add_ingredient(Ingredient(test_scenarios.INGREDIENT_4))
        list.add_ingredient(Ingredient(test_scenarios.INGREDIENT_5))
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_1), list.ingredients[0])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_2), list.ingredients[1])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_3), list.ingredients[2])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_4), list.ingredients[3])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_5), list.ingredients[4])

    def tearDown(self):
        if exists(test_scenarios.EMPTY_TEST_LIST_FILEPATH):
            remove(test_scenarios.EMPTY_TEST_LIST_FILEPATH)

        if exists(test_scenarios.TEST_LIST_UPDATE_FILEPATH):
            remove(test_scenarios.TEST_LIST_UPDATE_FILEPATH)

if __name__ == '__main__':
    unittest.main()