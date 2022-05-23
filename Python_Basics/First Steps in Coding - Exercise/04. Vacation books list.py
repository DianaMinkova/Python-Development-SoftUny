# First solution:
number_of_pages = int(input())
read_pages_for_one_hour = int(input())
number_of_days = int(input())

total_time_for_read = number_of_pages / read_pages_for_one_hour
hour_of_days = total_time_for_read / number_of_days

print(int(hour_of_days))

# Second solution:
def total_time(pages, hour=1):
    read = int(pages / hour)
    return read


def days_read(read, day_n):
    hour_days = int(read / day_n)
    return hour_days


time = total_time(int(input('Input number of pages: ')), int(input('Pages you read in 1 hour: ')))
days = days_read(time, int(input('The number of days: ')))
print(f'Hours required: {days}')
