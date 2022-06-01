from os.path import exists
import json

from main.ingredients.ingredient import Ingredient

class IngredientList:
    def __init__(self, ingredients: list[Ingredient] = [], filepath: str = None):
        self.ingredients = ingredients
        self.filepath = filepath

        if filepath is not None:
            self.load_list_file(filepath)

    def load_list_file(self, filepath: str):
        self.filepath = filepath
        if not exists(filepath):
            self.update_list_file([])

        self.ingredients = []
        with open(filepath, 'r') as f:
            for ingredient in json.load(f):
                self.ingredients.append(Ingredient(ingredient))
            
    def ingredient_already_exists(self, ingredient_to_check: Ingredient) -> bool:
        ingredient_exists = False
        for ingredient in self.ingredients:
            if ingredient.name == ingredient_to_check.name:
                ingredient_exists = True
        return ingredient_exists

    def add_ingredient(self, new_ingredient: Ingredient):
        if not self.ingredient_already_exists(new_ingredient):
            self.ingredients.append(new_ingredient)
            self.update_list_file(self.get_json_object())

    def get_ingredient(self, ingredient_name: str) -> Ingredient:
        for ingredient in self.ingredients:
            if ingredient.name == ingredient_name:
                return ingredient
        return None

    def from_json_object(self, ingredients_json: list[dict[str, str]]):
        self.ingredients = []

        for ingredient in ingredients_json:
            self.add_ingredient(Ingredient(ingredient))

    def get_json_object(self) -> list[dict[str, str]]:
        ingredient_list = []
        for ingredient in self.ingredients:
            ingredient_list.append(ingredient.get_json_object())

        return ingredient_list

    def update_list_file(self, ingredients_json: list[dict[str, str]]):
        if hasattr(self, "filepath") and self.filepath is not None:
            with open(self.filepath, "w") as f:
                json.dump(ingredients_json, f)