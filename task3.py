# Задание 3.
# Реализовать базовый класс Worker(работник),
# в котором определить публичные атрибуты name, surname, position(должность),
# и защищенный атрибут income(доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position(должность) на базе класса Worker. В классе Position реализовать публичные методы
# получения полного имени сотрудника(get_full_name) и дохода с учетом премии(get_total_income).
# Проверить работу примера на реальных данных(создать экземпляры класса Position, передать данные,
#                                             проверить значения атрибутов, вызвать методы экземпляров).
# П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
# __str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.

from unicodedata import name


class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

    def __str__(self):
        return 'salary'


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


name = Position('Anton', 'Kulakov', 'programmer', 100000, 20000)
print(name.get_full_name())
print(name.position)
print(name.get_total_income())
