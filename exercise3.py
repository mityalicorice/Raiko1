"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""

wi = 'Это зима'
sp = 'Это весна'
su = 'Это лето'
fa = 'Это осень'
all_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
year = [wi, wi, sp, sp, sp, su, su, su, fa, fa, fa, wi] # Последовательность месяцев по сезонам в году
up_and_running = 'y'

while up_and_running == 'y': # Работаем ли дальше


    methodic = input('Метод решения задачи (list/dict): ')


    if methodic == 'list': # Решение через list:

        winter = [1, 2, 12]
        spring = [3, 4, 5]
        summer = [6, 7, 8]
        fall = [9, 10, 11]

        month_input = input('Введите месяц в виде целого числа от 1 до 12: ')
        while month_input.isdigit(): # Проверяем, что пользователь ввёл число
            if int(month_input) in all_months:
                if int(month_input) in winter:
                    print(wi)
                    up_and_running = input('Может, ещё раз? (y/n): ')
                    break
                elif int(month_input) in spring:
                    print(sp)
                    up_and_running = input('Может, ещё раз? (y/n): ')
                    break
                elif int(month_input) in summer:
                    print(su)
                    up_and_running = input('Может, ещё раз? (y/n): ')
                    break
                elif int(month_input) in fall:
                    print(fa)
                    up_and_running = input('Может, ещё раз? (y/n): ')
                    break
            else:
                month_input = input('Такого месяца нет. Введите месяц в виде целого числа от 1 до 12: ')
        else:
            up_and_running = input('Ой, что-то пошло не так. Попробовать снова? (y/n): ')


    elif methodic == 'dict': # Решение через dict:

        seasons_dict = dict(zip(all_months, year)) # Создаётся словарь из двух списков
        month_input = input('Введите месяц в виде целого числа от 1 до 12: ')
        while month_input.isdigit():  # Проверяем, что пользователь ввёл число
            if int(month_input) in all_months:
                print(seasons_dict.get(int(month_input)))
                up_and_running = input('Может, ещё раз? (y/n): ')
                break
            else:
                month_input = input('Такого месяца нет. Введите месяц в виде целого числа от 1 до 12: ')
        else:
            up_and_running = input('Ой, что-то пошло не так. Попробовать снова? (y/n): ')


    else:
        up_and_running = input('Ой, что-то пошло не так. Попробовать снова? (y/n): ')
