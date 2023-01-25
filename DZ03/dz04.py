from random import randint

print('Заполнить список из 10 элементов случайными числами. Найти максимальный элемент списка и переместить его в начало списка.\n')

mas = [randint(10, 99) for i in range(10)]
print(mas)
print('Max: ', max(mas))
mas.insert(0, mas.pop(mas.index(max(mas))))
print(mas, '\n\n')

print('Заполнить список из 10 элементов случайными числами, как положительными, так и отрицательными.')
print('Изменить этот список таким образом, чтобы все отрицательные элементы оказались в конце.\n')

mas = [randint(-20, 20) for i in range(10)]
print(mas)
mas.sort(reverse=True)
print(mas, '\n\n')

print('Заполнить список из 10 элементов случайными числами. Удалить все элементы, расположенные перед минимальным элементом списка.\n')
mas = [randint(10, 99) for i in range(10)]
print(mas)
print('Min: ', min(mas))
print('Index min: ', mas.index(min(mas)))
mas = mas[mas.index(min(mas)):]
print(mas)