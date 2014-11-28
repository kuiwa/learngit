# -*- coding: utf-8 -*-

from Tkinter import *

root = Tk()
def changeText():
	if v.get() == 'text':
		v.set('change')
		print 'change'
	else:
		v.set('text')
		print 'text'
v = StringVar()
b = Button(root,textvariable=v,width=20,command=changeText)
v.set('text')
b.pack()
root.mainloop()