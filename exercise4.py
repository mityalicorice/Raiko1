"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

my_num = int(input("Введите целое положительное число: "))
my_num2 = my_num
largest = 0
while my_num > 0:
    r = my_num % 10
    if largest < r:
        largest = r
    my_num = int(my_num / 10)

print("Самая большая цифра в числе", my_num2, "— это", largest)