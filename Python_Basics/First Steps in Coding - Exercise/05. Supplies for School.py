# # First solution:
# pens_price = 5.80
# markers_price = 7.20
# detergent_price = 1.20
#
# pens_num = int(input())
# markers_num = int(input())
# detergent_l = int(input())
#percent_discount = int(input()) / 100
#
# panns = pens_num * pens_price
# markers = markers_num * markers_price
# detergent = detergent_l * detergent_price
# total_price = panns + markers + detergent
# discount = total_price * percent_discount
# total = total_price - discount
#
# print(total)


# Second solution:
def cal_price(number, price):
    return number * price


pens_price = 5.80
markers_price = 7.20
detergent_price = 1.20

sum_price_panns = cal_price(int(input()), pens_price)
sum_markers_panns = cal_price(int(input()), markers_price)
sum_detergent_panns = cal_price(int(input()), detergent_price)
percent = int(input()) / 100
sum_products = (sum_price_panns + sum_markers_panns + sum_detergent_panns) * percent
total_price = (sum_price_panns + sum_markers_panns + sum_detergent_panns) - sum_products
print(total_price)
