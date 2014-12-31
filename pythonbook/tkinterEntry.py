# -*- coding: utf-8 -*-
# file: tkinterEntry.py
#
from Tkinter import *
root = Tk()
entry1 = Entry(root, show = '*')
entry1.pack()
entry2 = Entry(root, show = '#', width = 50)
entry2.pack()
entry3 = Entry(root, bg = 'red', fg = 'blue')
entry3.pack()
entry4 = Entry(root, selectbackground = 'red', selectforeground = 'gray')
entry4.pack()
entry5 = Entry(root, state = DISABLED)
entry5.pack()
edit1 = Text(root, selectbackground = 'red', selectforeground = 'gray')
edit1.pack()
root.mainloop()