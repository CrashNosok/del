# csv файлы
'''
# стандартная работа с файлом
f = open('file.txt', 'r')
msg = f.read()
f.close()
print(msg)

# работа с файлом с помощью менеджера контектов with
# пример делает то же самое, что и пример выше:
with open('file.txt', 'r') as f:
    msg = f.read()
print(msg)
'''

# 1 способ импорта:
'''
import tkinter
root = tkinter.Tk()
root.mainloop()
'''
# 2 способ импорта:
'''
import tkinter as tk
root = tk.Tk()
root.mainloop()
'''
# 3 способ импорта:
'''
from tkinter import Tk, Button
root = Tk()
but = Button(root)
but.pack()
root.mainloop()
'''
# 4 способ импорта:
'''
from tkinter import *
root = Tk()
root.mainloop()
'''

# для работы с csv файлами используем модуль csv
import csv

# строка для csv файла
row = ['Bob', 12]
# несколько строк для csv файла
rows = [
    ['Alice', 18],
    ['John', 10],
    ['Mikle', 11]
]
# print(rows[1][0]) # John

'''
# запись в csv файл:
with open('d.csv', 'w', newline='', encoding='utf-8') as f:
    # получам объект для работы с записью в csv:
    writer = csv.writer(f)
    # запис в файл одной строки:
    writer.writerow(row)
    # запись нескольких строчек:
    writer.writerows(rows)
'''
'''
# чтение из csv файла
with open('d.csv', 'r', newline='', encoding='utf-8') as f:
    # получам объект для работы с чтением csv:
    reader = csv.reader(f)
    # читаем по одной строчке через цикл:
    for row in reader:
        print(row)
'''
'''
задача 1:
создать файл, в котором есть 
5 объектом (имя,возраст)
'''
rows = [
    ['Alice', 18],
    ['John', 10],
    ['Mikle', 11],
    ['Bob', 12],
    ['Alex', 19],
]

# with open('file.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(rows)

'''
задача 2:
создать список rows и в этот список добавить все строки из csv файла
в конце вывести этот массив
'''
rows = []
with open('file.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)
print(rows)
print()
'''
задача 3:
посчитать общий возраст (сумму) всех объектов csv файла
'''
age = 0
with open('file.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        age += int(row[1])
print(age)
'''
задача 4:
посчитать среднеарифметический возраст всех объектов csv файла
'''
