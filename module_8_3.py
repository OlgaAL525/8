class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message



class IncorrectCarNumber(Exception):
    def __init__(self, message):
        self.message = message



class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        if self.__is_valid_numbers() == True and self.__is_valid_vin() == True:
            print(f'{model} успешно создан')


    def __is_valid_vin(self):
        try:
            if type(self.__vin) != int:
                raise IncorrectVinNumber('Некорректный тип vin номера')
            if self.__vin < 1000000 or self.__vin > 9999999:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        except IncorrectVinNumber as e:
            print(f'{e.message}')
        else:
            return True


    def __is_valid_numbers(self):
        try:
            if type(self.__numbers) != str:
                raise IncorrectCarNumber('Некорректный тип данных для номеров')
            if len(self.__numbers) != 6:
                raise IncorrectCarNumber('Неверная длина номера')
        except IncorrectCarNumber as e:
            print(f'{e.message}')
        else:
            return True





first = Car('Модель1', 1200000, '123dur')
second = Car('Модель 2', 100, '456afj')
third = Car('Модель 3', 1000010, [123])
