a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]

while len(a) > 0:
    item = a.pop(0)
    if a.count(item) == 0:
        print(item, end=' ')
    else:
        for i in range(a.count(item)):
            a.remove(item)
