from main.ingredients.ingredient import Ingredient


class Recipe:
    def __init__(self, recipe_json : dict[str, str, list[dict[dict[str, str], float]], list[str]] = {}):
        self.from_json_object(recipe_json)

    def from_json_object(self, recipe_json: dict[str, str, list[dict[dict[str, str], float]], list[str]]):
        if "name" in recipe_json:
            self.name = recipe_json["name"]
        if "steps" in recipe_json:
            self.steps = recipe_json["steps"]
        if "ingredients" in recipe_json:
            for entry in recipe_json["ingredients"]:
                self.add_ingredient(Ingredient(entry["ingredient"]), entry["amount"])
        if "duration_in_min" in recipe_json:
            self.duration_in_min = recipe_json["duration_in_min"]

    def get_json_object(self) -> dict[str, str, list[dict[dict[str, str], float]], list[str]]:
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
            "duration_in_min": self.duration_in_min
        }

    def add_name(self, name: str):
        self.name = name

    def add_step(self, step: str):
        if not hasattr(self, "steps"):
            self.steps = []

        self.steps.append(step)

    def add_ingredient(self, ingredient: Ingredient, amount: float):
        if not hasattr(self, "ingredients"):
            self.ingredients = []

        self.ingredients.append({
            "ingredient": ingredient, 
            "amount": amount
        })

    def add_duration_in_min(self, duration_in_min: int):
        self.duration_in_min = duration_in_min