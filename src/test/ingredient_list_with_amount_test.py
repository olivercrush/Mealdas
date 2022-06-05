import unittest
import test_scenarios

from main.ingredients.ingredient import Ingredient
from main.ingredients.ingredient_list import IngredientList
from main.ingredients.ingredient_list_with_amount import IngredientListWithAmount

def ingredient_compare(ingredient1, ingredient2, msg):
    return ingredient1.name == ingredient2.name and ingredient1.unit == ingredient2.unit

class TestIngredientListWithAmountMethods(unittest.TestCase):

    def setUp(self):
        self.addTypeEqualityFunc(Ingredient, ingredient_compare)

    def test_from_json_object(self):
        ingredientList = IngredientListWithAmount()
        ingredientList.from_json_object(test_scenarios.INGREDIENT_WITH_AMOUNT_LIST_JSON)
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_1), ingredientList.ingredients[0])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_2), ingredientList.ingredients[1])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_3), ingredientList.ingredients[2])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_4), ingredientList.ingredients[3])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_5), ingredientList.ingredients[4])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_6), ingredientList.ingredients[5])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_7), ingredientList.ingredients[6])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_8), ingredientList.ingredients[7])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_9), ingredientList.ingredients[8])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_10), ingredientList.ingredients[9])
        self.assertEqual(test_scenarios.AMOUNT_1, ingredientList.amounts[0])
        self.assertEqual(test_scenarios.AMOUNT_2, ingredientList.amounts[1])
        self.assertEqual(test_scenarios.AMOUNT_3, ingredientList.amounts[2])
        self.assertEqual(test_scenarios.AMOUNT_4, ingredientList.amounts[3])
        self.assertEqual(test_scenarios.AMOUNT_5, ingredientList.amounts[4])
        self.assertEqual(test_scenarios.AMOUNT_6, ingredientList.amounts[5])
        self.assertEqual(test_scenarios.AMOUNT_7, ingredientList.amounts[6])
        self.assertEqual(test_scenarios.AMOUNT_8, ingredientList.amounts[7])
        self.assertEqual(test_scenarios.AMOUNT_9, ingredientList.amounts[8])
        self.assertEqual(test_scenarios.AMOUNT_10, ingredientList.amounts[9])

    def test_get_json_object(self):
        ingredientList = IngredientListWithAmount(test_scenarios.INGREDIENT_AS_OBJECT_LIST, test_scenarios.AMOUNT_LIST)
        self.assertEqual(test_scenarios.INGREDIENT_WITH_AMOUNT_LIST_JSON, ingredientList.get_json_object())

    def test_add_ingredient(self):
        ingredientList = IngredientListWithAmount()
        ingredientList.add_ingredient(Ingredient(test_scenarios.INGREDIENT_1), test_scenarios.AMOUNT_1)
        ingredientList.add_ingredient(Ingredient(test_scenarios.INGREDIENT_2), test_scenarios.AMOUNT_2)
        ingredientList.add_ingredient(Ingredient(test_scenarios.INGREDIENT_3), test_scenarios.AMOUNT_3)
        ingredientList.add_ingredient(Ingredient(test_scenarios.INGREDIENT_4), test_scenarios.AMOUNT_4)
        ingredientList.add_ingredient(Ingredient(test_scenarios.INGREDIENT_5), test_scenarios.AMOUNT_5)
        ingredientList.add_ingredient(Ingredient(test_scenarios.INGREDIENT_6), test_scenarios.AMOUNT_6)
        ingredientList.add_ingredient(Ingredient(test_scenarios.INGREDIENT_7), test_scenarios.AMOUNT_7)
        ingredientList.add_ingredient(Ingredient(test_scenarios.INGREDIENT_8), test_scenarios.AMOUNT_8)
        ingredientList.add_ingredient(Ingredient(test_scenarios.INGREDIENT_9), test_scenarios.AMOUNT_9)
        ingredientList.add_ingredient(Ingredient(test_scenarios.INGREDIENT_10),test_scenarios.AMOUNT_10)
        ingredientList.add_ingredient(Ingredient(test_scenarios.INGREDIENT_11),test_scenarios.AMOUNT_11)
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_1), ingredientList.ingredients[0])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_2), ingredientList.ingredients[1])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_3), ingredientList.ingredients[2])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_4), ingredientList.ingredients[3])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_5), ingredientList.ingredients[4])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_6), ingredientList.ingredients[5])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_7), ingredientList.ingredients[6])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_8), ingredientList.ingredients[7])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_9), ingredientList.ingredients[8])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_10), ingredientList.ingredients[9])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_11), ingredientList.ingredients[10])
        self.assertEqual(test_scenarios.AMOUNT_1, ingredientList.amounts[0])
        self.assertEqual(test_scenarios.AMOUNT_2, ingredientList.amounts[1])
        self.assertEqual(test_scenarios.AMOUNT_3, ingredientList.amounts[2])
        self.assertEqual(test_scenarios.AMOUNT_4, ingredientList.amounts[3])
        self.assertEqual(test_scenarios.AMOUNT_5, ingredientList.amounts[4])
        self.assertEqual(test_scenarios.AMOUNT_6, ingredientList.amounts[5])
        self.assertEqual(test_scenarios.AMOUNT_7, ingredientList.amounts[6])
        self.assertEqual(test_scenarios.AMOUNT_8, ingredientList.amounts[7])
        self.assertEqual(test_scenarios.AMOUNT_9, ingredientList.amounts[8])
        self.assertEqual(test_scenarios.AMOUNT_10, ingredientList.amounts[9])
        self.assertEqual(test_scenarios.AMOUNT_11, ingredientList.amounts[10])

    def test_get_ingredient_with_amount(self):
        ingredientList = IngredientListWithAmount(test_scenarios.INGREDIENT_AS_OBJECT_LIST, test_scenarios.AMOUNT_LIST)
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_1), ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_1["name"])[0])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_2), ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_2["name"])[0])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_3), ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_3["name"])[0])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_4), ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_4["name"])[0])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_5), ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_5["name"])[0])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_6), ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_6["name"])[0])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_7), ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_7["name"])[0])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_8), ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_8["name"])[0])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_9), ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_9["name"])[0])
        self.assertEqual(Ingredient(test_scenarios.INGREDIENT_10), ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_10["name"])[0])
        self.assertEqual(test_scenarios.AMOUNT_1, ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_1["name"])[1])
        self.assertEqual(test_scenarios.AMOUNT_2, ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_2["name"])[1])
        self.assertEqual(test_scenarios.AMOUNT_3, ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_3["name"])[1])
        self.assertEqual(test_scenarios.AMOUNT_4, ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_4["name"])[1])
        self.assertEqual(test_scenarios.AMOUNT_5, ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_5["name"])[1])
        self.assertEqual(test_scenarios.AMOUNT_6, ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_6["name"])[1])
        self.assertEqual(test_scenarios.AMOUNT_7, ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_7["name"])[1])
        self.assertEqual(test_scenarios.AMOUNT_8, ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_8["name"])[1])
        self.assertEqual(test_scenarios.AMOUNT_9, ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_9["name"])[1])
        self.assertEqual(test_scenarios.AMOUNT_10, ingredientList.get_ingredient_with_amount(test_scenarios.INGREDIENT_10["name"])[1])