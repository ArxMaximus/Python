a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))
print(a if a > b and a > c else b if b > a and b > c else c)
