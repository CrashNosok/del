from tkinter import *


def foo(event):
    Toplevel(root)


root = Tk()

# Рамка (Frame)
fra1 = Frame(root, width=500, height=100, bg='darkred', bd=2)
# bd - boderwidth - ширина рамки
fra2 = Frame(root, width=300, height=200, bg='green', bd=20)
fra3 = Frame(root, width=500, height=150, bg='darkblue', bd=5)

lab1 = Label(fra1, text='Первый лэйбл')
lab2 = Label(fra2, text='Второй лэйбл')

# шкала (Scale)
sca1 = Scale(fra3, orient=HORIZONTAL, length=300, from_=0, to=100, tickinterval=10,
             resolution=5, troughcolor='red')
sca2 = Scale(root, orient=VERTICAL, length=400, from_=0, to=2, tickinterval=0.1,
             resolution=0.1, troughcolor='white')
# orient - вертикально или горизонтально
# length - длина шкалы в пикселях
# from_ - с какого значения начинается шкала
# to - до какого значения
# tickinterval - интервал, через который отображаются метки шкалы
# resolution - минимальная длина отрезка,на которую можно передвинуть движок


# # полоса прокрутки (Scrollbar)
# frame2 = Frame(root, bg='red', bd=5)
# tx = Text(frame2, width=20, height=5)
# # command - показывает к чему будет привязан Scrollbar. привязываем к tx вертикально
# scr = Scrollbar(frame2, command=tx.yview)
# tx.configure(yscrollcommand=scr.set)
#
# frame2.pack()
# # side - сторона. с каакой стороны будет располагаться объект
# scr.pack(side='right', fill='y')
# tx.pack(fill='both')


# окно верхнего уровня (Toplevel)
tl = Toplevel(root, relief=FLAT, bd=10, bg='lightblue')
tl.title('Дочернее окно')
tl.minsize(width=400, height=200)
tl.maxsize(width=400, height=200)
but = Button(root, text='qqq')
but.bind('<Button-1>', foo)
but.pack()
# lab = Label(tl, text='НОВЫЙ Лабел')
# lab.pack()

fra1.pack()
fra2.pack()
fra3.pack()

lab1.pack()
lab2.pack()

sca1.pack()
sca2.pack()

root.mainloop()



























# from tkinter import *
#
#
# def foo(event):
#     print('hello world!!')
#
#
# def button_click(event):
#     # print(var) !!!!!!!!!!!! так нельзя
#     print(var.get())
#
#
# def button_click2(event):
#     print(c1.get(), c2.get())
#
#
# root = Tk()
#
# # виджеты
#
# # 1) кнопка (Button)
# but = Button(root, text='кнопка', width='10', height='2', bg='black',
#              fg='blue', font='Verdana 15')
# but.bind('<Button-1>', foo)
#
# # 2) метка (Label)
# lab = Label(root, text='Моя метка', font='Arial 20', width='15', bg='red')
#
# # 3) однострочное текстовае поле (Entry)
# ent = Entry(root, font='Arial 13', width='15', bg='lightblue')
#
# # 4) многострочное текстовое поле (Text)
# txt = Text(root, width=40, font='Verdana 12', wrap=WORD, height=5)
#
# # 5) радиокнопки (Radiobutton)
# # IntVar - специальная переменна от tkinter. в которой хранятся значения типа int
# var = IntVar()
# # var = 1 !!!!!!!!!НЕЛЬЗЯ
# var.set(1)
# # если выберут первую кнопку, то var будет равняться 1
# rad1 = Radiobutton(root, text='Первая', variable=var, value=1)
# # если выберут первую кнопку, то var будет равняться 2
# rad2 = Radiobutton(root, text='Вторая', variable=var, value=2)
# # если выберут первую кнопку, то var будет равняться 3
# rad3 = Radiobutton(root, text='Третья', variable=var, value=3)
# but2 = Button(root, text='check')
# but2.bind('<Button-1>', button_click)
#
# # флажки (Checkbutton)
# c1 = IntVar()
# c2 = IntVar()
# # если нажмут на первый флажок, то c1=1, если не нажмут, то c1=0
# che1 = Checkbutton(root, text='Первый', variable=c1, onvalue=1, offvalue=0)
# che2 = Checkbutton(root, text='Второй', variable=c2, onvalue=1, offvalue=0)
# but3 = Button(root, text='check2')
# but3.bind('<Button-1>', button_click2)
#
#
# # списки (Listbox)
# r = ['Linux', 'Python', 'Tk', 'Tkinter']
# # selectmod=SINGLE - можно выделить только 1 элемент
# # height=4 - показывает сколько элеменов отображается на 1 странице списка
# lis = Listbox(root, selectmod=SINGLE, height=4)
# for elem in r:
#     # insert - добавить. (1 аргумент - куда добавить. 2 аргумент - что добавить)
#     lis.insert(END, elem)
#
# lab.pack()
# but.pack()
# ent.pack()
# txt.pack()
#
# rad1.pack()
# rad2.pack()
# rad3.pack()
# but2.pack()
#
# che1.pack()
# che2.pack()
# but3.pack()
#
# lis.pack()
#
# root.mainloop()
