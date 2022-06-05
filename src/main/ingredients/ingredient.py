class Ingredient:
    def __init__(self, ingredient_json: dict[str, str] = {}):
        self.from_json_object(ingredient_json)

    def from_json_object(self, ingredient_json: dict[str, str]):
        if "name" in ingredient_json:
            self.name = ingredient_json["name"]
        if "unit" in ingredient_json:
            self.unit = ingredient_json["unit"]

    def get_json_object(self) -> dict[str, str]:
        return {
            "name": self.name,
            "unit": self.unit
        }

    def add_name(self, name: str):
        self.name = name

    def add_unit(self, unit: str):
        self.unit = unit

    def is_valid(self) -> bool:
        return hasattr(self, "name") and hasattr(self, "unit")

def ingredient_compare(ingredient1: Ingredient, ingredient2: Ingredient, msg: str = ""):
    return ingredient1.name == ingredient2.name and ingredient1.unit == ingredient2.unit

    