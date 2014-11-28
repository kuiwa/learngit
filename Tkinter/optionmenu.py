# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
v = StringVar()
v.set('Language')
def printV(text):
	print text
	print v.get()
om = OptionMenu(root,v,'python','php','C','CPP',command=printV)
om.pack()
print v.get()
root.mainloop()