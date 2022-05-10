# # First solution:
# dog_food_price = 2.50
# cat_food_price = 4.00
#
# quantity_dog_food = int(input())
# quantity_cat_food = int(input())
#
# total_price_dog_food = dog_food_price * quantity_dog_food
# total_price_cat_food = cat_food_price * quantity_cat_food
#
# total_price_all_food = total_price_dog_food + total_price_cat_food
# print(f'{total_price_all_food} lv.')
#
#
# # Second solution:
# #'''used function'''
# def food_costs(quantity_dog, quantity_cat, food_dog_price = 2.50, food_cat_price = 4.00):
#     res_dog = quantity_dog * food_dog_price
#     res_cat = quantity_cat * food_cat_price
#     res = res_dog + res_cat
#     return f'{res}lv.'
#
#
# food_1 = food_costs(5, 4)
# food_2 = food_costs(13, 9)
#
# print(food_1)
# print(food_2)


# Third solution:
# '''used class''
class FoodCosts:
    def __init__(self, dog_quantity, cat_quantity):
        self.dog_quantity = dog_quantity
        self.cat_quantity = cat_quantity
        self.food_dog_price = 2.50
        self.food_cat_price = 4

    def get_need_food_dog(self):
        need_food = self.dog_quantity * self.food_dog_price
        return need_food

    def get_need_food_cat(self):
        need_food = self.cat_quantity * self.food_cat_price
        return need_food

    def get_total_price_food(self):
        total = self.get_need_food_dog() + self.get_need_food_cat()
        return total


food1 = FoodCosts(5, 4)
res1 = food1.get_total_price_food()
print(f'{res1} lv.')

food2 = FoodCosts(13, 9)
res2 = food2.get_total_price_food()
print(f'{res2} lv.')

