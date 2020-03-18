"""6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools."""

import itertools
import time

my_list = ['Work it harder',
           'Make it better',
           'Do it faster',
           'Makes us stronger',
           'More than ever',
           'Hour after',
           'Our work is',
           'Never over']

i = 0
for elem in itertools.cycle(my_list):
    print(elem)
    time.sleep(1)
    i += 1
