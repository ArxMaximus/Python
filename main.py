# def coins(num):
#     c_high = num // 10
#     c_low = num % 10
#     if c_high == 1 or c_low > 4 or c_low == 0:
#         return 'копеек'
#     elif c_low > 1:
#         return 'копейки'
#     else:
#         return 'копейка'
#
#
# if __name__ == '__main__':
#     cnt = int(input('Количество: '))
#     if 0 < cnt < 100:
#         print('На вашем счете', cnt, coins(cnt), end='.')
#     else:
#         print('Столько посчитать не получится!')

# day = 'Среда'
# time = 18
#
# match day.lower():
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 18:
#         print('Рабочий день')
#     case 'суббота' | 'воскресенье':
#         print('Выходной')
#     case _ if time < 9 or time > 18:
#         print('Не рабочее время!')
#     case _:
#         print('Вообще не день')

# x = int(input('Делимое: '))
# y = int(input('Делитель: '))
# print(x / y if y != 0 else 'На ноль делить нельзя!')

# x = input('x: ')
# y = input('y: ')
# try:
#     x, y = int(x), int(y)
# except ValueError:
#     x = str(x)
# finally:
#     print(x + y)


# i = 1
# while i <= 20:
#     print(str(i) + ', ' if i % 2 == 0 else '', end='')
#     i += 1

# try:
#     x = int(input('Количество: '))
#     print('*' * x)
# except ValueError:
#     print('Недопустимое число!')

# a = int(input('Начало диапазона: '))
# b = int(input('Конец диапазона: '))
# if a % 2 == 0:
#     a += 1
# sum1 = 0
# if i > j: i, j = j, i
# while a <= b:
#     sum += a
#     a += 2;
# print('Сумма нечетных: ', sum1)

# n = input('Введите целое число: ')
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print('Не целое число (или вообще не число)!')
#         n = input('Введите целое число: ')
#
# if n % 2 == 0:
#     print('Четное число.')
# else:
#     print('Нечетное число.')


# i = 0
# while i < 10:
#     print(i, end = ' ')
#     if i == 5:
#         break
#     i += 1
# print('Цикл завершен!')

# i = 0
# while True:
#     print(i)
#     if i == 10:
#         break
#     i += 1

# while True:
#     n = int(input('Введите положительное число: '))
#     if n < 0:
#         break

# m = 1
# while True:
#     n = int(input('Число: '))
#     if n == 0:
#         break
#     m *= n
# print('Произведение равно:', m)


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j, '\t', end='')
#         j += 1
#     print()
#     i += 1

# for i in "Hello", "red", "blue", "yellow", 20, True, 0.3:
#     print(i)

# class FRange:
#     def __init__(self, start: float, end: float = None, step: float = 1):
#         if not end:
#             self.start = 0
#             self.end = start
#         else:
#             self.start = start
#             self.end = end
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start < self.end and self.step > 0 or self.start > self.end and self.step < 0:
#             self.start += self.step
#             return self.start - self.step
#         else:
#             raise StopIteration
#
#
# for i in FRange(10):
#     print(i, end=' ')

# for i in iter(FloatIter()):
#     print(format(i, '.10f'), end=' ')


# for i in zip(range(1, 10), range(2, 11)):
#     print(i, end=' ')

# num = input('Введите целое число: ')
# try:
#     num = int(num)
#     for i in range(1, num):
#         if i % 10 == i // 10:
#             print(i, end=' ')
# except ValueError:
#     print('Вас просили число!')

# w = int(input('W = '))
# h = int(input('H = '))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print('*', end='')
#         elif (i + j) % 2 == 0:
#             print('\\', end='')
#         else:
#             print('/', end='')
#     print()

# s = []
# print(s)
# print(type(s))
#
# b = list()
# print(b)
# print(type(b))

# s = [5, 2] * 6
# print(s)

# n = range(10)
#
# print('; '.join(map(str, list(n))))

# a = filter(sum, [int(input('-> ')) for num in [0] * int(input('Count: '))])
# print(a)

# for i in a:
#     a[i] = i

# for i, item in enumerate(a):
#     a[i] = i
#
# for i in a:
#     print(i)

# a = [int(input('-> ')) for num in [0] * int(input('Count: '))]
# count = sum1 = 0
# for i in a:
#     if i != 0:
#         count += 1
#         sum1 += i
# print('Среднее: ', sum1 / count)
#
# print(a)

# a = [int(input('-> ')) for num in [0] * int(input('Count: '))]

# for i in range(1, len(a)):
#     if a[i - 1] < a[i]:
#         print(a[i], end=' ')

# a = [int(input('-> ')) for num in [0] * int(input('Count: '))]
# prev = None
# for i in a:
#     if prev and i > prev:
#         print(i, end=' ')
#     prev = i

# a = [9, 1, 3, 4, 5]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)

# a = [9, 1, 3, 4, 5, 17]
# pos = 4
# item = 22
# print(a[:pos]+[item]+a[pos:])

# a = [1, 2, 3, 4, 5, 6, 7]
# [:]
# [::-1]
# [::2]
# [1::2]

# import time
#
# for i in range(10):
#     print(i, end='\r')
#     time.sleep(1)
#
# a = list(range(1, 8))
# print(a)
# a[1:6] = []
# print(a)

# print(dir(list))

# a = list(range(1, 8))
# print(a)
#
# a.extend(range(10))
#
# print(a)

# a = [int(input('-> ')) for num in [0] * int(input('Count: '))]

# a = int(input('Количество элементов:'))
# s = []
# for i in range(a):
#     x = int(input('--> '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print('{} не делится на 3 без остатка.'.format(x))
# print(s)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# z = []
# for i in range(len(a) if len(a) < len(b) else len(b)):
#     z.extend([a[i], b[i]])
# # z = list(map([].extend((a, b), )))
# z.extend(a[i:] if len(a) > len(b) else b[i:])
# print(z)


# a = [int(input('-> ')) for num in ' ' * int(input('Count: '))]
# b = int(input('Index: '))
# a.pop(b)
# print(a)

# b = ['Виталий', 'Сергей', 'Александр', 'Анна']
#
# b.sort(key=len, reverse=True)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
#
# c = sorted(a)
#
# print(b)

# import random
#
# print(random.randint(1, 5))

# from random import randint as r, randrange
#
# print(r(1, 5))
# print(randrange(1, 9, 2))

# import random as r

# print(round(r.uniform(1, 10), 3))

# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
#
# print(r.choice(city))
# print(r.choices(city, k=10))

# mas = [i for i in range(10)]
# r.shuffle(mas)
# print(mas)

# from random import randint
#
# print('Заполнить список из 10 элементов случайными числами. Найти максимальный элемент списка и переместить его в начало списка.\n')
#
# mas = [randint(10, 99) for i in range(10)]
# print(mas)
# print('Max: ', max(mas))
# mas.insert(0, mas.pop(mas.index(max(mas))))
# print(mas, '\n\n')
#
# print('Заполнить список из 10 элементов случайными числами, как положительными, так и отрицательными.')
# print('Изменить этот список таким образом, чтобы все отрицательные элементы оказались в конце.\n')
#
# mas = [randint(-20, 20) for i in range(10)]
# print(mas)
# mas.sort(reverse=True)
# print(mas, '\n\n')
#
# print('Заполнить список из 10 элементов случайными числами. Удалить все элементы, расположенные перед минимальным элементом списка.\n')
# mas = [randint(10, 99) for i in range(10)]
# print(mas)
# print('Min: ', min(mas))
# print('Index min: ', mas.index(min(mas)))
# mas = mas[mas.index(min(mas)):]
# print(mas)

# s = [8, 9, 6, 4, 7, 8, 2, 3]
# res = []
#
# for i in s:
#     if i % 2 == 0:
#         res.append(i)
#
# print(res)


# print('Выбор фигуры:\n1 - треугольник\n2 - прямоугольник\n3 - круг')
# shape = input(': ')
# try:
#     shape = int(shape)
#     if shape < 1 or shape > 3:
#         raise ValueError
#     match shape:
#         case 1:
#             try:
#                 a = int(input('Введите сторону a = '))
#                 b = int(input('Введите сторону b = '))
#                 c = int(input('Введите сторону c = '))
#                 p = (a + b + c) / 2
#                 print('Плошадь равна ', round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 3))
#             except ValueError:
#                 print('Необходимо целое число')
#         case 2:
#             try:
#                 a = int(input('Введите сторону a = '))
#                 b = int(input('Введите сторону b = '))
#                 print('Плошадь равна ', round(a * b, 3))
#             except ValueError:
#                 print('Необходимо целое число')
#         case 3:
#             try:
#                 r = int(input('Введите радиус = '))
#                 print('Плошадь равна ', round(3.141592654 * r * r, 3))
#             except ValueError:
#                 print('Необходимо целое число')
# except ValueError:
#     print('Необходимо число от 1 до 3.')

# def hello(name, word):
#     print('Hello, {}. Say {}!'.format(name, word))
#
# hello(word='Irina', name='hello')

# x = [5]

# def get_sum(cnt, a, b):
#     print((a + b) * (cnt // 2) + a * (cnt % 2))


# def get_sum(count, a, b):
#     print(''.join(a * (1 - i % 2) + b * (i % 2) for i in range(count)))
#
# get_sum(9, '+', '-')

# def maximum(one, two):
#     return one > two
#
#
# print(maximum(5, 7))


# def check_password(password):
#
#     # if len(password) >= 8:
#     #     return True
#     if len(password) >= 8 and password.upper() != password and password.lower() != password:
#         return True
#     return False
#
# p = input('Введите пароль: ')
# if check_password(p):
#     print('Этот пароль надежный.')
# else:
#     print('Этот пароль ненадежный.')

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst

# def change(lst):
#     return [lst[-1]] + lst[1:-1] + [lst[0]]
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def digits_sum(n, even=True):
#     return sum(map(int, filter(lambda x: ((1 - int(x) % 2) * even + (int(x) % 2) * (not even)), [*str(n)])))


# def digits_sum(n, even=True):
#     return sum(filter(lambda x: (1 - x % 2) * even + (x % 2) * (not even), map(int, [*str(n)])))
#
#
# print(digits_sum(9874023))      # 14 19
# print(digits_sum(38271, False))        # 10 11
# print(digits_sum(123456789))    # 20 25


# s = tuple(2 ** i for i in range(12))
# print(s)

# def tuple_parse(tup, num):
#     if num not in tup:
#         return tuple()
#     first = tup.index(num)
#     if num not in tup[first + 1:]:
#         return tup[first:]
#     last = tup.index(num, first + 1)
#     return tup[first:last + 1]
#
#
# print(tuple_parse((1, 2, 3), 8))
# print(tuple_parse((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(tuple_parse((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint
#
#
# def tpl_sum(t1, t2):
#     print(t1)
#     print(t2)
#     print(t1 + t2, (t1 + t2).count(0))
#
#
# tpl_sum(tuple(randint(0, 5) for i in range(12)), tuple(randint(-5, 0) for j in range(12)))
#


# point = (10, 0)

# match point:
#     case (0, 0):
#         print('Точка находится в координатах (0, 0)')
#     case (x, 0):
#         print('Точка находится в координате ', x, ' по оси X и в координате 0 по оси Y')

# t = (1, 2, 3)
# _, y, _ = t
# print(y)

# countries = (
#     ('Германия', 80.2, (('Берлин', 3.326), ('Гамбург', 1.718))),
#     ('Франция', 66, (('Париж', 2.2), ('Марсель', 1.6))),
# )
#
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print('\nСтрана:', countryName, ', население =', countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print('\tГород:', cityName, ', население =', cityPopulation)


# from functools import reduce
# import sys
#
#
# def is_simple(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
#
# def min_max(in_list):
#     return reduce(lambda summ, elem: (elem if elem < summ[0] else summ[0], summ[1]) if is_simple(elem) else (summ[0],
#                                       elem if elem > summ[1] else summ[1]), in_list, (sys.maxsize, -sys.maxsize))
#
#
# lst = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
# print(lst, '\n')
# print('Min: {0[0]}\nMax: {0[1]}'.format(min_max(lst)))

# from functools import reduce
#
#
# def find_max13(in_list):
#     return reduce(lambda summa, elem: elem if elem > 0 and elem % 13 == 0 else summa, in_list, 0) or 'no such numbers'
#
#
# print(find_max13([2, 7, 0, 3, 1, 5, -13]))
# print(find_max13([2, 7, 0, 3, 1, 5, -13, 13]))
# print(find_max13([26]))
# print(find_max13([99, 99, 100, 34, -39]))
# print(find_max13([99, 39, 99, 100, 34]))


# crt = ('ab', 'abcd', 'cde', 'abc', 'def')
# s = 'ab'
#
# print('Yes' if s in crt else 'No')

# from functools import reduce


# def symb_stat_v1(in_crt):
#
#     def stat_add(in_list, in_elem):
#         if in_elem in in_list[0]:
#             in_list[1][in_list[0].index(in_elem)] += 1
#         else:
#             in_list[0].append(in_elem)
#             in_list[1].append(1)
#         return in_list
#
#     return zip(*reduce(lambda summa, elem: stat_add(summa, elem), in_crt, [[], []]))


# def symb_stat(in_crt):
#     return zip(*reduce(lambda summa, elem: [summa[0], summa[1][:summa[0].index(elem)] + [summa[1][summa[0].index(elem)] + 1] +
#                                             summa[1][summa[0].index(elem) + 1:]] if elem in summa[0] else
#                                             [summa[0] + [elem], summa[1] + [1]], in_crt, [[], []]))
#
#
# num = 253523651
# tpl = tuple(str(num))
# print(tpl)
# print('\n'.join('Количество ' + i[0] + ' = ' + str(i[1]) for i in symb_stat((tpl))))

# s = {'banana', 'apple', 'orange'}
# print(s)
#
# for i in s:
#     print(i)

# numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6]
# s = {x for x in numbers if x % 2 == 0}
# print(s)
#

# def to_set(par):
#     return set(par), len(set(par))
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# s = {'banana', 'apple', 'orange'}
# s.add('pineapple')
# print(s)
# print('apple' in s)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2', 'cc_1', 'cc_2']
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] if i[0] == 'b' else i for i in r}
# print(a)

# s = {'banana', 'apple', 'orange'}
# s |= {'pineapple'}
# print(s)

# d = {'one w': 1, 'two w': 2, 'three w': 3}
# print(d)

# a = [1, 2, 3]
# b = dict(map(lambda x: (x, x), a))
#
# print(b)

# d = {i: i ** 2 for i in range(2, 7)}
# print(d)

# d = {0: 'text', 'one': 45, (1, 2.3): 'Кортеж', True: 'Boolean', 'x': [2, 3]}
# print('\n'.join(str(i) + str(j) for i, j in enumerate(d)))

# from functools import reduce
#
# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
#
# s = reduce(lambda x, i: x * d[i], d, 1)
#
# print(s)

# d = {input('key: '): input('-->') for i in range(1, 5)}
#
# print(d)
#
# dislike = int(input('Item index to delete: '))
#
# if dislike in d:
#     del d[dislike]
#     print(d)
# else:
#     print('No suck a key in dict')

# goods = {
#     'Core-i3-4330': [9, 4500],
#     'Core i5-4670K': [3, 8500],
#     'AMD FX-6300': [6, 3700],
#     'Pentium G3220': [8, 2100],
#     'Core i5-3450': [5, 6400],
# }
#
# for i, j in enumerate(goods):
#     print(i + 1, ') ', j, ' - ', goods[j][0], ' шт. по ', goods[j][1], ' руб.', sep='')
#
# while True:
#     num = input('№ ')
#     if num == '0':
#         break
#     if int(num) > len(goods):
#         print('Wrong number!')
#     else:
#         cnt = input('Count: ')
#         goods[list(goods.keys())[int(num) - 1]][0] = cnt
#
# for i, j in enumerate(goods):
#     print(i + 1, ') ', j, ' - ', goods[j][0], ' шт. по ', goods[j][1], ' руб.', sep='')

# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], ' руб.', sep='')

# d = {'emp1': {'name': 'John', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3': {'name': 'Brad', 'salary': 6500}}
# print('---------------------------\n|  ID   |  NAME  | SALARY |')
# print('\n'.join('---------------------------\n| ' + i + '\t| ' + d[i]['name'] + '\t | ' + str(d[i]['salary']) + '\t  |' for i in d))
# print('---------------------------\n')
# d['emp3']['salary'] = 8500;
# print('---------------------------\n|  ID   |  NAME  | SALARY |')
# print('\n'.join('---------------------------\n| ' + i + '\t| ' + d[i]['name'] + '\t | ' + str(d[i]['salary']) + '\t  |' for i in d))
# print('---------------------------\n')

# from functools import reduce
#
# cnt = input('Количество студентов: ')
# try:
#     cnt = int(cnt)
#     students = {input('{}-й студент: '.format(i)): input('Балл: ') for i in range(1, cnt + 1)}
#     aver_points = int(reduce(lambda s, i: s + int(i[1]), students.items(), 0) / cnt + 0.5)
#     print('Средний балл: {}. Студенты с баллом выше среднего:'.format(aver_points))
#     # print(*map(lambda x: x[0], filter(lambda item: int(item[1]) > aver_points, students.items())), sep='\n')
#     print(reduce(lambda s, i: s + ((i[0] + '\n') if int(i[1]) > aver_points else ''), students.items(), ''))
#
# except ValueError:
#     print('Неверное число')

# d1 = ['red', 'green', 'blue']
# d2 = ['#FF0000', '#008000', '#0000FF']

# Вариант 1
# d = {d1[i]: d2[i] for i in range(len(d1))}

# Вариант 2
# d = {j: d2[i] for i, j in enumerate(d1)}

# Вариант 3
# d = dict(zip(d1, d2))
#
# print(d)


# d = {i: i ** 3 for i in range(1, 11)}
# print(d)

# d = {
#     'John': {
#         'N': 3056,
#         'S': 8463,
#         'E': 8441,
#         'W': 2694,
#     },
#     'Tom': {
#         'N': 4832,
#         'S': 6786,
#         'E': 4737,
#         'W': 3612,
#     },
#     'Anne': {
#         'N': 5239,
#         'S': 4802,
#         'E': 5820,
#         'W': 1859,
#     },
#     'Fiona': {
#         'N': 3904,
#         'S': 3645,
#         'E': 8821,
#         'W': 2451,
#     },
# }
#
# from functools import reduce
#
# print(reduce(lambda x, val: x + val + '\n' + reduce(lambda y, v: y + '\t' + v + ': ' + str(d[val][v]) + '\n', d[val], ''), d, ''))
#
# a = input('Name: ')
# b = input('Region: ')
# c = input('New value: ')
#
# d[a][b] = c
#
# print(reduce(lambda x, val: x + val + '\n' + reduce(lambda y, v: y + '\t' + v + ': ' + str(d[val][v]) + '\n', d[val], ''), d, ''))


# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = [randint(1, 99) for i in range(10)]
# print(res)

# from random import randint
#
# l = [randint(1, 40) for i in range(10)]
# print(l)
# n = list(filter(lambda x: 10 <= x <= 20, l))
# print(n)

# l = [45, 55, 60, 37, 100, 105, 220]
#
# n = list(filter(lambda x: x % 15 == 0, l))
# print(n)

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#
# @my_decorator
# def func_test():
#     print('Hello, I am func "func_test"')
#
# func_test()

# def my_decorator(func):
#     count = 0
#     def wrap():
#         nonlocal count
#         count += 1
#         print('{}\nCount = {}'.format(func(), count))
#     return wrap
#
# @my_decorator
# def Hello():
#     return 'Hello!'
#
# Hello()
# Hello()
# Hello()

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print('args:', args)
#         print('kwargs:', kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print('My name is {} {}!'.format(first, last))
#
#
# @args_decorator
# def print_full_name_1(first, second, last):
#     print('My name is {} {} {}!'.format(first, second, last))
#
#
# print_full_name('Ivan', 'Sidorov')
# print_full_name_1('Dmitry', 'Petrovich', 'Petrov')

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print('{}: {} {} {} ='.format(args1, x, args2, y), end=' ')
#             fn(x, y)
#         return wrap
#     return args_dec
#
#
# @decor('Сумма', '+')
# def summa(a, b):
#     print(a + b)
#
#
# @decor('Разность', '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def multiply(num):
#     def decor(fn):
#         def wrap(mult):
#             return num * fn(mult)
#         return wrap
#     return decor
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))
#

# from functools import reduce
#
#
# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             if reduce(lambda s, i: s and type(f_args[i]) == args[i], range(len(f_args)), True) and reduce(lambda s, i: s and type(f_kwargs[i]) == kwargs[i], kwargs, True):
#                 return fn(*f_args, **f_kwargs)
#             else:
#                 raise TypeError('Некорректный тип данных!')
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn_2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn_3(x, y, z='Hello!'):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# print(typed_fn_2('Mo', 'du', 'le'))
# print(typed_fn_3('+', '-', 5))

# def args_decorator(tx=None, decorator_text=''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end='')
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator(decorator_text='Hello, ')
# def hello_world(text):
#     print(text)
#
#
# @args_decorator
# def hello_world_2(text):
#     print(text)
#
#
# hello_world('world!')
# hello_world_2('Hi!')

# from functools import reduce
#
# d = {'c': 3, 'a': 1, 'b': 2, 'd': 4}
#
# w = reduce(lambda s, i: False or s.update({i[0]: i[1]}) if len(s) <= 2 else s, d.items(), {})
#
# print(w)
#

a = 5
print(a)