# First solution:
first_name = input()
last_name = input()
age = int(input())
town = input()

print(f'You are {first_name} {last_name}, a {age}-years old person from {town}.')


# Second solution:
# # '''used function'''
def collect_text(first_n, last_n, n_age, town_n):
    return f'You are {first_n} {last_n}, a {n_age}-years old person from {town_n}.'


people_1 = collect_text('Ivan', 'Ivanov', 27, 'Sofia')
people_2 = collect_text('Dodo', 'Dodova', 30, 'Plovdiv')
people_3 = collect_text('Pesho', 'Peshev', 30, 'Varna')

print(people_1)
print(people_2)
print(people_3)


# Third solution:
# '''used class''
class CollectText:
    def __init__(self, f_name, l_name, agr_num, t_name):
        self.f_name = f_name
        self.l_name = l_name
        self.agr_num = agr_num
        self.t_name = t_name

    def get_collect_text(self):
        return f'You are {self.f_name} {self.l_name}, a {self.agr_num}-years old person from {self.t_name}.'


people_1 = CollectText('Ivan', 'Ivanov', 27, 'Sofia')
res1 = people_1.get_collect_text()
print(res1)

people_2 = CollectText('Pesho', 'Peshev', 30, 'Varna')
res2 = people_2.get_collect_text()
print(res2)



