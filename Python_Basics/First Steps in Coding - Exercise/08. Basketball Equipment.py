annual_fee = int(input())

price_sneakers = annual_fee - (annual_fee * 0.4)
outfit = price_sneakers - (price_sneakers * 0.2)
ball = outfit / 4
accessories = ball / 5

total_annual = annual_fee + price_sneakers + outfit + ball + accessories
print(total_annual)
