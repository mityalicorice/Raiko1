"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове."""

user_str = input('Введите строку из нескольких слов, разделённых пробелами: ')

listed_str = user_str.split(' ') # Из строки делаем список

i = 0

while i < len(listed_str):

    current_elem = listed_str[i]  # Текущий элемент списка
    elem_length = len(current_elem)  # Длина слова в списке

    if elem_length <= 10: # Длина слова до 10 символов включительно
        print(i + 1, current_elem)
        i = i + 1
        continue
    else: # Длина слова более 10 символов
        name_str = current_elem[:10]
        print(i + 1, name_str, '...')
        i = i + 1
        continue
    break
