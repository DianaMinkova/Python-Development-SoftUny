# First solution:
time_project = 3
architect_name = input()
count_of_projects = int(input())

need_hours = time_project * count_of_projects
print(f'The architect {architect_name} will need {need_hours} hours to complete {count_of_projects} project/s.')

# Second solution:
#'''used function'''
def preparation_of_projects(architect, count_projects, fix_time = 3):
    res = fix_time * count_projects
    return f'The architect {architect} will need {res} hours to complete {count_projects} project/s.'


project_1 = preparation_of_projects('George', 4)
project_2 = preparation_of_projects('Sanya', 9)

print(project_1)
print(project_2)


# Third solution:
# '''used class''
class PreparationProjects:
    def __init__(self, name_architect, projects_count):
        self.name_architect = name_architect
        self.projects_count = projects_count
        self.time_preparation = 3

    def get_need_time(self):
        need_time = self.time_preparation * self.projects_count
        return f'The architect {self.name_architect} will need {need_time} hours to complete {self.projects_count} project/s.'


project_1 = PreparationProjects('George', 4)
res1 = project_1.get_need_time()
print(res1)

project_2 = PreparationProjects('Sanya', 9)
res2 = project_2.get_need_time()
print(res2)

