price_one_km = 7.61
landscaped_km = float(input())

all_price = landscaped_km * price_one_km
percent_discount = all_price * 0.18
total_price = all_price - percent_discount

print(f'The final price is: {total_price} lv.\nThe discount is: {percent_discount} lv.')
