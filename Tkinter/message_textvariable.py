# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
v = StringVar()
v.set('000')
for i in range(10):
	Message(root,text='textvariable',textvariable=v).pack()
print v.get()
root.mainloop()