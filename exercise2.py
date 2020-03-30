"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property."""

class Clothes:
    fabric_consumption: float = 0.0
    name: str = "leaf"
    size: float = 0.0
    _all_clothes = []

    def __init__(self, name, size):
        self.name = name
        self.size = size
        Clothes._all_clothes.append(self)

    @staticmethod
    def summary_fabric_consumtion():
        sum = 0
        #print(Clothes._all_clothes)
        for x in Clothes._all_clothes:
            sum += x.fabric_consumption
        return sum

class Overcoat(Clothes):
    _size_flag = 'V'

    def __init__(self, name, size):
        super().__init__(name, size)

    @property
    def fabric_consumption(self):
        return (self.size / 6.5 + 0.5)

class Suit(Clothes):
    _size_flag = 'H'

    def __init__(self, name, size):
        super().__init__(name, size)

    @property
    def fabric_consumption(self):
        return (self.size * 2.0 + 0.3)

if __name__ == '__main__':
    overcoat = Overcoat('overcoat №1', 6.5)
    suit = Suit('suit №1', 0.35)
    print(Clothes.summary_fabric_consumtion())

