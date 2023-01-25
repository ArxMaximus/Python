from functools import reduce
import sys


def is_simple(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def min_max(in_list):
    return reduce(
        lambda summa, elem: (min(elem, summa[0]), summa[1]) if is_simple(elem) else
                            (summa[0], max(elem, summa[1])), in_list, (sys.maxsize, -sys.maxsize))


lst = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
print(lst, '\n')
print('Min: {0[0]}\nMax: {0[1]}'.format(min_max(lst)))
