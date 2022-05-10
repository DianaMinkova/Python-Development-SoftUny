# First solution:
name = input()
print("Hello, " + name + "!")

# Second solution:
name = input()
print(f'Hello, {name}!')

# Third solution:
print(f'Hello, {input()}!')


# Fourth solution:
# '''used def'''
def greeting_by_name(g_name):
    return f'Hello, {g_name}!'


res = greeting_by_name('Ivan')  # '''call a function, use the function name followed by parenthesis and add parameter'''
print(res)


# Fifth solution:
# '''used class'''
class GreetingNane:
    def __init__(self, g_name):
        self.g_name = g_name

    def get_greet(self):
        return f'Hello, {self.g_name}!'


f_name = GreetingNane('Ivan')
res = f_name.get_greet()
print(res)
