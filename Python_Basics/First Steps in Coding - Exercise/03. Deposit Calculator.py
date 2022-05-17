# # First solution:
# deposit = float(input())
# month = int(input())
# interest = float(input())
# month_interest = deposit * interest / 12 / 100
# total_money = deposit + month * month_interest
# print(total_money)


# Second solution:

def deposit_calculator(sum_deposit, count_month, percent_interest):
    accrued_interest = sum_deposit * percent_interest / 100
    interest_for_month = accrued_interest / 12
    total_interest = sum_deposit + count_month * interest_for_month
    print(total_interest)


deposit_calculator(sum_deposit=200, count_month=3, percent_interest=5.7)
deposit_calculator(sum_deposit=2350, count_month=6, percent_interest=7)
