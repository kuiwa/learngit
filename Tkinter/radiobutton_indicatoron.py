# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
v = IntVar()
v.set(1)
for i in range(3):
	Radiobutton(root,variable=v,indicatoron=100,text='python&tkinter',value=i).pack()
root.mainloop()