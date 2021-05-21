# использование time внутри которго есть функция sleep для заморозки программы на определенное кол-во секундfr

from time import sleep


class TrafficLight:
    __color = {"Красный": 7, 'Желтый': 2, 'Зеленый': 30}

    def __init__(self):
        for key, value in self.__color.items():
            print(key)
            sleep(value)

    # По заданию должна быть функция running

    def running(self):
        self.__init__()


light = TrafficLight()
light.running()

