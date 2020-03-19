"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников."""

with open('my_file3.txt', 'r', encoding='utf-8') as f_obj:
    a = f_obj.readlines() # Сохраняется каждая строка как элемент списка 'a'
    all_staff = dict(line.split(' ') for line in a) # Создаётся словарь = {'Фамилия' : 'зарплата'}
    employees = list(all_staff.keys()) # Отдельно список сотрудников
    wages = [float(x) for x in list(all_staff.values())] # Отдельно все зарплаты
    middle_wage = sum(wages) / len(employees) # Средняя величина дохода сотрудников
    all_staff2 = dict(zip(employees, wages)) # Теперь зарплата в словаре хранится как float
    underpaid = {key:value for (key, value) in all_staff2.items() if value < 20000}
    print('Все сотрудники и их оклады:', all_staff2)
    print('Сотрудники с окладом менее 20000:', underpaid)
    print('Средняя величина дохода сотрудников: ', middle_wage)
