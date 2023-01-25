print('Выбор фигуры:\n1 - треугольник\n2 - прямоугольник\n3 - круг')
shape = input(': ')
try:
    shape = int(shape)
    if shape < 1 or shape > 3:
        raise ValueError
    match shape:
        case 1:
            try:
                a = int(input('Введите сторону a = '))
                b = int(input('Введите сторону b = '))
                c = int(input('Введите сторону c = '))
                p = (a + b + c) / 2
                print('Плошадь равна ', round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 3))
            except ValueError:
                print('Необходимо целое число')
        case 2:
            try:
                a = int(input('Введите сторону a = '))
                b = int(input('Введите сторону b = '))
                print('Плошадь равна ', round(a * b, 3))
            except ValueError:
                print('Необходимо целое число')
        case 3:
            try:
                r = int(input('Введите радиус = '))
                print('Плошадь равна ', round(3.141592654 * r * r, 3))
            except ValueError:
                print('Необходимо целое число')
except ValueError:
    print('Необходимо число от 1 до 3.')
