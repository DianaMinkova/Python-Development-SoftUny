number_of_pages = int(input())
read_pages_for_one_hour = int(input())
number_of_days = int(input())

total_time_for_read = number_of_pages / read_pages_for_one_hour
hour_of_days = total_time_for_read / number_of_days

print(int(hour_of_days))

