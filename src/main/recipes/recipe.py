from main.ingredients.ingredient import Ingredient


class Recipe:
    def __init__(self, recipe_json={}):
        self.from_json_object(recipe_json)

    def from_json_object(self, recipe_json):
        if "name" in recipe_json:
            self.name = recipe_json["name"]
        if "steps" in recipe_json:
            self.steps = recipe_json["steps"]
        if "ingredients" in recipe_json:
            for entry in recipe_json["ingredients"]:
                self.add_ingredient(Ingredient(entry["ingredient"]), entry["amount"])
        if "duration" in recipe_json:
            self.duration = recipe_json["duration"]

    def get_json_object(self):
        json_ingredients = []
        for entry in self.ingredients:
            json_ingredients.append({
                "ingredient": entry["ingredient"].get_json_object(),
                "amount": entry["amount"]
            })

        return {
            "name": self.name,
            "steps": self.steps,
            "ingredients": json_ingredients,
            "duration": self.duration
        }

    def add_name(self, name):
        self.name = name

    def add_step(self, step):
        if not hasattr(self, "steps"):
            self.steps = []

        self.steps.append(step)

    def add_ingredient(self, ingredient, amount):
        if not hasattr(self, "ingredients"):
            self.ingredients = []

        self.ingredients.append({
            "ingredient": ingredient, 
            "amount": amount
        })

    def add_duration(self, duration):
        self.duration = duration