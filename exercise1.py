"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами."""

from sys import argv

script_name, first_param, second_param, third_param = argv

work_hours = float(first_param)
hourly_wage = float(second_param)
bonus = float(third_param)
pay = work_hours * hourly_wage + bonus

print('Выработка в часах:', work_hours)
print('Ставка в час:', hourly_wage)
print('Премия:', bonus)
print('Заработная плата составляет:', pay)
