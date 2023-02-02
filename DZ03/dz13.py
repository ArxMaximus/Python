# На занятии был задача: вывести из словаря первые 2 элемента
# Придумал 4 варианта.

d = {'c': 3, 'a': 1, 'b': 2, 'd': 4}

# Вариант 1
# Преимущество - в 1 строку. Недостаток - перебирает весь список, а не только первые 2 элемента
# v = {l[0]: l[1] for k, l in enumerate(d.items()) if k < 2}

# Вариант 2
# x = iter(d.keys())
# y = iter(d.values())
# v = {next(x): next(y) for i in range(2)}

# Вариант 3
# v = {}
# x = iter(d.items())
# for i in range(2):
#     v.update({*[next(x)]})

# Вариант 4
# Строк две, зато только перебираются только первые два элемента
x = iter(d.items())
v = dict(map(lambda i: next(x), range(2)))

print(v)
