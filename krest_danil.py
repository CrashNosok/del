from tkinter import *
from tkinter.messagebox import showinfo


words_dict = {
    'cat': 'кот',
    'dog': 'собака',
    'fence': 'забор',
}

words_list = list(words_dict.keys())
index_word = 0
n = 0
name = ''


def clear():
    # Удаление предыдущего окна, чтобы окна не наслаивались одно на другое
    if frm.winfo_children():
        for elem in frm.winfo_children():
            if str(elem) != '.!frame.!entry':
                elem.destroy()


def get_result(event):
    showinfo('Результат', f'{name} вы набрали {n} баллов')


def gotomenu1(event):
    global name
    clear()
    name = ent.get()
    ent.delete(0, END)
    lab = Label(frm, text='1. Не копаться в коде', font='30', fg='blue', bg='pink')
    lab.place(relx=0.5, rely=0.1, anchor="center")

    btn = Button(frm, text="Начать тест", width=30)
    btn.bind('<Button-1>', gotomenu2)
    btn.bind('<Return>', gotomenu2)
    btn.place(relx=0.5, rely=0.5, anchor="center")


def gotomenu2(event):
    global index_word
    global n
    clear()

    btn = Button(frm, width=30)
    if ent.get() == words_dict[words_list[index_word - 1]]:
        n += 1
    ent.delete(0, END)
    if index_word < len(words_list):
        lab = Label(frm, text=words_list[index_word], font='30', fg='blue', bg='pink')
        index_word += 1
        # проверка слова
        btn['text'] = 'Далее'
        btn.bind('<Button-1>', gotomenu2)
        lab.place(relx=0.5, rely=0.1, anchor="center")
    else:
        btn['text'] = 'Получить результат'
        btn.bind('<Button-1>', get_result)
        btn.bind('<Return>', get_result)
    btn.place(relx=0.5, rely=0.5, anchor="center")


root = Tk()
root.geometry("400x400")

frm = Frame(root, width=400, height=400, bg="red")
frm.pack()

btn = Button(frm, text='Перейдите к правилам')
btn.bind('<Button-1>', gotomenu1)
btn.place(relx=0.5, rely=0.5, anchor="center")
lab = Label(frm, text='здравствуйте это мой тест', font='30', fg='blue', bg='pink')
lab.place(relx=0.5, rely=0.1, anchor="center")
ent = Entry(frm, font='30', fg='blue', bg='pink')
ent.place(relx=0.5, rely=0.3, anchor="center")

root.focus_force()
root.mainloop()

































