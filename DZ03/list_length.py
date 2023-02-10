def count_items(item_list):
    """
    Counts total length of given list including nested lists


    :param item_list: source list
    :return: tuple: count of elements and maximum nested level
    """
    stack = []
    pos = 0
    level = 0
    maxlevel = 0
    count = 0
    pointer = item_list
    while not (pos == len(item_list) and level == 0):
        if isinstance(pointer[pos], list):
            stack.append(pos)
            stack.append(pointer)
            pointer = pointer[pos]
            pos = 0
            level += 1
            if level > maxlevel:
                maxlevel = level
        else:
            count += 1
            pos += 1
            while pos == len(pointer) and level > 0:
                pointer = stack.pop()
                pos = stack.pop()
                pos += 1
                level -= 1
    return count, maxlevel


names = ['Adam', ['Bob', ['Chet', 'Cat', ['Victor', 'Sergey', ['Olga', 'Helena']]], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill', ['Ivan', 'Petr', 'Sidor']], 'Ann']

if __name__ == '__main__':
    print(names)
    print('\033[3m\033[34mElements count:\033[0m {}, \033[3m\033[34mmaximum nesting level:\033[0m {}'.format(*count_items(names)))
