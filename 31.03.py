import csv

'''
# Менеджер контекста

# старый способ открытия файла:
f = open('file.txt', 'r')
msg = f.read()
f.close()
print(msg)

# аналогичный вариант с менеджер контекста:
with open('file.txt', 'r') as f:
    msg = f.read()
print(msg)
'''

# Работа с csv форматом
# import csv
'''
# строка для записи в csv файл
header = ['Name', 'Age', 'Weight']
data = [
    ['Bob', 12, 40],
    ['Alice', 18, 50],
    ['John', 60, 120]
]

# запись в csv файл
with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    # получаем объект для работы с csv файлом
    writer = csv.writer(f)
    # запись в csv файл одной строки:
    writer.writerow(header)
    # запись в csv файл нескольких строк:
    writer.writerows(data)
'''

# чтение csv файла
# with open('data.csv', 'r', encoding='utf-8') as f:
#     # получаем объект для чтения с csv файлом
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# задача 1:
# посчитать сумму возрастов всех людей из файла
# age = 0
# with open('data.csv', 'r', encoding='utf-8') as f:
#     # получаем объект для чтения с csv файлом
#     reader = csv.reader(f)
#     i = 0
#     for row in reader:
#         # в первой строчке - заголовок. её нужно пропустить
#         if i == 0:
#             i = 1
#             continue
#         age += int(row[1])
# print(age)

'''
задача 1:
написать функцию, которая принимает название 
файла и двумерный массив с информацией
функция должна в этот файл записать информацию (csv)
'''
def create_csv_file(file, data):
    with open(file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

'''
задача 2:
написать функцию, которая принимает название файла
и 1-мерный массив для записи в конец этого файла
'''
def append_row_to_csv_file(file, row):
    with open(file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)
'''
задача 3:
написать функцию, которая принимает название файла
функция возвращает двумерный массив с информацией из
файла (используйте append())
'''
def get_info_from_csv(file):
    rows = []
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
    return rows

'''
задача 4:
написать функцию, которая принимает название файла
и 1 массив для записи в НАЧАЛО этого файла
'''

data2 = [
    ['Bob', 12, 40],
    ['Alice', 18, 50],
    ['John', 60, 120]
]
create_csv_file('ttt.csv', data2)
user = ['Mikle', 6, 20]
append_row_to_csv_file('ttt.csv', user)
users = get_info_from_csv('ttt.csv')
print(users)
