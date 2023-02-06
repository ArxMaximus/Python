def minimum(*args, **kwargs):
    m = args[0]
    for i in args + tuple(kwargs.values()):
        if i < m:
            m = i
    return m


print(minimum(10, d=9))
print(minimum(2, 3, 4))
print(minimum(3, 5, 10, 6))
