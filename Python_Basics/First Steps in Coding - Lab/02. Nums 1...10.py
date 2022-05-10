# First solution:
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# Second solution:
# '''used For Loop to iterating over a sequence'''
numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for num in numbers:
    print(num)

# Third solution:
#''used While Loop to iterate over a sequence by index'''
numbers = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
index = 0

while index < len(numbers):
    print_num = numbers[index]
    print(print_num)
    index += 1

# short recording:
while index < len(numbers):
    print(numbers[index])
    index += 1

# Fourth solution:
# '''used List Comprehension'''
numbers = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
[print(num) for num in numbers]



