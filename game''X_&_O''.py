from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title('X & O')

moove = 'X'

def CheckForWinner():
    if but1['text'] == 'X' and but2['text'] == 'X' and but3['text'] == 'X': #flat X
        showinfo('X & O', 'XXX "X wins" XXX')
    if but4['text'] == 'X' and but5['text'] == 'X' and but6['text'] == 'X': #flat X
        showinfo('X & O', 'XXX "X wins" XXX')
    if but7['text'] == 'X' and but8['text'] == 'X' and but9['text'] == 'X': #flat X
        showinfo('X & O', 'XXX "X wins" XXX')
    if but1['text'] == 'X' and but4['text'] == 'X' and but7['text'] == 'X': #vertical X
        showinfo('X & O', 'XXX "X wins" XXX')
    if but2['text'] == 'X' and but5['text'] == 'X' and but8['text'] == 'X': #vertical X
        showinfo('X & O', 'XXX "X wins" XXX')
    if but3['text'] == 'X' and but6['text'] == 'X' and but9['text'] == 'X': #vertical X
        showinfo('X & O', 'XXX "X wins" XXX')
    if but1['text'] == 'X' and but5['text'] == 'X' and but9['text'] == 'X': #diagonal X
        showinfo('X & O', 'XXX "X wins" XXX')
    if but3['text'] == 'X' and but5['text'] == 'X' and but7['text'] == 'X': #diagonal X
        showinfo('X & O', 'XXX "X wins" XXX')
    if but1['text'] == 'O' and but2['text'] == 'O' and but3['text'] == 'O': #flat O
        showinfo('X & O', 'OOO "O wins" OOO')
    if but4['text'] == 'O' and but5['text'] == 'O' and but6['text'] == 'O': #flat O
        showinfo('X & O', 'OOO "O wins" OOO')
    if but7['text'] == 'O' and but8['text'] == 'O' and but9['text'] == 'O': #flat O
        showinfo('X & O', 'OOO "O wins" OOO')
    if but1['text'] == 'O' and but4['text'] == 'O' and but7['text'] == 'O': #vertical O
        showinfo('X & O', 'OOO "O wins" OOO')
    if but2['text'] == 'O' and but5['text'] == 'O' and but8['text'] == 'O': #vertical O
        showinfo('X & O', 'OOO "O wins" OOO')
    if but3['text'] == 'O' and but6['text'] == 'O' and but9['text'] == 'O': #vertical O
        showinfo('X & O', 'OOO "O wins" OOO')
    if but1['text'] == 'O' and but5['text'] == 'O' and but9['text'] == 'O': #diagonal O
        showinfo('X & O', 'OOO "O wins" XXX')
    if but3['text'] == 'O' and but5['text'] == 'O' and but7['text'] == 'O': #diagonal O
        showinfo('X & O', 'OOO "O wins" OOO')

def btn(event):
    global moove
    but = event.widget
    if moove == 'O':
        if not(but['text'] == 'X' or but['text'] == 'O'):
            but['text'] = 'O'
            moove = 'X'
    if moove == 'X':
        if not(but['text'] == 'X' or but['text'] == 'O'):
            but['text'] = 'X'
            moove = 'O'
    CheckForWinner()

but1 = Button(root, text=' ', width=8, height=4)
but2 = Button(root, text=' ', width=8, height=4)
but3 = Button(root, text=' ', width=8, height=4)
but4 = Button(root, text=' ', width=8, height=4)
but5 = Button(root, text=' ', width=8, height=4)
but6 = Button(root, text=' ', width=8, height=4)
but7 = Button(root, text=' ', width=8, height=4)
but8 = Button(root, text=' ', width=8, height=4)
but9 = Button(root, text=' ', width=8, height=4)

but1.bind('<Button-1>', btn)
but2.bind('<Button-1>', btn)
but3.bind('<Button-1>', btn)
but4.bind('<Button-1>', btn)
but5.bind('<Button-1>', btn)
but6.bind('<Button-1>', btn)
but7.bind('<Button-1>', btn)
but8.bind('<Button-1>', btn)
but9.bind('<Button-1>', btn)

but1.grid(column=0, row=0)
but2.grid(column=1, row=0)
but3.grid(column=2, row=0)
but4.grid(column=0, row=1)
but5.grid(column=1, row=1)
but6.grid(column=2, row=1)
but7.grid(column=0, row=2)
but8.grid(column=1, row=2)
but9.grid(column=2, row=2)

root.mainloop()
