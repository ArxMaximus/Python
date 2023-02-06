from functools import reduce


def my_decorator(func):
    def wrapper(*args, **kwargs):
        x = func(*args, **kwargs)
        print(f'Среднее арифметическое чисел {", ".join(map(str, args + tuple(kwargs.values())))} = {x / (len(args) + len(kwargs))}')
        return x
    return wrapper


@my_decorator
def summa(*args, **kwargs):
    m = args + tuple(kwargs.values())
    x = reduce(lambda s, v: s + v, m, 0)
    print(f'Сумма чисел {", ".join(map(str, m))} = {x}')
    return x


summa(2, 3, 3, x=4)
