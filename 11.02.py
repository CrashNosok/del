from tkinter import *

root = Tk()
root.title('my window')

# fra = Frame(root, width=100, height=200, bg='red', bd=20)
# fra.pack()

# but1 = Button(root, text='clic1', width=20, height=3)
# but2 = Button(root, text='clic2', width=20, height=3)
# but3 = Button(root, text='clic3', width=20, height=3)
# but4 = Button(root, text='clic4', width=42, height=3)

# row - строка
# column - столбец
# columnspan - сколько столбцов займет
# but1.grid(row=0, column=0)
# but2.grid(row=0, column=1)
# but3.grid(row=1, column=1)
# but4.grid(row=2, column=0, columnspan=2)

def foo(event):
    print(event)
    root.destroy()

but = Button(root, text='нажми меня!!', width=30, height=3, 
            bg='lightblue', font='Arial 30')

'''
типы событий:
события мыши:
<Button-1> - ЛКМ
<Button-2> - СКМ
<Button-3> - ПКМ
<Double-Button-1> - двойное нажатие ЛКМ
<Triple-Button-1> - тройное нажатие ЛКМ
<Motion> - движение мыши

события клавиатуры:
a - буква а
1 - цифра 1
A - большая буква А
<Return> - ентер
<space> - пробел
<Shift_L> - левый шифит
<Shift_R> - правый шифит
<Control_L> - левый контрол
<Alt_L> - левый альт

Pause, Caps_Lock, Escape, Prior (Page Up), Next (Page Down),
End, Home, Left, Up, Right, Down, Print, Insert, Delete, F1,
F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, Num_Lock, and
Scroll_Lock...

комбинации (пишем без _L, _R):
<Control-a>
<Shift-p>
'''

root.bind('a', foo)
but.pack()

root.mainloop()
