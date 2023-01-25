from random import random

number = int(random() * 100 + 1)
count = 1
while True:
    num = input('Введите число от 1 до 100: ')
    try:
        num = int(num)
        if num == 0:
            print('Очень жаль, что вы нас покидаете!')
            break
        if num < 1 or num > 100:
            raise ValueError
        if num == number:
            print('Вы угадали загаданное число с {}-го раза!'.format(count))
            break
        if num < number:
            print('Загаданное число больше')
        else:
            print('Загадочное число меньше')
        count += 1
    except ValueError:
        print('Введено неверное число!')



