"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
окончании ввода данных свидетельствует пустая строка."""

f = open('my_file1.txt', 'w')
f.close()

with open('my_file1.txt', 'a', encoding='utf-8') as f_obj:
    my_var = 1
    while my_var:
        my_var = input('Введите строку: ')
        f_obj.write(my_var)
        f_obj.write('\n')
