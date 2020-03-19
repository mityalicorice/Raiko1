"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов."""

def my_func():
    arg1 = int(input('Введите первое число: '))
    arg2 = int(input('Введите второе число: '))
    arg3 = int(input('Введите третье число: '))
    my_list = sorted([arg1, arg2, arg3], reverse=True)
    result = my_list[0] + my_list[1]
    return result

print('Сумма двух наибольших аргументов равна', my_func())