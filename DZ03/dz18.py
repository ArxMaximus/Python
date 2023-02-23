def bubble_sort(item_list, accend):
    """
    Пузыртковая сортировка

    :param item_list: несортированный список
    :return: отсортированный список
    """

    new_list = item_list[:]
    direct = 1 if accend else -1
    for i in range(len(new_list) - 1):
        changed = False
        for j in range(len(new_list) - 1 - i):
            if new_list[j] * direct > new_list[j + 1] * direct:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
                changed = True
        if not changed:
            break
    return new_list


def shake_sort(item_list, accend):
    """
    Сортировка перемешиванием (шейкерная сортировка)

    :param item_list: несортированный список
    :return: отсортированный список
    """

    new_list = item_list[:]
    direct = 1 if accend else -1
    begin = 0
    end = len(new_list) - 1
    changed = True
    while begin < end and changed:
        changed = False
        for i in range(begin, end - 1):
            if new_list[i] * direct > new_list[i + 1] * direct:
                new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
                changed = True
        end -= 1
        for i in range(end + 1, begin, -1):
            if new_list[i] * direct < new_list[i - 1] * direct:
                new_list[i], new_list[i - 1] = new_list[i - 1], new_list[i]
                changed = True
        begin += 1
    return new_list


def combo_sort(item_list, accend):
    """
    Сортировка расческой

    :param item_list: несортированный список
    :return: отсортированный список
    """

    new_list = item_list[:]
    direct = 1 if accend else -1
    factor = 1.247
    step = len(new_list) - 1
    while step >= 1:
        for i in range(len(new_list) - step):
            if new_list[i] * direct > new_list[i + step] * direct:
                new_list[i], new_list[i + step] = new_list[i + step], new_list[i]
        step = int(step // factor)
    return new_list


def insertion_sort(item_list, accend):
    """
    Сортировка вставками

    :param item_list: несортированный список
    :return: отсортированный список
    """

    new_list = item_list[:]
    direct = 1 if accend else -1
    for i in range(1, len(new_list)):
        x = new_list[i]
        j = i
        while j > 0 and new_list[j - 1] * direct > x * direct:
            new_list[j] = new_list[j - 1]
            j -= 1
        new_list[j] = x
    return new_list


def selection_sort(item_list, accend):
    """
    Сортировка выбором

    :param item_list: несортированный список
    :return: отсортированный список
    """

    new_list = item_list[:]
    direct = 1 if accend else -1
    for i in range(0, len(new_list)):
        min_num = i
        for j in range(i, len(new_list)):
            if new_list[j] * direct < new_list[min_num] * direct:
                min_num = j
        if min_num > i:
            new_list[i], new_list[min_num] = new_list[min_num], new_list[i]
    return new_list


def merge_sort(item_list, accend):
    """
    Сортировка слиянием

    :param item_list: несортированный список
    :return: отсортированный список
    """

    n = len(item_list)
    direct = 1 if accend else -1
    if n < 2:
        return item_list

    left = merge_sort(item_list[:n // 2], accend)
    right = merge_sort(item_list[n // 2:], accend)

    i = j = 0

    new_list = []

    while i < len(left) and j < len(right):
        if left[i] * direct < right[j] * direct:
            new_list.append(left[i])
            i += 1
        else:
            new_list.append(right[j])
            j += 1
    if i == len(left):
        new_list.extend(right[j:])
    else:
        new_list.extend(left[i:])
    return new_list


def shell_sort(data, accend):
    """
    Сортировка Шелла

    :param item_list: несортированный список
    :return: отсортированный список
    """

    last_index = len(data)
    direct = 1 if accend else -1
    step = len(data) // 2
    while step > 0:
        for i in range(step, last_index, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] * direct > data[j] * direct:
                data[delta], data[j] = data[j], data[delta]
                j = delta
                delta = j - step
        step //= 2
    return data


def quick_sort(item_list, accend):
    """
    Быстрая сортировка

    :param item_list: несортированный список
    :return: отсортированный список
    """

    new_list = item_list[:]
    direct = 1 if accend else -1
    if len(new_list) > 1:
        x = new_list[(len(new_list) - 1) // 2]

        low = [i for i in new_list if i * direct < x * direct]
        eq = [i for i in new_list if i == x]
        hi = [i for i in new_list if i * direct > x * direct]

        new_list = quick_sort(low, accend) + eq + quick_sort(hi, accend)

    return new_list


if __name__ == '__main__':
    list1 = [5, 9, 6, 7]
    list2 = [3, 11, 8]
    list3 = [2, 4]
    list4 = [10, 1, 12]
    num = int(input('Выберите метод сортировки:\n1 - Пузырьковый\n2 - Перемешиванием\n3 - Расческой\n4 - Вставками\n5 - Выбором\n6 - Слиянием\n7 - Шелла\n8 - Быстрая сортировка\n'))
    print(list1, list2, list3, list4)
    accendent = True if input('1 - сортировка по убыванию\n2 - сортировка по возрастанию\n') == '1' else False
    match num:
        case 1:
            res = bubble_sort(list1 + list2 + list3 + list4, accendent)
        case 2:
            res = shake_sort(list1 + list2 + list3 + list4, accendent)
        case 3:
            res = combo_sort(list1 + list2 + list3 + list4, accendent)
        case 4:
            res = insertion_sort(list1 + list2 + list3 + list4, accendent)
        case 5:
            res = selection_sort(list1 + list2 + list3 + list4, accendent)
        case 6:
            res = merge_sort(list1 + list2 + list3 + list4, accendent)
        case 7:
            res = shell_sort(list1 + list2 + list3 + list4, accendent)
        case 8:
            res = quick_sort(list1 + list2 + list3 + list4, accendent)
        case _:
            res = 'Неправильный ввод'
    print(res)