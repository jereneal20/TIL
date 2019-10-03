
"""
Here is food order system.
Build a food order system which makes orders if customers choose their recipe.

customers first need to choose base: rice(1), noodle(2), beens.
and then they choose meat: beef(1), pork(2) ..
vegi
sauce

each item has price so after choose all things.
after choose all things you need to show total price.

"""

"""
- 1 customer -> 1 food
- 1 food -> multiple bases (which contains noodle ... all the ingredients)
 -> base/meat/vegi/sauce
    -> each ingredients have prices ( price will be added 4 or less things)
"""

    
class Catetory(Enum):
    BASE = 0
    MEAT = 1
    ..
    
    
class Recipe:
    list_of_ingredients = ["beef", "pork", "rice", ...]

class Ingredient:
    name
    expire_date
    price
    category
    amount
    ...
    def valid():
    
#class Base(Ingredient):
#    ...
#class Meat(Ingredient):
#    ...
    

class FoodOrderSystem:
    ingredient_dict = dict() # "beef" : Ingredient
    
	def order(self, recipe: Recipe) -> int:
        price = 0
        added_to_the_list = list()
        
        for ingredient_name in recipe.list_of_ingredients:
        	if ingredient_name not in self.ingredient_dict:
                raise Exception
            ingredient = self.ingredient_dict[ingredient_name]
            if not ingredient.valid():
                raise Exception
            if ingredient.__class__ in added_to_the_list:
#            isInstanceOf(added, ingredient) for added in added_to_the_list:
            ingredient.delete(1)
            price += ingredient.price
            
        return price
            
        

