# First solution
number = int(input())

if number % 2 == 0:
    print('even')
else:
    print('odd')


# Second solution
def check(num):
    if num % 2 == 0:
        print('even')
    else:
        print('odd')


check(2)
check(3)

# Third solution
n = int(input())
print(['even', 'odd'][n % 2])
