"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата."""

class Complex:
    a:float = 0
    b:float = 0

    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return('{a} + {b}i'.format(a=self.a, b = self.b))

    def __add__(self, other):
        return Complex(self.a+other.a, self.b+other.b)

    def __mul__(self, other):
        return Complex(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a
        )

if __name__ == '__main__':
    a = Complex(7, 3)
    print('a =', a)
    b = Complex(-12, 2)
    print('b =', b)
    print('a + b =', a + b)
    print('a * b =', a * b)
    print(f"multiplication by build-in 'complex': {complex(7,3) * complex(-12,2)}")

