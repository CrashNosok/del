from tkinter import *

root = Tk()

'''
переменные в tkinter

StringVar() - для строк
IntVar() - целое число
DoubleVar() - дробное
BooleanVar() - булевые значениие (True, False)

у этих переменных есть 2 специальных метода (доступные через точку)
set() - установить значение
get() - получить значение

# пример:

a = IntVar()

ТАК НЕЛЬЗЯ!!!!!!!!!!!!
a = 90
print(a)

ТАК МОЖНО
a.set(90)
print(a.get())
'''

def check_radio(event):
    answer = var.get()
    if answer == 0:
        print('right answer')
    else:
        print('wrong answer')


def check_check(event):
    result = 0
    if var0.get() == 'yes' and var2.get() == 'yes' and var1.get() == 'no':
        result += 2
    elif (var0.get() == 'yes' or var2.get() == 'yes') and var1.get() == 'no':
        result += 1
    print(f'Вы набрали {result} баллов')
    

var = IntVar()
var.set(0)
lab = Label(root, text='На какой цвет можно переходить дорогу?')
rad0 = Radiobutton(root, text='зелёный', variable=var, value=0)
rad1 = Radiobutton(root, text='красный', variable=var, value=1)
rad2 = Radiobutton(root, text='жёлтый', variable=var, value=2)
but = Button(root, text='click me!')
but.bind('<Button-1>', check_radio)

lab.pack()
rad0.pack()
rad1.pack()
rad2.pack()
but.pack()

var0 = StringVar()
var1 = StringVar()
var2 = StringVar()

var0.set('no')
var1.set('no')
var2.set('no')

lab2 = Label(root, text='Выберите хищников')
ch0 = Checkbutton(root, text='лиса', variable=var0, onvalue='yes', offvalue='no')
ch1 = Checkbutton(root, text='заяц', variable=var1, onvalue='yes', offvalue='no')
ch2 = Checkbutton(root, text='медведь', variable=var2, onvalue='yes', offvalue='no')

but2 = Button(root, text='check')
but2.bind('<Button-1>', check_check)

lab2.pack()
ch0.pack()
ch1.pack()
ch2.pack()
but2.pack()

root.mainloop()
