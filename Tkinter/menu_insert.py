# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Language',menu=filemenu)

def printItem():
	print 'add_separator'
	
for k in range(5):
	filemenu.add_command(label=str(k),)
filemenu.insert_command(1,label='1000',)
filemenu.insert_checkbutton(2,label='2000')
filemenu.insert_checkbutton(4,label='4000')
filemenu.insert_radiobutton(3,label='3000')
filemenu.insert_separator(1)
filemenu.insert_separator(5)
root['menu'] = menubar
root.mainloop()