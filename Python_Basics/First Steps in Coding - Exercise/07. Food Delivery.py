chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
delivery = 2.50

number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegetarian_menu = int(input())

sum_chicken_menu = chicken_menu * number_chicken_menu
sum_fish_menu = fish_menu * number_fish_menu
sum_vegetarian_menu = vegetarian_menu * number_vegetarian_menu

total_sum = sum_chicken_menu + sum_fish_menu + sum_vegetarian_menu
dessert = total_sum * 0.2

total_price = total_sum + dessert + delivery
print(total_price)
