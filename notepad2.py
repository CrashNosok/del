from tkinter import *

t = '''Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!'''

root = Tk()

'''
виджет Text
'''

tx = Text(root, font='times 25', width=60, height=12)
# expand=YES - текст всегда по центру
# fill=BOTH - текст заполняет всё окно
tx.pack(expand=YES, fill=BOTH)

tx.insert('1.0', t)

# добавим тег в текст
# tx.tag_add(название_тега, откуда_начинается, где_заканчивается)
# название_тега - сами придумываете
# откуда_начинается и где_заканчивается указывать в формате:
# 'строка.символ' (например, 4 строка, 5 символ: '4.5')
tx.tag_add('title', '1.0', '1.end') # end - до конца
tx.tag_add('title', '2.5', '2.10')
tx.tag_add('fg', '3.2', '4.end')


# настройка тега:
# tx.tag_config(название_тега, свойства)
# формат font 'название_шрифта, размер, особенность'
# bold - жирный шрифт
# italic - курсив
# underline - подчеркивание
tx.tag_config('title', font='Arial 30 underline',
                foreground='red', justify=CENTER)
tx.tag_config('fg', background='grey')
# justify - где текст находится (может быть LEFT, CENTER, RIGHT)


root.mainloop()
