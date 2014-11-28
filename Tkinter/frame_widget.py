# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
fm = []
for color in ['red','blue','green']:
	fm.append(Frame(height=200,width=400,bg=color))
Label(fm[1],text='hello label').pack()
fm[0].pack()
fm[1].pack()
fm[2].pack()
root.mainloop()