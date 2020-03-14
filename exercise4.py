"""4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй —
более сложная реализация без оператора **, предусматривающая использование цикла."""

up_and_running = 'да'

while up_and_running == 'да':
    def my_func(x, y):
        result = float(x) ** int(y)
        return print('Результат возведения числа x в степень y равен', result)

    x_inp = input('Введите действительное положительное число x: ')
    while True:
        try:
            x = float(x_inp)
            break
        except ValueError:
            x_inp = input('Введено неверное значение! Введите действительное положительное число x: ')

    y_inp = input('Введите целое отрицательное число y: ')
    while True:
        try:
            y = int(y_inp)
            break
        except ValueError:
            y_inp = input('Введено неверное значение! Введите целое отрицательное число y: ')

    my_func(x, y)

    up_and_running = input('Посчитать ещё что-нибудь? (да/нет) ')