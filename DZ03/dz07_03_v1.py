from functools import reduce


def symb_stat(in_crt):

    def stat_add(in_list, in_elem):
        if in_elem in in_list[0]:
            in_list[1][in_list[0].index(in_elem)] += 1
        else:
            in_list[0].append(in_elem)
            in_list[1].append(1)
        return in_list

    return zip(*reduce(lambda summa, elem: stat_add(summa, elem), in_crt, [[], []]))


num = 253523651
tpl = tuple(str(num))
print(tpl)
print('\n'.join('Количество ' + i[0] + ' = ' + str(i[1]) for i in symb_stat((tpl))))
