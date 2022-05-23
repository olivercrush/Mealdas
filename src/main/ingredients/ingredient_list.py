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
            
    def update_list_file(self, json_dictionnary):
        with open(self.filepath, "w") as f:
            json.dump(json_dictionnary, f)

    def add_ingredient(self, ingredient):
        if self.list["ingredients"].count(ingredient.get()) == 0:
            self.list["ingredients"].append(ingredient.get())
            self.update_list_file(self.list)

    def get_ingredient_list(self):
        return self.list

    def get_ingredient(self, ingredient_name):
        for ingredient in self.list:
            if ingredient["name"] == ingredient_name:
                return ingredient