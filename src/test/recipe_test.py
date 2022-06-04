import unittest
from main.ingredients.ingredient import Ingredient
from main.recipes.recipe import Recipe

TEST_NAME = "TEST_NAME"
TEST_DURATION = "TEST_DURATION"

TEST_STEPS = [
    "TEST STEP 1",
    "TEST STEP 2",
    "TEST STEP 3",
    "TEST STEP 4",
]

INGREDIENT_1 = {"name": "garlic", "unit": "clove"}
INGREDIENT_1_AMOUNT = 2

INGREDIENT_2 = {"name": "steak", "unit": "g"}
INGREDIENT_2_AMOUNT = 500

INGREDIENT_3 = {"name": "chicken", "unit": "mcx"}
INGREDIENT_3_AMOUNT = 3

INGREDIENT_4 = {"name": "pepper", "unit": "pinch"}
INGREDIENT_4_AMOUNT = 4

TEST_INGREDIENTS_AS_JSON_DICTS = [
    {"ingredient": INGREDIENT_1, "amount": INGREDIENT_1_AMOUNT},
    {"ingredient": INGREDIENT_2, "amount": INGREDIENT_2_AMOUNT},
    {"ingredient": INGREDIENT_3, "amount": INGREDIENT_3_AMOUNT},
    {"ingredient": INGREDIENT_4, "amount": INGREDIENT_4_AMOUNT}
]

JSON_OBJECT = {
    "name": TEST_NAME,
    "duration_in_min": TEST_DURATION,
    "steps": TEST_STEPS,
    "ingredients": TEST_INGREDIENTS_AS_JSON_DICTS
}

# TODO : find a way to put the amounts in the ingredient list object

def ingredient_compare(ingredient1, ingredient2, msg):
    return ingredient1.name == ingredient2.name and ingredient1.unit == ingredient2.unit

class TestIngredientMethods(unittest.TestCase):

    def setUp(self):
        self.addTypeEqualityFunc(Ingredient, ingredient_compare)

    def test_from_json_object(self):
        recipe = Recipe(JSON_OBJECT)
        self.assertEqual(TEST_NAME, recipe.name)
        self.assertEqual(TEST_DURATION, recipe.duration_in_min)
        self.assertEqual(TEST_STEPS, recipe.steps)
        self.assertEqual(Ingredient(INGREDIENT_1), recipe.ingredients[0]["ingredient"])
        self.assertEqual(INGREDIENT_1_AMOUNT, recipe.ingredients[0]["amount"])
        self.assertEqual(Ingredient(INGREDIENT_2), recipe.ingredients[1]["ingredient"])
        self.assertEqual(INGREDIENT_2_AMOUNT, recipe.ingredients[1]["amount"])
        self.assertEqual(Ingredient(INGREDIENT_3), recipe.ingredients[2]["ingredient"])
        self.assertEqual(INGREDIENT_3_AMOUNT, recipe.ingredients[2]["amount"])
        self.assertEqual(Ingredient(INGREDIENT_4), recipe.ingredients[3]["ingredient"])
        self.assertEqual(INGREDIENT_4_AMOUNT, recipe.ingredients[3]["amount"])

    def test_get_json_object(self):
        recipe = Recipe()
        recipe.add_name("TEST_NAME")
        recipe.add_duration_in_min("TEST_DURATION")
        recipe.add_step("TEST STEP 1")
        recipe.add_step("TEST STEP 2")
        recipe.add_step("TEST STEP 3")
        recipe.add_step("TEST STEP 4")
        recipe.add_ingredient(Ingredient(INGREDIENT_1), INGREDIENT_1_AMOUNT)
        recipe.add_ingredient(Ingredient(INGREDIENT_2), INGREDIENT_2_AMOUNT)
        recipe.add_ingredient(Ingredient(INGREDIENT_3), INGREDIENT_3_AMOUNT)
        recipe.add_ingredient(Ingredient(INGREDIENT_4), INGREDIENT_4_AMOUNT)
        self.assertEqual(JSON_OBJECT, recipe.get_json_object())

    def test_add_name(self):
        recipe = Recipe()
        recipe.add_name(TEST_NAME)
        self.assertEqual(TEST_NAME, recipe.name)

    def test_add_duration(self):
        recipe = Recipe()
        recipe.add_duration_in_min(TEST_DURATION)
        self.assertEqual(TEST_DURATION, recipe.duration_in_min)

    def test_add_step(self):
        recipe = Recipe()
        recipe.add_step("TEST STEP 1")
        recipe.add_step("TEST STEP 2")
        recipe.add_step("TEST STEP 3")
        recipe.add_step("TEST STEP 4")
        self.assertEqual(TEST_STEPS, recipe.steps)

    def test_add_ingredient(self):
        recipe = Recipe()
        recipe.add_ingredient(Ingredient(INGREDIENT_1), INGREDIENT_1_AMOUNT)
        recipe.add_ingredient(Ingredient(INGREDIENT_2), INGREDIENT_2_AMOUNT)
        recipe.add_ingredient(Ingredient(INGREDIENT_3), INGREDIENT_3_AMOUNT)
        recipe.add_ingredient(Ingredient(INGREDIENT_4), INGREDIENT_4_AMOUNT)
        self.assertEqual(Ingredient(INGREDIENT_1), recipe.ingredients[0]["ingredient"])
        self.assertEqual(INGREDIENT_1_AMOUNT, recipe.ingredients[0]["amount"])
        self.assertEqual(Ingredient(INGREDIENT_2), recipe.ingredients[1]["ingredient"])
        self.assertEqual(INGREDIENT_2_AMOUNT, recipe.ingredients[1]["amount"])
        self.assertEqual(Ingredient(INGREDIENT_3), recipe.ingredients[2]["ingredient"])
        self.assertEqual(INGREDIENT_3_AMOUNT, recipe.ingredients[2]["amount"])
        self.assertEqual(Ingredient(INGREDIENT_4), recipe.ingredients[3]["ingredient"])
        self.assertEqual(INGREDIENT_4_AMOUNT, recipe.ingredients[3]["amount"])

if __name__ == '__main__':
    unittest.main()