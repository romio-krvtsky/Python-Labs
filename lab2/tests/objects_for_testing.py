import math


class Processor:

    def __init__(self, clock_rate):
        self.__clock_rate = clock_rate

    def __eq__(self, other):
        return self.__clock_rate == other.__clock_rate

    def get_info(self):
        print(f'Clock rate of processor: {self.__clock_rate} Hz')


class PC:

    def __init__(self,
                 brand: str,
                 model: str,
                 height: float,
                 year_of_release: int,
                 price: int,
                 processor: Processor):
        self.__brand = brand
        self.__model = model
        self.__height = height
        self.__year_of_release = year_of_release
        self.__price = price
        self.__processor = processor

    def __eq__(self, other):
        return self.__model == other.__model \
               and self.__brand == other.__brand \
               and self.__height == other.__height \
               and self.__year_of_release == other.__year_of_release \
               and self.__price == other.__price \
               and self.__processor == other.__processor

    def get_info(self):
        print(f'Brand: {self.__brand}')
        print(f'Model: {self.__model}')
        print(f'Height: {self.__height}')
        print(f'Year of release: {self.__year_of_release}')
        print(f'Price: {self.__price}')
        self.__processor.get_info()

    def turn_on(self):
        print(f'PC {self.__brand} {self.__model} is on!')


def func_with_builtin_func(arr: list):
    return sorted(arr)


mes = 'halo'


def func_with_closure(x: int):
    global mes
    print(mes)

    def increase_value(interval: int):
        return x + interval

    return increase_value(5)


c = 2


def Butoma_function(x, y):
    global c
    return math.sin(x * y * c)
