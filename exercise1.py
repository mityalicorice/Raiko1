"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""

class Date():
    value: str = ''
    def __str__(self):

        #return(f'{self.day}-{self.month}-{self.year}')
        return self.value
    def __init__(self, string):
        # day, month, year = string.split('-')
        # self.day   = day
        # self.month = month
        # self.year  = year
        self.value = string

    @classmethod
    def to_int(cls, string):
        day, month, year = string.split('-')
        return (int(day), int(month), int(year))

    @staticmethod
    def is_valid(string):
        day, month, year = string.split('-')
        try:
            day, month, year = int(day), int(month), int(year)
            if (month not in range(1,13)
                or day not in range(1,32)
                or year == 0
            ):
                print(day, month, year)
                raise ValueError

        except ValueError:
            return False
        return True

if __name__=='__main__':
    print(Date('12-1-2000'))
    print(Date.to_int('17-04-1992'))
    print(Date.is_valid('12-12-12'))

