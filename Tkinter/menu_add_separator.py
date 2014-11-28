# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Language',menu=filemenu)

def printItem():
	print 'add_separator'
for k in ['python','java','C++','PHP']:
	filemenu.add_command(label=k,command=printItem)
	filemenu.add_separator()
root['menu']=menubar
root.mainloop()