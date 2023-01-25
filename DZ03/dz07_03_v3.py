from functools import reduce


def symb_stat(in_tpl):
    return reduce(lambda summa, elem: summa.update([(elem, summa.setdefault(elem, 0) + 1)]) or summa, in_tpl, {})


num = 253523651
tpl = tuple(str(num))
print(tpl)
print('\n'.join('Количество ' + key + ' = ' + str(val) for key, val in symb_stat(tpl).items()))
