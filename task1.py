# Урок 6. Задание 1:
#  Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#  Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
#  желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
#  третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
#  порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.


import time


class TrafficLight():

    red_color_wait = 7
    yellow_color_wait = 2
    green_color_wait = 4

    red_color_name = 'red'
    yellow_color_name = 'yellow'
    green_color_name = 'green'

    def __init__(self, color):
        self.__color = color
        print(
            f'\ncreated new object TrafficLight with the start color {self.__color}')

    def switch_light(self, color, wait_period):
        self.wait_period = wait_period
        print(
            f'turned on {color} light, time of waiting {self.wait_period} sec')
        time.sleep(self.wait_period)

    def running(self, color=''):

        if not color:
            loc_color = self.__color
        else:
            loc_color = color

        if loc_color == self.red_color_name:
            self.switch_light('red', self.red_color_wait)
            self.switch_light('yellow', self.yellow_color_wait)
            self.switch_light('green', self.green_color_wait)
        elif loc_color == self.yellow_color_name:
            self.switch_light('yellow', self.yellow_color_wait)
            self.switch_light('green', self.green_color_wait)
        else:
            self.switch_light('green', self.green_color_wait)

        print('cycle of switching is finished')


tl1 = TrafficLight('red')
tl1.running()

tl2 = TrafficLight('yellow')
tl2.running()

tl3 = TrafficLight('green')
tl3.running()

tl1 = TrafficLight('red')
tl1.running('yellow')
