class Vehicle:
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    __COLOR_VARIANTS = ['небесный', 'мятный', 'снежный', 'лазурный', 'серебристый', 'изумрудный', 'алый']
    def set_color(self, new_color):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
           self.__color = new_color
        else:
            if new_color not in Vehicle.__COLOR_VARIANTS:
                print(f"Цвет '{new_color}' не поддерживается. Возможные цвета: {', '.join(Vehicle.__COLOR_VARIANTS)}")

    def get_model(self):
        return print(f"Модель :",self.__model)
    def get_horsepower(self):
        return print(f"Мощность двигателя :",self.__engine_power)
    def get_color(self):
        return print(f"Цвет :",self.__color)
    def print_info(self):
        return print(f"Владелец : {self.owner}\nМодель : {self.__model}\nМощность двигателя : {self.__engine_power}\nЦвет : {self.__color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'красный')
vehicle1.print_info()
vehicle1.set_color('пурпурный')
vehicle1.set_color('изумрудный')
vehicle1.owner = 'Vasyok'


vehicle1.print_info()