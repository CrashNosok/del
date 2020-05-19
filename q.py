from tkinter import *


def foo(event):
    print('hello world!!')


def button_click(event):
    # print(var) !!!!!!!!!!!! так нельзя
    print(var.get())


def button_click2(event):
    print(c1.get(), c2.get())


root = Tk()

# виджеты

# 1) кнопка (Button)
but = Button(root, text='кнопка', width='10', height='2', bg='black',
             fg='blue', font='Verdana 15')
but.bind('<Button-1>', foo)

# 2) метка (Label)
lab = Label(root, text='Моя метка', font='Arial 20', width='15', bg='red')

# 3) однострочное текстовае поле (Entry)
ent = Entry(root, font='Arial 13', width='15', bg='lightblue')

# 4) многострочное текстовое поле (Text)
txt = Text(root, width=40, font='Verdana 12', wrap=WORD, height=5)

# 5) радиокнопки (Radiobutton)
# IntVar - специальная переменна от tkinter. в которой хранятся значения типа int
var = IntVar()
# var = 1 !!!!!!!!!НЕЛЬЗЯ
var.set(1)
# если выберут первую кнопку, то var будет равняться 1
rad1 = Radiobutton(root, text='Первая', variable=var, value=1)
# если выберут первую кнопку, то var будет равняться 2
rad2 = Radiobutton(root, text='Вторая', variable=var, value=2)
# если выберут первую кнопку, то var будет равняться 3
rad3 = Radiobutton(root, text='Третья', variable=var, value=3)
but2 = Button(root, text='check')
but2.bind('<Button-1>', button_click)

# флажки (Checkbutton)
c1 = IntVar()
c2 = IntVar()
# если нажмут на первый флажок, то c1=1, если не нажмут, то c1=0
che1 = Checkbutton(root, text='Первый', variable=c1, onvalue=1, offvalue=0)
che2 = Checkbutton(root, text='Второй', variable=c2, onvalue=1, offvalue=0)
but3 = Button(root, text='check2')
but3.bind('<Button-1>', button_click2)


# списки (Listbox)
r = ['Linux', 'Python', 'Tk', 'Tkinter']
# selectmod=SINGLE - можно выделить только 1 элемент
# height=4 - показывает сколько элеменов отображается на 1 странице списка
lis = Listbox(root, selectmod=SINGLE, height=4)
for elem in r:
    # insert - добавить. (1 аргумент - куда добавить. 2 аргумент - что добавить)
    lis.insert(END, elem)

lab.pack()
but.pack()
ent.pack()
txt.pack()

rad1.pack()
rad2.pack()
rad3.pack()
but2.pack()

che1.pack()
che2.pack()
but3.pack()

lis.pack()

root.mainloop()
