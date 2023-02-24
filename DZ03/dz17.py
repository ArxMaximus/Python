def count_negative_rec(in_list):
    '''
    Подсчет отрицательных чисел в списке рекурсивным методом

    :param in_list: входящий список
    :return: количество отрицательных чисел в списке
    '''
    if len(in_list) == 1:
        return 1 if in_list[0] < 0 else 0
    return (1 if in_list[0] < 0 else 0) + count_negative_rec(in_list[1:])


def count_negative_iter(in_list):
    '''
    Подсчет отрицательных чисел в списке итерационным методом

    :param in_list: входящий список
    :return: количество отрицательных чисел в списке
    '''
    return len(list(filter(lambda x: x < 0, in_list)))


if __name__ == '__main__':
    lst = [-2, 3, 8, -11, -4, 6]
    print(f'Исходный список:\n\033[34m{lst}\n\033[0mКоличество отрицательных чисел:\n\t- рекурсивным методом: '
          f'\033[35m{count_negative_rec(lst)}\n\t\033[0m- итерационным методом: \033[35m{count_negative_iter(lst)}')
