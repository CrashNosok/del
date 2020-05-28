from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import showinfo, askyesno


def write(event):
    text = var.get() + '\n'
    i = 0
    while i < len(lessons_lst):
        if lessons_lst[i].get() != '':
            text += str(i) + '\t' + lessons_lst[i].get() + '\n'
        i += 1
    sa = asksaveasfilename()
    if askyesno('???', 'удалить всё из файла перед записью?'):
        f = open(sa, 'w')
    else:
        f = open(sa, 'a')
    f.write(text)
    f.close()


root = Tk()

lab = Label(text='Здравствуйте\nВыберите день, который хотите заполнить')

var = StringVar()
var.set('Понедельник')
rad1 = Radiobutton(root, text='Понедельник', variable=var, value='Понедельник')
rad2 = Radiobutton(root, text='Вторник', variable=var, value='Вторник')
rad3 = Radiobutton(root, text='Среда', variable=var, value='Среда')
rad4 = Radiobutton(root, text='Четверг', variable=var, value='Четверг')
rad5 = Radiobutton(root, text='Пятница', variable=var, value='Пятница')
rad6 = Radiobutton(root, text='Суббота', variable=var, value='Суббота')

lab2 = Label(text='Заполните расписание')
lesson1 = Entry(root)
lesson2 = Entry(root)
lesson3 = Entry(root)
lesson4 = Entry(root)
lesson5 = Entry(root)
lesson6 = Entry(root)
lesson7 = Entry(root)
lesson8 = Entry(root)

lessons_lst = [lesson1, lesson2, lesson3, lesson4, lesson5, lesson6, lesson7, lesson8]

but = Button(root, text='Записать расписание')
but.bind('<Button-1>', write)


lab.pack()

rad1.pack()
rad2.pack()
rad3.pack()
rad4.pack()
rad5.pack()
rad6.pack()

lab2.pack()
lesson1.pack()
lesson2.pack()
lesson3.pack()
lesson4.pack()
lesson5.pack()
lesson6.pack()
lesson7.pack()
lesson8.pack()

but.pack()

root.mainloop()
