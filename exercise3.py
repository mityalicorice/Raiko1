"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

number = input("Введите любое целое положительное число: n = ")
nn = int(2*str(number))
nnn = int(3*str(number))
my_sum = int(number) + nn + nnn
print("n + nn + nnn =", number, "+", nn, "+", nnn, "=", my_sum)
