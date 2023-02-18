from random import randint
import time


def bubble_sort(item_list):
    """
    Пузыртковая сортировка

    :param item_list: несортированный список
    :return: отсортированный список
    """

    new_list = item_list[:]
    for i in range(len(new_list) - 1):
        changed = False
        for j in range(len(new_list) - 1 - i):
            if new_list[j] > new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
                changed = True
        if not changed:
            break
    return new_list


def shake_sort(item_list):
    """
    Сортировка перемешиванием (шейкерная сортировка)

    :param item_list: несортированный список
    :return: отсортированный список
    """

    new_list = item_list[:]
    begin = 0
    end = len(new_list) - 1
    changed = True
    while begin < end and changed:
        changed = False
        for i in range(begin, end - 1):
            if new_list[i] > new_list[i + 1]:
                new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
                changed = True
        end -= 1
        for i in range(end + 1, begin, -1):
            if new_list[i] < new_list[i - 1]:
                new_list[i], new_list[i - 1] = new_list[i - 1], new_list[i]
                changed = True
        begin += 1
    return new_list


def combo_sort(item_list):
    """
    Сортировка расческой

    :param item_list: несортированный список
    :return: отсортированный список
    """

    new_list = item_list[:]
    factor = 1.247
    step = len(new_list) - 1
    while step >= 1:
        for i in range(len(new_list) - step):
            if new_list[i] > new_list[i + step]:
                new_list[i], new_list[i + step] = new_list[i + step], new_list[i]
        step = int(step // factor)
    return new_list


def insertion_sort(item_list):
    """
    Сортировка вставками

    :param item_list: несортированный список
    :return: отсортированный список
    """

    new_list = item_list[:]
    for i in range(1, len(new_list)):
        x = new_list[i]
        j = i
        while j > 0 and new_list[j - 1] > x:
            new_list[j] = new_list[j - 1]
            j -= 1
        new_list[j] = x
    return new_list


def selection_sort(item_list):
    """
    Сортировка выбором

    :param item_list: несортированный список
    :return: отсортированный список
    """

    new_list = item_list[:]
    for i in range(0, len(new_list)):
        min_num = i
        for j in range(i, len(new_list)):
            if new_list[j] < new_list[min_num]:
                min_num = j
        if min_num > i:
            new_list[i], new_list[min_num] = new_list[min_num], new_list[i]
    return new_list


def merge_sort(item_list):
    """
    Сортировка слиянием

    :param item_list: несортированный список
    :return: отсортированный список
    """

    n = len(item_list)
    if n < 2:
        return item_list

    left = merge_sort(item_list[:n // 2])
    right = merge_sort(item_list[n // 2:])

    i = j = 0

    new_list = []

    # while i < len(left) or j < len(right):
    #     if not i < len(left):
    #         new_list.append(right[j])
    #         j += 1
    #     elif not j < len(right):
    #         new_list.append(left[i])
    #         i += 1
    #     elif left[i] < right[j]:
    #         new_list.append(left[i])
    #         i += 1
    #     else:
    #         new_list.append(right[j])
    #         j += 1

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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


def shell_sort(data):
    """
    Сортировка Шелла

    :param item_list: несортированный список
    :return: отсортированный список
    """

    last_index = len(data)
    step = len(data) // 2
    while step > 0:
        for i in range(step, last_index, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] > data[j]:
                data[delta], data[j] = data[j], data[delta]
                j = delta
                delta = j - step
        step //= 2
    return data

    # new_list = item_list[:]
    # step = len(new_list) // 2
    # while step > 0:
    #     for i in range(len(new_list) - step):
    #         if new_list[i] > new_list[i + step]:
    #             new_list[i], new_list[i + step] = new_list[i + step], new_list[i]
    #     step //= 2
    # return new_list


def quick_sort(item_list):
    """
    Быстрая сортировка

    :param item_list: несортированный список
    :return: отсортированный список
    """

    new_list = item_list[:]
    if len(new_list) > 1:
        x = new_list[(len(new_list) - 1) // 2]

        low = [i for i in new_list if i < x]
        eq = [i for i in new_list if i == x]
        hi = [i for i in new_list if i > x]

        new_list = quick_sort(low) + eq + quick_sort(hi)

    return new_list


def print_sorted(sort_type, item_list, passed_time, max_time):
    # print(f'  \033[3m\033[4m\033[34m{sort_type}\033[0m time: \033[36m{passed_time}\033[0m ns (\033[36m{int(100 * passed_time / max_time)}%\033[0m).\n{item_list}')
    print(f'  \033[3m\033[4m\033[34m{sort_type}\033[0m time: \033[36m{passed_time}\033[0m ns (\033[36m{(100 * passed_time / max_time):.3f}%\033[0m).')


if __name__ == '__main__':
    maxitem = 100
    itemcount = 2000
    items = [randint(1, maxitem) for i in range(itemcount)]
    # print(f'  \033[3m\033[4m\033[34mOriginal list:\033[0m\n{items}')
    tic1 = time.perf_counter_ns()
    new_items1 = bubble_sort(items)
    time1 = time.perf_counter_ns() - tic1
    tic2 = time.perf_counter_ns()
    new_items2 = shake_sort(items)
    time2 = time.perf_counter_ns() - tic2
    tic3 = time.perf_counter_ns()
    new_items3 = combo_sort(items)
    time3 = time.perf_counter_ns() - tic3
    tic4 = time.perf_counter_ns()
    new_items4 = insertion_sort(items)
    time4 = time.perf_counter_ns() - tic4
    tic5 = time.perf_counter_ns()
    new_items5 = selection_sort(items)
    time5 = time.perf_counter_ns() - tic5
    tic6 = time.perf_counter_ns()
    new_items6 = merge_sort(items)
    time6 = time.perf_counter_ns() - tic6
    tic7 = time.perf_counter_ns()
    new_items7 = shell_sort(items)
    time7 = time.perf_counter_ns() - tic7
    tic8 = time.perf_counter_ns()
    new_items8 = quick_sort(items)
    time8 = time.perf_counter_ns() - tic8
    maxtime = max(time1, time2, time3, time4, time5, time6, time7, time8)
    print_sorted('Bubble sort', new_items1, time1, maxtime)
    print_sorted('Shake sort', new_items2, time2, maxtime)
    print_sorted('Combo sort', new_items3, time3, maxtime)
    print_sorted('Insertion sort', new_items4, time4, maxtime)
    print_sorted('Selection sort', new_items5, time5, maxtime)
    print_sorted('Merge sort', new_items6, time6, maxtime)
    print_sorted('Shell sort', new_items7, time7, maxtime)
    print_sorted('Quick sort', new_items8, time8, maxtime)
