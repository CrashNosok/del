'''
MENU
'''

from tkinter import *

def open_win():
    new_win = Toplevel(root)

root = Tk()

# создали объект меню
m = Menu(root)
root.config(menu=m)

# создаёт пункт меню с размещением в основном меню
fm = Menu(m)
m.add_cascade(label='File', menu=fm)

# заполнение меню
fm.add_command(label='Open', command=open_win)
fm.add_command(label='New')
fm.add_command(label='Save')
fm.add_command(label='Exit')

# второй пункт меню
hm = Menu(m)
m.add_cascade(label='About', menu=hm)
hm.add_command(label="About us")
hm.add_command(label="Help")

root.mainloop()
