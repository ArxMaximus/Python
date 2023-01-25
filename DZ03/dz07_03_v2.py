from functools import reduce


def symb_stat(in_tpl):
    return zip(*reduce(lambda summa, elem: [summa[0], summa[1][:summa[0].index(elem)] + [summa[1][summa[0].index(elem)] + 1] +
                                            summa[1][summa[0].index(elem) + 1:]] if elem in summa[0] else
                                            [summa[0] + [elem], summa[1] + [1]], in_tpl, [[], []]))


num = 253523651
tpl = tuple(str(num))
print(tpl)
symb_stat(tpl)
print('\n'.join('Количество ' + i[0] + ' = ' + str(i[1]) for i in symb_stat((tpl))))
