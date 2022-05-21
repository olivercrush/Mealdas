from ingredients import Ingredients

ingredients = Ingredients()
print(ingredients.get_ingredient_list())
ingredients.add_ingredient("garlic")
ingredients.add_ingredient("steak")
ingredients.add_ingredient("chicken")
ingredients.add_ingredient("pasta")
print(ingredients.get_ingredient_list())