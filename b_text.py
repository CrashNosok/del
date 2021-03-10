from tkinter import *

def erase():
    tx.delete(1.0, END)

root = Tk()

t = '''The Zen of Python, by Tim Peters   

Beautiful is better than ugly.     
Explicit is better than implicit.  
Simple is better than complex.     
Complex is better than complicated.
Flat is better than nested.        
Sparse is better than dense.       
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

tx = Text(root, width=50, height=15, font='times 20', wrap=WORD)
tx.insert(1.0, t)

# fill - растяжение (влево, вправо)
# expand - растяжение (вверх, вниз)
tx.pack(fill=BOTH, expand=YES)

# создаем теги
# синтаксис:
# tx.tag_add(название_тега, откуда_начинается, где_заканчивается)
# откуда_начинается и где_заканчивается указываются в формате:
# 'строка.символ' - строки начинаются с 1, символы начинаются с 0
tx.tag_add('title', '1.0', '1.end')

# настройка тега
# синтаксис:
# tx.tag_config(название, свойства)
# font='название_шрифта размер_шрифта особенность'

# bold      - жирный шрифт
# italic    - курсив
# underline - подчеркнутый
tx.tag_config('title', font='Arial 40 italic', foreground='red', 
                justify=CENTER, background='white')
# justify - выравнивание (LEFT, CENTER, RIGHT)


# в текст можно вставлять виджеты
bt = Button(tx, text='click', command=erase)
# разместить виджет в Text
# чтобы разместить виджет в Text, вместо pack используем 
# text.window_create(индекс, windor=виджет_который_вставляем)
tx.window_create(END, window=bt)

root.mainloop()
