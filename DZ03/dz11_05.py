l = [3, 6, 8, 9, 1, 2]

print(list(map(lambda x: x[0] ** 3 * x[1], enumerate(l))))
