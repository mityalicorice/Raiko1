"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""

with open('my_file2.txt', 'r', encoding='utf-8') as f_obj:
    # content = f_obj.read()
    # print(content)
    line_count = len(open('my_file2.txt').readlines())
    print('Всего в файле', line_count, 'строк')
    result = [len(line.split(' ')) for line in f_obj]
    i = 0
    while i < int(line_count):
        print('В строке', i + 1, 'содержится', result[i], 'слов(а)')
        i += 1
