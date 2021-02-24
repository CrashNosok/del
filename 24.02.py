from tkinter import *

root = Tk()

def my_sqrt():
    # n = int(ent.get())
    n = int(input()) # 49
    i = 0
    while i*i <= n:
        if i*i == n:
            return i
        i += 1
    return -1

def fact():
    # n = int(ent.get())
    n = int(input()) # 5! = 1*2*3*4*5 = 120
    i = 1
    res = 1
    while i <= n:
        res *= i
        i += 1
    return res

def plus_ent(e):
    n = int(ent.get())
    n += 1
    ent.delete(0, END)
    ent.insert(0, n)

def my_pow(e):
    # 2^5
    v = ent.get()
    if v.count('^') == 1:
        tmp = v.split('^')
        o = int(tmp[0])
        s = int(tmp[1])
        ent.delete(0, END)
        ent.insert(0, o**s)


ent = Entry(root)
ent.pack()

but = Button(root, text='click')
but.bind('<Button-1>', my_pow)
but.pack()

root.mainloop()
