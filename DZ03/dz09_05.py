from functools import reduce

def summa(*args, **kwargs):
    return reduce(lambda s, v: (s[0] + (' ' if s[0] != '' else '') + str(s[1] + v), s[1] + v), args + tuple(kwargs.values()), ('', 0))[0]


print(summa(3, 9, d=1))
print(summa(2, 5, 4, 2))
print(summa(3, 5, 10, 6, 3))
