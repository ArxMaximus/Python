import math


square_circle = lambda r: math.pi * r * r
square_rect = lambda a, b: a * b
square_trapeze = lambda a, b, h: h * (a + b) / 2

c_rad = 2
r_length, r_width = 10, 13
tr_a, tr_b, tr_h = 7, 5, 3

print(f'Площадь окружности радиуса {c_rad}: {square_circle(c_rad)}')
print(f'Площадь прямоугольника размером {r_length} х {r_width}: {square_rect(r_length, r_width)}')
print(f'Площадь трапеции для a = {tr_a}, b = {tr_b}, h = {tr_h}: {square_trapeze(tr_a, tr_b, tr_h)}')
