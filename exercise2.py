"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год
рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать
вывод данных о пользователе одной строкой."""

up_and_running = 'да'

while up_and_running == 'да':
    def all_data():
        username = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        birth_year = input('Введите год рождения: ')
        city = input('Введите город проживания: ')
        email = input('Введите e-mail: ')
        phone = input('Введите номер телефона: ')
        user_data = ('Имя: {username}; Фамилия: {surname}; Год рождения: {birth_year}; Город проживания: {city}; '
                     'e-mail: {email}; Телефон: {phone}'.format(username=username,
                                                                surname=surname,
                                                                birth_year=birth_year,
                                                                city=city,
                                                                email=email,
                                                                phone=phone))
        return user_data


    print(all_data())
    up_and_running = input('Ещё раз? (да/нет) ')
