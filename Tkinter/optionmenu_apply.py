# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
Lang = ['python','php','cpp','Perl']
v = StringVar()
v.set('Tkinter')
def printOption(event):
	print v.get()
om = apply(OptionMenu,(root,v)+tuple(Lang))
om.bind('<Button-1>',printOption)
om.pack()
root.mainloop()