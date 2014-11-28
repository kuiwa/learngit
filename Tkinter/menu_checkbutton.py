# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
def printItem():
	print 'python= ', vPython.get()
menubar = Menu(root)
vPython = StringVar()
dictV = {'Python': vPython}
submenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Language',menu=submenu)
for k,v in dictV.items():
	submenu.add_checkbutton(label=k,command=printItem,variable=v)
root['menu'] = menubar
root.mainloop()