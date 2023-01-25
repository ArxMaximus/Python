# Вариант 1

def var1(mW, mH, n):
    print('Алгоритм со строками')
    field1 = ('*' * n + ' ' * n) * (mW // 2) + '*' * n * (mW % 2) + '\n'
    field2 = (' ' * n + '*' * n) * (mW // 2) + '\n'
    field = (field1 * n + field2 * n) * (mH // 2) + field1 * n * (mH % 2)
    print(field)


# Вариант 2

def var2(mW, mH, n):
    print('Алгоритм с циклами')
    i = 1
    while i <= mH:
        k = 1
        while k <= n:
            j = 1
            while j <= mW:
                t = 1
                while t <= n:
                    if ((i + j) % 2 == 0):
                        print('*', end='')
                    else:
                        print(' ', end='')
                    t += 1
                j += 1
            print()
            k += 1
        i += 1


if __name__ == '__main__':
    mW = int(input('Ширина поля: '))
    mH = int(input('Высота поля: '))
    n = int(input('Размер клетки: '))
    v = input('Вариант алгоритма (1 - строки, 2 - циклы):')
    if v == '1':
        var1(mW, mH, n)
    else:
        var2(mW, mH, n)
