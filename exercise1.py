"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль."""

up_and_running = 'да'

while up_and_running == 'да':
    def division():
        num_1 = float(input('Введите делимое: '))
        num_2 = float(input('Введите делитель: '))
        if num_2 == 0:
            print('Делить на ноль нельзя!')
            num_2 = float(input('Введите другой делитель: '))
        else:
            pass
        num_3 = num_1 / num_2
        return num_3

    result = division()
    print('Результат деления:', result)
    up_and_running = input('Поделить ещё что-нибудь? (да/нет) ')

