class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner = (str), __model = (str), __color = (str), __engine_power = (int)):
        self.owner = owner
        self.model = __model
        self.color = __color
        self.engine_power = __engine_power

    def set_color(self, new_color = (str)):
        for i in Vehicle.__COLOR_VARIANTS:
            if new_color.lower() == i.lower():
                self.color = new_color
                break
        else:
            print(f'Нельзя сменить цвет на {new_color}')

    def get_model(self):
        print(f'Модель: {self.model}')

    def get_horsepower(self):
        print(f'Мощность: {self.engine_power}')

    def get_color(self):
        print(f'Цвет: {self.color}')

    def print_info(self):
        print(f'Модель: {self.model}\nМощность двигателя: {self.engine_power}\nЦвет: {self.color}\nВладелец: {self.owner}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
