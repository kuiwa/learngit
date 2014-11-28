# -*- coding: utf-8 -*-

from Tkinter import *

root = Tk()
Entry(root,text='input your text here').pack()
e = StringVar()
entry = Entry(root,textvariable=e)
e.set('input your text hrere')
entry.pack()
root.mainloop()