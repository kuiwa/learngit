# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
def hello():
	print 'hello menu'
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Language',menu=filemenu)
lang=['python','php','cpp','Java']
for item in lang:
	filemenu.add_command(label=item,command=hello)
root['menu']=menubar
root.mainloop()