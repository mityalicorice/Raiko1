"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""

import json

with open('my_file7.txt', 'r', encoding='utf-8') as f_obj:

    a = f_obj.readlines()  # Сохраняется каждая строка как элемент списка 'a'

    line_count = len(open('my_file7.txt').readlines())  # Считаем количество организаций в файле (по количеству строк)

    all_firms = []  # В этом списке будут все фирмы, в т.ч. убыточные

    all_profits = []  # В этом списке будут прибыли и убытки

    profitable_firms = []  # В этом списке будут только фирмы без убытка

    only_profits = [] # В этом списке будут прибыли только прибыльных фирм

    i = 0
    while i < int(line_count):
        x = a[i].split(' ')
        name = x[0]  # Название компании
        profit = float(x[2]) - float(x[3])  # Прибыль организации (выручка минус издержки)
        print('Название:', name, '    Прибыль:', profit)  # Выводим название и прибыль
        all_firms.append(name)
        all_profits.append(profit)
        if profit > 0:
            profitable_firms.append(name)
            only_profits.append(profit)
        i += 1

    mid_profit = sum(map(float, only_profits)) / len(profitable_firms)  # Средняя прибыль (без учёта убыточных компаний)

    print('Средняя прибыль:', mid_profit)

    firms_and_profits = dict(zip(all_firms, all_profits))  # Словарь с фирмами и их прибылями
    mid_profit_dict = {'average_profit' : mid_profit}  # Словарь со средней прибылью
    firms_profits_midprofit = [firms_and_profits, mid_profit_dict]  # Список содержит два словаря

    with open('my_file7_data.json', 'w', encoding='utf-8') as file:
        json.dump(firms_profits_midprofit, file, ensure_ascii=False)  # Список сохраняется в виде json-объекта в файл

    with open('my_file7_data.json', 'r', encoding='utf-8') as file2:
        resurrect = json.load(file2)  # Воскрешается список из json-файла
        print(resurrect)
