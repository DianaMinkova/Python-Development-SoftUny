# First solution:
# '''Input: 6,8'''
side_a = int(input())
side_b = int(input())
area = side_a * side_b
print(area)


# Second solution:
# '''used function'''
def area_of_rectangle(width, height):
    area_sum = width * height
    print(area_sum)


area_of_rectangle(8, 6)


# Third solution:
# '''used class'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


sum_area = Rectangle(8, 6)  # ''' Object is an instance of a class Rectangle'''
print(sum_area.get_area())

sum_area.height = 8  # ''' Change value on parameter'''
print(sum_area.width)
print(sum_area.height)
print(sum_area.get_area())
