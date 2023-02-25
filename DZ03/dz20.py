class Automobile:

    def __init__(self, model, year, manufacturer, power, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.power = power
        self.color = color
        self.price = price

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_power(self, power):
        self.power = power

    def get_power(self):
        return self.power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def print_info(self):
        print(f'********** Данные автомобиля **********\nНазвание модели: \033[35m{self.model}\033[0m\n'
              f'Производитель: \033[35m{self.manufacturer}\033[0m\n'
              f'Мощность двигателя: \033[35m{self.power}\033[0m\n'
              f'Цвет машины: \033[35m{self.color}\033[0m\n'
              f'Цена: \033[35m{self.price}\033[0m\n=======================================')


if __name__ == '__main__':
    car = Automobile('X7 M50i', '2021', 'BMW', '530 л.с.', 'white', '10790000')
    car.print_info()
    car.set_model('X6 x35i')
    car.set_year('2009')
    car.set_manufacturer('BMW AG Germany')
    car.set_power('306 л.с.')
    car.set_color('silver')
    car.set_price('1750000')
    print(f'********** Данные автомобиля **********\nНазвание модели: \033[34m{car.get_model()}\033[0m\n'
          f'Производитель: \033[34m{car.get_manufacturer()}\033[0m\n'
          f'Мощность двигателя: \033[34m{car.get_power()}\033[0m\n'
          f'Цвет машины: \033[34m{car.get_color()}\033[0m\n'
          f'Цена: \033[34m{car.get_price()}\033[0m\n=======================================')
