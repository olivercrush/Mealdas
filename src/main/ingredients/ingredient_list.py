from os.path import exists
import json

INGREDIENTS_PATH = "res/ingredients.json"

class IngredientList:
    def __init__(self):
        self.list = self.load_list_file()
        pass

    def load_list_file(self):
        if not exists(INGREDIENTS_PATH):
            empty_list = {
                "ingredients": []
            }
            self.update_list_file(empty_list)

        with open(INGREDIENTS_PATH, 'r') as f:
            return json.load(f)
            
    def update_list_file(self, json_dictionnary):
        with open(INGREDIENTS_PATH, "w") as f:
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