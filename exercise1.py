"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать
функцию type() для проверки типа. Элементы списка можно не запрашивать
у пользователя, а указать явно, в программе."""

my_first_list = [17, 0.13701, False, None, 'Абырвалг']

for ind, el in enumerate(my_first_list):
    print(ind, el)

up_and_running = input('Показать тип данных какого-либо элемента из спиcка? (да/нет) ')

while up_and_running == 'да':
    myindex = int(input('Введите индекс элемента (целое число от 0 до 4): '))

    if not 0 <= myindex <= 4:
        continue
    else:
        dataprint = my_first_list[int(myindex)]
        datatype = type(my_first_list[int(myindex)])

        print('Элемент с индексом', myindex, 'содержит следующие данные: "', dataprint, '", относящиеся к типу', datatype)
        up_and_running = input('Показать тип данных другого элемента? (да/нет) ')
        continue
    continue
