class Car:

    def __init__(self, speed, color, name, is_police):
        self.name = name
        self.is_police = is_police
        self.color = color
        self.speed = speed

    def go(self):
        print('Start')

    def stop(self):
        print('Stop')

    def turn(self, direction):
        print(f'Поворот {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60: print('Вы привысили скорость на:', self.speed-60)
        else: print(self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 400: print('Вы привысили скорость на:', self.speed-40)
        else: print(self.speed)


class PoliceCar(Car):
    pass

police = PoliceCar(60,'red/white','Zaz',True)
police.stop()
police.go()
police.show_speed()
police.turn("Направо")

town = TownCar(100,'blue','BMW',False)
town.show_speed()