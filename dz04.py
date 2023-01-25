print('Выберите операцию:\n1 - "r" - применяет унарный минус к операнду\n2 - "+" - сложение')
print('3 - "-" - вычитание\n4 - "/" - деление\n5 - "*" - умножение')
print('6 - "%" - деление по модулю (остаток от деления)\n7 - "<" - минимальное из двух чисел')
print('8 - ">" - максимальное из двух чисел')
print('9 - выход, 0 - вывод справки')
while True:
    action = input('Выберите действие: ')
    try:
        action = int(action)
        if action == 0:
            print('Выберите операцию:\n1 - "r" - применяет унарный минус к операнду\n2 - "+" - сложение')
            print('3 - "-" - вычитание\n4 - "/" - деление\n5 - "*" - умножение')
            print('6 - "%" - деление по модулю (остаток от деления)\n7 - "<" - минимальное из двух чисел')
            print('8 - ">" - максимальное из двух чисел')
            print('9 - выход, 0 - вывод справки')
        elif action == 1:
            num = input('Ввеите число: ')
            print('-' + num)
        elif action == 9:
            break
        elif 1 < action < 9:
            first = input('Введите первое число: ')
            second = input('Введите второе число: ')
            try:
                first = int(first)
                second = int(second)
                match action:
                    case 2:
                        print('Сумма равна: ' + str(first + second))
                    case 3:
                        print('Разность равна: ' + str(first - second))
                    case 4:
                        print('Частное равно: ' + str(first / second))
                    case 5:
                        print('Произведение равно: ' + str(first * second))
                    case 6:
                        print('Остаток от деления равен: ' + str(first % second))
                    case 7:
                        print('Минимальное из двух чисел: ' + str(first if first < second else second))
                    case 8:
                        print('Максимальное из двух чисел: ' + str(first if first > second else second))
            except ZeroDivisionError:
                print('На 0 делить нельзя')
            except ValueError:
                print('Введено неверное число!')
        else:
            print('Выбрано недоступное действие!')
    except ValueError:
        print('Вас просили цифру!')
    print()
print('Спасибо, что выбрали наш калькулятор!')