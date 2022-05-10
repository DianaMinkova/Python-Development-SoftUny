# First solution:
cm = float(input())
inch = cm * 2.54
print(inch)

# Second solution:
cm = float(input())
inch = 2.54
res = cm * inch
print(res)


# Third solution:
# '''used function'''
def cal_inch(num_cm, set_inch=2.54):
    result = num_cm * set_inch
    print(result)


cal_inch(5)


# Fourth solution:
# '''used class'''

class ConverterInch:

    def __init__(self, num_cm):
        self.num_cm = num_cm
        self.set_inch = 2.54

    def get_inch(self):
        return self.num_cm * self.set_inch


inch_res = ConverterInch(5)   # ''' Object is an instance of a class Rectangle'''
print(inch_res.get_inch())    # ''' Call the function'''

inch_res.num_cm = 8           # ''' Change value on parameter'''
print(inch_res.get_inch())








