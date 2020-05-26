from tkinter import *

root = Tk()
# root.geometry('400x400')

lab1 = Button(root, text='1', width=10, height=10)
lab2 = Button(root, text='2', width=10, height=10)
lab3 = Button(root, text='3', width=10, height=10)
lab4 = Button(root, text='4', width=10, height=10)

# позиционирование сеткой
lab1.grid(row=0, column=0)
lab2.grid(row=0, column=1)
lab3.grid(row=1, column=0)
lab4.grid(row=1, column=1)

root.mainloop()
