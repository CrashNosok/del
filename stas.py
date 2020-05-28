import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter import messagebox


# def save(event):
#     with open('my_file.txt', 'w') as file:
#         file.write(str(var.get()))
#
#
# def foo(event):
#     top = Toplevel()
#     # var.set(1)
#     rad1 = Radiobutton(top, text='Pn', variable=var, value=1)
#     rad1.pack()
#     rad2 = Radiobutton(top, text='Vt', variable=var, value=2)
#     rad2.pack()
#     rad3 = Radiobutton(top, text='Sr', variable=var, value=3)
#     rad3.pack()
#     rad4 = Radiobutton(top, text='Cht', variable=var, value=4)
#     rad4.pack()
#     rad5 = Radiobutton(top, text='Pt', variable=var, value=5)
#     rad5.pack()
#     but2 = Button(top, text='Save')
#     but2.bind('<Button-1>', save)
#     but2.pack()


root = tkinter.Tk()
root.title("Notepad")
# root.minsize(width=500, height=500)
# root.maxsize(width=500, height=500)

text = Text(root, width=500, height=500, wrap="word")
but = Button(root, text='Save')
# but.bind('<Button-1>', foo)

text.pack()
but.pack()
root.mainloop()
