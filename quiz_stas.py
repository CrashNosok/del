from tkinter import *
from tkinter import messagebox


def check_results(event):
    result = 0
    # если пользователь нажал на 1 кнопку (1-ый ответ верный)
    if var1.get() == 1:
        result += 1

    # если поьзователь выбрал 2 и 3 флажок (2 и 3 ответы верные)
    if c2.get() == 1 and c3.get() == 1 and c1.get() == 0:
        result += 2
    # если поьзователь выбрал 2 флажок (2 и 3 ответы верные)
    elif c2.get() == 1 and c1.get() == 0 and c3.get() == 0:
        result += 1
    # если поьзователь выбрал 3 флажок (2 и 3 ответы верные)
    elif c3.get() == 1 and c2.get() == 0 and c1.get() == 0:
        result += 1

    # если пользователь ввёл "ежик" (ежик - правильный ответ)
    if ent.get() == 'ежик':
        result += 2

    # если пользователб на шкале выбрал 50 (50 - правильный ответ)
    if sca1.get() == 50:
        result += 2
    messagebox.showinfo('Результат', f'Вы набрали {result} баллов из 7')


root = Tk()
root.title("Викторина")
# root["bg"] = "gray"
root.geometry("450x600")

question1 = Label(root, text='Придумай вопрос 1', font='Verdana 15', fg='darkblue', height='2', width='20')
var1 = IntVar()
rad1 = Radiobutton(root, text='первая', variable=var1, value=1, font='Verdana 15')
rad2 = Radiobutton(root, text='вторая', variable=var1, value=2, font='Verdana 15')
rad3 = Radiobutton(root, text='третья', variable=var1, value=3, font='Verdana 15')

question2 = Label(root, text='Придумай вопрос 2', font='Verdana 15', fg='darkblue', height='2', width='20')
c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
check1 = Checkbutton(root, text='первый', variable=c1, onvalue=1, offvalue=0, font='Verdana 15')
check2 = Checkbutton(root, text='второй', variable=c2, onvalue=1, offvalue=0, font='Verdana 15')
check3 = Checkbutton(root, text='третий', variable=c3, onvalue=1, offvalue=0, font='Verdana 15')

question3 = Label(root, text='Придумай вопрос 3', font='Verdana 15', fg='darkblue', height='2', width='20')
ent = Entry(root, font='Verdana 15')

question4 = Label(root, text='Придумай вопрос 4', font='Verdana 15', fg='darkblue', height='2', width='20')
sca1 = Scale(root, orient=HORIZONTAL, length=300,
             from_=0, to=100, tickinterval=10, resolution=5)

but = Button(text='Получить результаты', bg='gold', width='30', height='2')
but.bind('<Button-1>', check_results)

question1.pack()
rad1.pack()
rad2.pack()
rad3.pack()
question2.pack()
check1.pack()
check2.pack()
check3.pack()

question3.pack()
ent.pack()

question4.pack()
sca1.pack()

but.pack()

root.mainloop()
