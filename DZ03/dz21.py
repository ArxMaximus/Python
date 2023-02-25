import math

class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def get_volume(self):
        return 4 * math.pi * self.radius ** 3 / 3

    def get_square(self):
        return 4 * math.pi * self.radius ** 2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, center):
        self.center = center

    def is_point_inside(self, x, y, z):
        return (self.center[0] - x) ** 2 + (self.center[1] - y) ** 2 + (self.center[2] - z) ** 2 <= self.radius ** 2


if __name__ == '__main__':
    my_sphere = Sphere((0, 0, 0), 0.6)
    print(f'\033[31mСфера:\033[0m\nРадиус: \033[34m{my_sphere.get_radius()}\033[0m\n'
          f'Объем: \033[34m{my_sphere.get_volume():.3f}\033[0m\n'
          f'Площадь поверхности: \033[34m{my_sphere.get_square():.3f}\033[0m\n'
          f'Координаты центра: \033[34m{my_sphere.get_center()}\033[0m\n'
          f'Лежит ли точка (0, -1.5, 0) внутри: \033[34m{my_sphere.is_point_inside(0, -1.5, 0)}\033[0m\n')
    my_sphere.set_radius(1.6)
    print(f'Устанавливаем радиус: \033[34m{my_sphere.get_radius()}\033[0m\n'
          f'Лежит ли точка (0, -1.5, 0) внутри: \033[34m{my_sphere.is_point_inside(0, -1.5, 0)}\033[0m\n')
