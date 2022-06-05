from main.ingredients.ingredient import Ingredient

# FILES
EMPTY_TEST_LIST_FILEPATH = "test/res/test.json"
TEST_LIST_FILEPATH = "test/res/ingredients.json"
TEST_LIST_UPDATE_FILEPATH = "test/res/ingredients_update.json"

# STRINGS
TEST_NAME = "TEST_NAME"
TEST_DURATION = "TEST_DURATION"
TEST_UNIT = "TEST_UNIT"

STEP_1 = "TEST STEP 1"
STEP_2 = "TEST STEP 2"
STEP_3 = "TEST STEP 3"
STEP_4 = "TEST STEP 4"

TEST_STEPS = [
    STEP_1,
    STEP_2,
    STEP_3,
    STEP_4,
]

# INGREDIENTS
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

# JSON DICTS AND LISTS
INGREDIENT_JSON_DICT = {
    "name": TEST_NAME,
    "unit": TEST_UNIT
}

INGREDIENT_WITH_AMOUNT_LIST_FOR_RECIPE_JSON = [
    {"ingredient": INGREDIENT_1, "amount": AMOUNT_1},
    {"ingredient": INGREDIENT_2, "amount": AMOUNT_2},
    {"ingredient": INGREDIENT_3, "amount": AMOUNT_3},
    {"ingredient": INGREDIENT_4, "amount": AMOUNT_4}
]

RECIPE_JSON_DICT = {
    "name": TEST_NAME,
    "duration_in_min": TEST_DURATION,
    "steps": TEST_STEPS,
    "ingredients": INGREDIENT_WITH_AMOUNT_LIST_FOR_RECIPE_JSON
}

INGREDIENT_WITH_AMOUNT_LIST_JSON = [
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

INGREDIENT_LIST_JSON = [
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

# OBJECT LISTS
INGREDIENT_AS_OBJECT_LIST = [
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

AMOUNT_LIST = [
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