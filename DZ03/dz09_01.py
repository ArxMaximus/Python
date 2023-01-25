d1 = ['red', 'green', 'blue']
d2 = ['#FF0000', '#008000', '#0000FF']

# Вариант 1
# d = {d1[i]: d2[i] for i in range(len(d1))}

# Вариант 2
# d = {j: d2[i] for i, j in enumerate(d1)}

# Вариант 3
d = dict(zip(d1, d2))

print(d)
