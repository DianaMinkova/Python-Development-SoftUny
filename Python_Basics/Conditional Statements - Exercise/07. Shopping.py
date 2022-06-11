budget = float(input())
n_video_cards = int(input())
n_processors = int(input())
n_ram = int(input())

video_cards = 250
processors = 0.35
ram = 0.10

sum_video_cards = video_cards * n_video_cards
sum_processors = (sum_video_cards * processors) * n_processors
sum_ram = (sum_video_cards * ram) * n_ram

sum_product = sum_video_cards + sum_processors + sum_ram
if n_video_cards > n_processors:
    sum_product -= sum_product * 0.15


if budget >= sum_product:
    rest_budget = abs(sum_product - budget)
    print(f"You have {rest_budget:.2f} leva left!")
else:
    rest_budget = abs(sum_product - budget)
    print(f"Not enough money! You need {rest_budget:.2f} leva more!")
