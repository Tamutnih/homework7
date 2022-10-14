# Задание 4.
# Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
# speed, color, name, is_police(булево).
# А также публичные методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула(куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс публичный метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'acceleration to  {speed} km/h')

    def stop(self):
        self.speed = 0
        print('stop')

    def turn(self, direction: str):
        if self.speed > 0:
            print(f'turn {direction}')
        else:
            print('cannot turn - stand')

    def show_speed(self):
        print(f'speed {self.speed} km/h')


class TownCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'attention! speed exceeded {self.speed} km/h')
        else:
            print(f'speed {self.speed} km/h')


class SportCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'attention! speed exceeded {self.speed} km/h')
        else:
            print(f'speed {self.speed} km/h')


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True


def test_drive(vehicle):
    print(
        f"drive {'police_car' if vehicle.is_police else 'civil'} car {vehicle.name}, color {vehicle.color}")
    vehicle.go(40)
    vehicle.show_speed()
    vehicle.turn('right')
    vehicle.stop()
    vehicle.show_speed()
    vehicle.turn('left')
    vehicle.go(60)
    vehicle.show_speed()
    vehicle.go(120)
    vehicle.show_speed()
    vehicle.stop()
    print("finish drive", end="\n\n")
