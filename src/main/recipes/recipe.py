class Recipe:
    def __init__(self):
        pass

    def add_name(self, name):
        self.name = name

    def add_ingredient(self, ingredient, amount):
        if self.ingredients is None:
            self.ingredients = []