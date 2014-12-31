# -*- coding: utf-8 -*-
# file: Hellotkinter.py
#
from Tkinter import *
root = Tk()
label = Label(root,text='tkinter label')
label.pack()
button1 = Button(root,text='tkinter button1')
button1.pack(side = RIGHT)
button2 = Button(root,text='tkinter button2')
button2.pack(side = LEFT)
root.mainloop()