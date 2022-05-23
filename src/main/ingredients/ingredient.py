class Ingredient:
    def __init__(self):
        pass

    @classmethod
    def from_json_object(self, ingredient_json):
        self.add_name(ingredient_json["name"])
        self.add_unit(ingredient_json["unit"])

    def add_name(self, name):
        self.name = name

    def add_unit(self, unit):
        self.unit = unit

    def is_valid(self):
        return hasattr(self, "name") and hasattr(self, "unit")

    def get_json_object(self):
        return self.ingredient