from random import randint
import time


def bubble_sort(item_list):
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


if __name__ == '__main__':
    maxitem = 100
    itemcount = 20
    items = [randint(1, maxitem) for i in range(itemcount)]
    print(items, end='\n\n')
    tic = time.perf_counter_ns()
    new_items = bubble_sort(items)
    toc = time.perf_counter_ns()
    print(f'Bubble sort time: \033[36m{toc - tic}\033[0m ns.\n{new_items}\n')
    tic = time.perf_counter_ns()
    new_items2 = shake_sort(items)
    toc = time.perf_counter_ns()
    print(f'Shake sort time: \033[36m{toc - tic}\033[0m ns.\n{new_items2}\n')
