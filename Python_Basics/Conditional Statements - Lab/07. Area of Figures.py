from math import pow
from math import pi

# # First solution
# type_shape = input()
#
# if type_shape == 'square':
#     a = float(input())
#     area_square = pow(a, 2)
#     print(f'{area_square:.3f}')
#
# elif type_shape == 'rectangle':
#     a = float(input())
#     b = float(input())
#     area_rectangle = (a * b)
#     print(f'{area_rectangle:.3f}')
#
# elif type_shape == 'circle':
#     r = float(input())
#     area_circle = pi * (pow(r, 2))
#     print(f'{area_circle:.3f}')
#
# elif type_shape == 'triangle':
#     a = float(input())
#     h = float(input())
#     area_triangle = (a * h) / 2
#     print(f'{area_triangle:.3f}')

# Second solution
t_shape = input()

if t_shape == 'square':
    a = float(input())
    area = pow(a, 2)

elif t_shape == 'rectangle':
    a = float(input())
    b = float(input())
    area = (a * b)

elif t_shape == 'circle':
    r = float(input())
    area = pi * (pow(r, 2))

elif t_shape == 'triangle':
    a = float(input())
    h = float(input())
    area = (a * h) / 2

print(f'{area:.3f}')
