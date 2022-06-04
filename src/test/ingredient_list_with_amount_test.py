import unittest

from main.ingredients.ingredient import Ingredient
from main.ingredients.ingredient_list import IngredientList
from main.ingredients.ingredient_list_with_amount import IngredientListWithAmount

INGREDIENT_1 = {"name": "garlic", "unit": "clove"}
AMOUNT_1 = 3
INGREDIENT_2 = {"name": "steak", "unit": "g"}
AMOUNT_2 = 250
INGREDIENT_3 = {"name": "chicken", "unit": "mcx"}
AMOUNT_3 = 5
INGREDIENT_4 = {"name": "pepper", "unit": "pinch"}
AMOUNT_4 = 2.5
INGREDIENT_5 = {"name": "pasta", "unit": "g"}
AMOUNT_5 = 500
INGREDIENT_6 = {"name": "zuchini", "unit": "mcx"}
AMOUNT_6 = 2
INGREDIENT_7 = {"name": "tomato", "unit": "mcx"}
AMOUNT_7 = 3
INGREDIENT_8 = {"name": "rice", "unit": "g"}
AMOUNT_8 = 1000
INGREDIENT_9 = {"name": "lentils", "unit": "g"}
AMOUNT_9 = 200
INGREDIENT_10 = {"name": "potato", "unit": "mcx"}
AMOUNT_10 = 2.5
INGREDIENT_11 = {"name": "onion", "unit": "mcx"}
AMOUNT_11 = 0.5

INGREDIENT_TEST_LIST = [
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

AMOUNT_TEST_LIST = [
    AMOUNT_1,
    AMOUNT_2,
    AMOUNT_3,
    AMOUNT_4,
    AMOUNT_5,
    AMOUNT_6,
    AMOUNT_7,
    AMOUNT_8,
    AMOUNT_9,
    AMOUNT_10
]

JSON_LIST = [
    {"ingredient": INGREDIENT_1, "amount": AMOUNT_1},
    {"ingredient": INGREDIENT_2, "amount": AMOUNT_2},
    {"ingredient": INGREDIENT_3, "amount": AMOUNT_3},
    {"ingredient": INGREDIENT_4, "amount": AMOUNT_4},
    {"ingredient": INGREDIENT_5, "amount": AMOUNT_5},
    {"ingredient": INGREDIENT_6, "amount": AMOUNT_6},
    {"ingredient": INGREDIENT_7, "amount": AMOUNT_7},
    {"ingredient": INGREDIENT_8, "amount": AMOUNT_8},
    {"ingredient": INGREDIENT_9, "amount": AMOUNT_9},
    {"ingredient": INGREDIENT_10, "amount": AMOUNT_10}
]

def ingredient_compare(ingredient1, ingredient2, msg):
    return ingredient1.name == ingredient2.name and ingredient1.unit == ingredient2.unit

class TestIngredientListWithAmountMethods(unittest.TestCase):

    def setUp(self):
        self.addTypeEqualityFunc(Ingredient, ingredient_compare)

    def test_from_json_object(self):
        ingredientList = IngredientListWithAmount()
        ingredientList.from_json_object(JSON_LIST)
        self.assertEqual(Ingredient(INGREDIENT_1), ingredientList.ingredients[0])
        self.assertEqual(AMOUNT_1, ingredientList.amounts[0])
        self.assertEqual(Ingredient(INGREDIENT_2), ingredientList.ingredients[1])
        self.assertEqual(AMOUNT_2, ingredientList.amounts[1])
        self.assertEqual(Ingredient(INGREDIENT_3), ingredientList.ingredients[2])
        self.assertEqual(AMOUNT_3, ingredientList.amounts[2])
        self.assertEqual(Ingredient(INGREDIENT_4), ingredientList.ingredients[3])
        self.assertEqual(AMOUNT_4, ingredientList.amounts[3])
        self.assertEqual(Ingredient(INGREDIENT_5), ingredientList.ingredients[4])
        self.assertEqual(AMOUNT_5, ingredientList.amounts[4])
        self.assertEqual(Ingredient(INGREDIENT_6), ingredientList.ingredients[5])
        self.assertEqual(AMOUNT_6, ingredientList.amounts[5])
        self.assertEqual(Ingredient(INGREDIENT_7), ingredientList.ingredients[6])
        self.assertEqual(AMOUNT_7, ingredientList.amounts[6])
        self.assertEqual(Ingredient(INGREDIENT_8), ingredientList.ingredients[7])
        self.assertEqual(AMOUNT_8, ingredientList.amounts[7])
        self.assertEqual(Ingredient(INGREDIENT_9), ingredientList.ingredients[8])
        self.assertEqual(AMOUNT_9, ingredientList.amounts[8])
        self.assertEqual(Ingredient(INGREDIENT_10), ingredientList.ingredients[9])
        self.assertEqual(AMOUNT_10, ingredientList.amounts[9])

    def test_get_json_object(self):
        ingredientList = IngredientListWithAmount(INGREDIENT_TEST_LIST, AMOUNT_TEST_LIST)
        self.assertEqual(JSON_LIST, ingredientList.get_json_object())


    def test_add_ingredient(self):
        ingredientList = IngredientListWithAmount()
        ingredientList.add_ingredient(Ingredient(INGREDIENT_1), AMOUNT_1)
        ingredientList.add_ingredient(Ingredient(INGREDIENT_2), AMOUNT_2)
        ingredientList.add_ingredient(Ingredient(INGREDIENT_3), AMOUNT_3)
        ingredientList.add_ingredient(Ingredient(INGREDIENT_4), AMOUNT_4)
        ingredientList.add_ingredient(Ingredient(INGREDIENT_5), AMOUNT_5)
        ingredientList.add_ingredient(Ingredient(INGREDIENT_6), AMOUNT_6)
        ingredientList.add_ingredient(Ingredient(INGREDIENT_7), AMOUNT_7)
        ingredientList.add_ingredient(Ingredient(INGREDIENT_8), AMOUNT_8)
        ingredientList.add_ingredient(Ingredient(INGREDIENT_9), AMOUNT_9)
        ingredientList.add_ingredient(Ingredient(INGREDIENT_10), AMOUNT_10)
        ingredientList.add_ingredient(Ingredient(INGREDIENT_11), AMOUNT_11)
        self.assertEqual(Ingredient(INGREDIENT_1), ingredientList.ingredients[0])
        self.assertEqual(AMOUNT_1, ingredientList.amounts[0])
        self.assertEqual(Ingredient(INGREDIENT_2), ingredientList.ingredients[1])
        self.assertEqual(AMOUNT_2, ingredientList.amounts[1])
        self.assertEqual(Ingredient(INGREDIENT_3), ingredientList.ingredients[2])
        self.assertEqual(AMOUNT_3, ingredientList.amounts[2])
        self.assertEqual(Ingredient(INGREDIENT_4), ingredientList.ingredients[3])
        self.assertEqual(AMOUNT_4, ingredientList.amounts[3])
        self.assertEqual(Ingredient(INGREDIENT_5), ingredientList.ingredients[4])
        self.assertEqual(AMOUNT_5, ingredientList.amounts[4])
        self.assertEqual(Ingredient(INGREDIENT_6), ingredientList.ingredients[5])
        self.assertEqual(AMOUNT_6, ingredientList.amounts[5])
        self.assertEqual(Ingredient(INGREDIENT_7), ingredientList.ingredients[6])
        self.assertEqual(AMOUNT_7, ingredientList.amounts[6])
        self.assertEqual(Ingredient(INGREDIENT_8), ingredientList.ingredients[7])
        self.assertEqual(AMOUNT_8, ingredientList.amounts[7])
        self.assertEqual(Ingredient(INGREDIENT_9), ingredientList.ingredients[8])
        self.assertEqual(AMOUNT_9, ingredientList.amounts[8])
        self.assertEqual(Ingredient(INGREDIENT_10), ingredientList.ingredients[9])
        self.assertEqual(AMOUNT_10, ingredientList.amounts[9])
        self.assertEqual(Ingredient(INGREDIENT_11), ingredientList.ingredients[10])
        self.assertEqual(AMOUNT_11, ingredientList.amounts[10])

    def test_get_ingredient_with_amount(self):
        ingredientList = IngredientListWithAmount(INGREDIENT_TEST_LIST, AMOUNT_TEST_LIST)
        self.assertEqual(Ingredient(INGREDIENT_1), ingredientList.get_ingredient_with_amount(INGREDIENT_1["name"])[0])
        self.assertEqual(AMOUNT_1, ingredientList.get_ingredient_with_amount(INGREDIENT_1["name"])[1])
        self.assertEqual(Ingredient(INGREDIENT_2), ingredientList.get_ingredient_with_amount(INGREDIENT_2["name"])[0])
        self.assertEqual(AMOUNT_2, ingredientList.get_ingredient_with_amount(INGREDIENT_2["name"])[1])
        self.assertEqual(Ingredient(INGREDIENT_3), ingredientList.get_ingredient_with_amount(INGREDIENT_3["name"])[0])
        self.assertEqual(AMOUNT_3, ingredientList.get_ingredient_with_amount(INGREDIENT_3["name"])[1])
        self.assertEqual(Ingredient(INGREDIENT_4), ingredientList.get_ingredient_with_amount(INGREDIENT_4["name"])[0])
        self.assertEqual(AMOUNT_4, ingredientList.get_ingredient_with_amount(INGREDIENT_4["name"])[1])
        self.assertEqual(Ingredient(INGREDIENT_5), ingredientList.get_ingredient_with_amount(INGREDIENT_5["name"])[0])
        self.assertEqual(AMOUNT_5, ingredientList.get_ingredient_with_amount(INGREDIENT_5["name"])[1])
        self.assertEqual(Ingredient(INGREDIENT_6), ingredientList.get_ingredient_with_amount(INGREDIENT_6["name"])[0])
        self.assertEqual(AMOUNT_6, ingredientList.get_ingredient_with_amount(INGREDIENT_6["name"])[1])
        self.assertEqual(Ingredient(INGREDIENT_7), ingredientList.get_ingredient_with_amount(INGREDIENT_7["name"])[0])
        self.assertEqual(AMOUNT_7, ingredientList.get_ingredient_with_amount(INGREDIENT_7["name"])[1])
        self.assertEqual(Ingredient(INGREDIENT_8), ingredientList.get_ingredient_with_amount(INGREDIENT_8["name"])[0])
        self.assertEqual(AMOUNT_8, ingredientList.get_ingredient_with_amount(INGREDIENT_8["name"])[1])
        self.assertEqual(Ingredient(INGREDIENT_9), ingredientList.get_ingredient_with_amount(INGREDIENT_9["name"])[0])
        self.assertEqual(AMOUNT_9, ingredientList.get_ingredient_with_amount(INGREDIENT_9["name"])[1])
        self.assertEqual(Ingredient(INGREDIENT_10), ingredientList.get_ingredient_with_amount(INGREDIENT_10["name"])[0])
        self.assertEqual(AMOUNT_10, ingredientList.get_ingredient_with_amount(INGREDIENT_10["name"])[1])