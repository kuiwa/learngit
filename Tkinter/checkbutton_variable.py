# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
v = IntVar()
def callCheckbutton():
	print v.get()
cb=Checkbutton(root,variable=v,text='checkbuttonvalue',command=callCheckbutton,bitmap='error',compound='left',wraplength=10)
cb.pack()

root.mainloop()