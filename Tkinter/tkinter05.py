# -*- coding: utf-8 -*-

from Tkinter import *

top = Tk()
top.title("Tkinter.title")
bm = PhotoImage(file = 'f:\\download\\39.bmp')
label = Label(top,bitmap=bm)
label.pack
top.mainloop()