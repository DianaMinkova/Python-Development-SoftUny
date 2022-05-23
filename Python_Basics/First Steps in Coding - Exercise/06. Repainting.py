protect_price = 1.50
paint_price = 14.50
diluent_price = 5.00
bags_price = 0.40

quantity_protect = int(input())
quantity_paint = int(input())
quantity_diluent = int(input())
hour_of_work = int(input())

incase_protect = 2
incase_paint = quantity_paint * 0.1

protect = (quantity_protect + incase_protect) * protect_price
paint = (quantity_paint + incase_paint) * paint_price
quantity = quantity_diluent * diluent_price

sum_materials = protect + paint + quantity + bags_price
cost_work = (sum_materials * 0.3) * hour_of_work

print(sum_materials + cost_work)

