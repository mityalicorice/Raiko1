"""6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools."""

import itertools, time
from sys import argv

script_name, num = argv

for el in itertools.count(int(num)):
    print(el)
    time.sleep(0.05)
