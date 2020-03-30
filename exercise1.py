"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д."""

import random

from copy import deepcopy

class Matrix:
    #
    def __init__(self, init_matrix = [[]]):
        width = len(init_matrix[0]) if len(init_matrix) else 0
        # является ли матрица вообще матрицей
        for i, line in enumerate(init_matrix):
            if width is not len(line):
                print('init matrix is not a matrix actually')

        self.value = deepcopy(init_matrix)

    #
    def __str__(self):
        for line in self.value:
            for x in line: print('{:>4}'.format(x), end='')
            print('\n', end='')
        return ''
    #
    def __add__(self, matrix):
        result_matrix = []

        # проверка на длину
        if (len(matrix.value) is not len(self.value)):
            print('matrix dimensions(length) are different')
            return self.value

        for i, line in enumerate(self.value):
            # проверка на ширину
            if len(line) is not len(matrix.value[i]):
                print(f'{i} matrix dimensions(width) are different')
                return self.value

            #
            result_matrix.append([])
            for j, value in enumerate(line):
                result_matrix[-1].append(line[j] + matrix.value[i][j])

        return Matrix(result_matrix)

if __name__ == '__main__':
    # init matrix
    n, m = 4,6
    i_m = [[random.randint(-20, 20) for _ in range(m)]
         for _ in range(n)]
    m1 = Matrix(i_m)
    # print(f'first(init) matrix:\n{m1}') m1 выводится перед текстом
    print('first(init) matrix:\n'); print(m1)
    m2 = Matrix(
        [[random.randint(-20, 20) for _ in range(m)]
         for _ in range(n)]
    )
    # print('second matrix:\n',m2) выводит лишний пробел в первой строке матрицы
    # print(f'second matrix:\n{m2}') выводит матрицу перед текстом
    print('second matrix:\n'); print(m2)
    print('sum of matrixes:\n'); print(m1 + m2)

