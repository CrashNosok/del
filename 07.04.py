'''
Импорты
'''

# первый способ (все функции из библиотеки доступны через
# название библиотеки и точку):
'''
import tkinter
root = tkinter.Tk()
root.mainloop() 
'''

# второй способ (все функции из библиотеки доступны через
# псевдоним и точку)
'''
import tkinter as tk
root = tk.Tk()
root.mainloop() 
'''

# третий способ (импортировать только нужное)
'''
from tkinter import Tk, Button
root = Tk()
but = Button(root, text='lalala')
but.pack()
root.mainloop()
'''

# четвертый способ (импортировать всё без псевдонимов)
'''
from tkinter import *
root = Tk()
root.mainloop()
'''

# Библиотека os (для работы с операционной системой)
# import os

# посмотреть текущую директорию проекта:
# print(os.getcwd())

# смена директории:
# os.chdir('C:/Users/Admin/Desktop/python_a')
# print(os.getcwd())

# посмотреть файла, которые находятся в директории
# print(os.listdir(path="."))

# создание папки
# os.mkdir('./new_papka')

# удаление файлов
# os.remove('./file.csv')

# удалит все файлы из дириктории
# files = os.listdir(path=".")
# for file in files:
#     os.remove(file)

# удалить дирикторию
# os.rmdir('./new_dirictory')   

# print(os.system('notepad'))

'''
кортеж (tuple) - неизменяемый список

создание кортежа 1 способ:
a1 = (12, 5, 7, 9, 32)

создание кортежа 2 способ:
a2 = 12, 5, 7, 9, 32
'''
# a2 = 12, 5, 7, 9, 32
# a3 = 1, 1, 1
# # объединение кортежей в 1
# a5 = a2 + a3
# print(a5)

# распаковка кортежей
# a = 1
# b = 2
# # tmp = b
# # b = a
# # a = tmp
# a, b = b, a
# print(a) # 2
# print(b) # 1

# a, b, c = 7, 6, 5
# a, b, c = c, a, b

'''
задача 1:
1) импорт библиотеки
2) создаете папку new (используя относительный путь)
3) перемещаетесь в папку new (используя относительный путь)
4) создаете папку new2 в текущей директории
'''
import os
# os.mkdir('./new')
# os.chdir('./new')
# os.mkdir('./new2')

'''
задача 2:
получить все файлы, которые находятся на рабочем столе
вывести их
'''
files = os.listdir(path="C:/Users/Admin/Desktop")
# print(files)
'''
задача 3:
используя задачу 2, вывести только те файлы, у которых
расширение '.txt'
'''
for file in files:
    if file[-4:] == '.txt':
        print(file)

'''
задача 4:
задача 3 без endswith
'''


