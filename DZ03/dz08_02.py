from functools import reduce

cnt = input('Количество студентов: ')
try:
    cnt = int(cnt)
    students = {input('{}-й студент: '.format(i)): input('Балл: ') for i in range(1, cnt + 1)}
    aver_points = int(reduce(lambda s, i: s + int(i[1]), students.items(), 0) / cnt + 0.5)
    print('\nСредний балл: {}. Студенты с баллом выше среднего:'.format(aver_points))
    print(reduce(lambda s, i: s + ((i[0] + '\n') if int(i[1]) > aver_points else ''), students.items(), ''))

except ValueError:
    print('Неверное число')