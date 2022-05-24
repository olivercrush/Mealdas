from os.path import exists
import json

from main.ingredients.ingredient import Ingredient

class IngredientList:
    def __init__(self, filepath):
        self.filepath = filepath
        self.ingredients = []
        self.load_list_file()
        pass

    def load_list_file(self):
        if not exists(self.filepath):
            empty_list = {
                "ingredients": []
            }
            self.update_list_file(empty_list)

        with open(self.filepath, 'r') as f:
            for ingredient in json.load(f)["ingredients"]:
                self.ingredients.append(Ingredient(ingredient))
            
    def ingredient_already_exists(self, ingredient_to_check):
        ingredient_exists = False
        for ingredient in self.ingredients:
            if ingredient.name == ingredient_to_check.name:
                ingredient_exists = True
        return ingredient_exists

    def add_ingredient(self, new_ingredient):
        if not self.ingredient_already_exists(new_ingredient):
            self.ingredients.append(new_ingredient)
            self.update_list_file(self.get_json_object())

    def get_json_object(self):
        json_object = {
            "ingredients": []
        }

        for ingredient in self.ingredients:
            json_object["ingredients"].append(ingredient.get_json_object())

        return json_object

    def update_list_file(self, ingredients_json):
        with open(self.filepath, "w") as f:
            json.dump(ingredients_json, f)