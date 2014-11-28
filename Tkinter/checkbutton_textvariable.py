# -*- coding: utf-8 -*-

from Tkinter import *

def callCheckbutton():
	if v.get() == "check python":
		v.set('check Tkinter')
	else:
		v.set('check python')
root = Tk()
v = StringVar()
v.set('check python')
Checkbutton(root,text='check python',textvariable=v,command=callCheckbutton).pack()
root.mainloop()