from main.ingredients.ingredient import Ingredient
from main.ingredients.ingredient_list import IngredientList

class IngredientListWithAmount(IngredientList):
    def __init__(self, ingredients: list[Ingredient] = [], amounts: list[float] = []):
        super().__init__(ingredients)
        self.amounts = amounts

    def add_ingredient(self, new_ingredient: Ingredient, amount: float):
        if not self.ingredient_already_exists(new_ingredient):
            self.ingredients.append(new_ingredient)
            self.amounts.append(amount)

    def get_ingredient_with_amount(self, ingredient_name: str) -> tuple[Ingredient, float]:
        for ingredient in self.ingredients:
            if ingredient.name == ingredient_name:
                return (ingredient, self.amounts[self.ingredients.index(ingredient)])
        return None

    def from_json_object(self, ingredients_json: list[dict[dict[str, str], float]]):
        self.ingredients = []

        for entry in ingredients_json:
            self.add_ingredient(Ingredient(entry["ingredient"]), entry["amount"])

    def get_json_object(self) -> list[dict[dict[str, str], float]]:
        ingredient_list = []
        for ingredient in self.ingredients:
            ingredient_list.append({"ingredient": ingredient.get_json_object(), "amount": self.amounts[self.ingredients.index(ingredient)]})

        return ingredient_list