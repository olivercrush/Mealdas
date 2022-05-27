class Ingredient:
    def __init__(self, ingredient_json={}):
        self.from_json_object(ingredient_json)

    def from_json_object(self, ingredient_json):
        if "name" in ingredient_json:
            self.name = ingredient_json["name"]
        if "unit" in ingredient_json:
            self.unit = ingredient_json["unit"]

    def get_json_object(self):
        return {
            "name": self.name,
            "unit": self.unit
        }

    def add_name(self, name):
        self.name = name

    def add_unit(self, unit):
        self.unit = unit

    def is_valid(self):
        return hasattr(self, "name") and hasattr(self, "unit")

    