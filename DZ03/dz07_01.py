from functools import reduce


def find_max13(in_list):
    return reduce(lambda summa, elem: elem if elem > 0 and elem % 13 == 0 else summa, in_list, 0) or 'no such numbers'


print(find_max13([2, 7, 0, 3, 1, 5, -13]))
print(find_max13([2, 7, 0, 3, 1, 5, -13, 13]))
print(find_max13([26]))
print(find_max13([99, 99, 100, 34, -39]))
print(find_max13([99, 39, 99, 100, 34]))
