"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой."""

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

