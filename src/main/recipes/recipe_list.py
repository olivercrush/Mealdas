from os.path import exists
import json

RECIPES_PATH = "res/recipes.json"

class RecipeList:
    def __init__(self):
        self.list = self.load_list_file()
        pass

    def load_list_file(self):
        if not exists(RECIPES_PATH):
            empty_list = {
                "recipes": []
            }
            self.update_list_file(empty_list)

        with open(RECIPES_PATH, 'r') as f:
            return json.load(f)
            
    def update_list_file(self, json_dictionnary):
        with open(RECIPES_PATH, "w") as f:
            json.dump(json_dictionnary, f)

    def add_recipe(self, recipe):
        if self.list["recipes"].count(recipe) == 0:
            self.list["recipes"].append(recipe)
            self.update_list_file(self.list)

    def get_recipe_list(self):
        return self.list