d = {'emp1': {'name': 'John', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3': {'name': 'Brad', 'salary': 6500}}
print('---------------------------\n|  ID   |  NAME  | SALARY |')
print('\n'.join('---------------------------\n| ' + i + '\t| ' + d[i]['name'] + '\t | ' + str(d[i]['salary']) + '\t  |' for i in d))
print('---------------------------\n')
d['emp3']['salary'] = 8500;
print('---------------------------\n|  ID   |  NAME  | SALARY |')
print('\n'.join('---------------------------\n| ' + i + '\t| ' + d[i]['name'] + '\t | ' + str(d[i]['salary']) + '\t  |' for i in d))
print('---------------------------\n')