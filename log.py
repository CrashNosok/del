'''
Работа с файлами
1) открыть файл:
file = open('filename.txt', '...')
open(1, 2)
1 - название файла (путь до него)
2 - режим открытия файла
'r'	открытие на чтение (является значением по умолчанию).
'w'	открытие на запись, содержимое файла удаляется, 
    если файла не существует, создается новый.
'a'	открытие на дозапись, информация добавляется в конец файла.
'+', 'ra' открытие на чтение и запись

запись в файл
file.write('str')
str - то, что записать в файл
'''
# запись в файл
# file = open('aaaaaaaaaaaaaaa.txt', 'w', encoding='utf-32')
# file.write('some text')
# file.close()

# чтение из файла
file = open('aaaaaaaaaaaaaaa.txt')
# читаем весь файл
# text = file.read()

# читаем первую строку
# text = file.readline()

# получаем массив строк
# text = file.readlines()

# print(text)

# чтение файла по строкам
# for line in file:
#     print(line, end='')

file.close()
