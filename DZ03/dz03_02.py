# Выводим элементы списка с четными индексами

MyList = [input('--> ') for num in [0] * int(input('Введите количество элементов: '))]
print(''.join(item + ' ' if num % 2 == 0 else '' for num, item in enumerate(MyList)))
