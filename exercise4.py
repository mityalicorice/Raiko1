"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""

with open('my_file4a.txt', 'r', encoding='utf-8') as old_file:
    with open('my_file4b.txt', 'w', encoding='utf-8') as new_file:
        while True:
            old_line = old_file.readline()
            print(old_line)
            if old_line.__contains__('1'):
                new_line = 'Один — 1\n'
            elif old_line.__contains__('2'):
                new_line = 'Два — 2\n'
            elif old_line.__contains__('3'):
                new_line = 'Три — 3\n'
            elif old_line.__contains__('4'):
                new_line = 'Четыре — 4'
            else:
                new_line = ''

            new_file.write(new_line)
            if not old_line:
                break