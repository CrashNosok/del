from tkinter import *

def foo():
    print('вы нажали на пункт меню')

def foo2():
    root.destroy()

root = Tk()

# создаем основное меню
m = Menu(root)
# привязать m к root
root.config(menu=m)

fm = Menu(m, tearoff=0)
# tearoff=0 - уберет черточки
# добавляем строчки в меню
fm.add_command(label='New File')
fm.add_command(label='New Window')
fm.add_command(label='Open')
# добавить меню в другое меню
m.add_cascade(label='File', menu=fm)

fm2 = Menu(fm, tearoff=0)
# привязка функций к меню
fm2.add_command(label='lalala', command=foo)
fm2.add_command(label='lalala2', command=foo2)
fm.add_cascade(label='my lalala', menu=fm2)

root.mainloop()
