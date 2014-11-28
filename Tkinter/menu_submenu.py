# -*- coding: utf-8 -*-
from Tkinter import *
root = Tk()
menubar = Menu(root)
submenubar = Menu(menubar,tearoff=0)
def printMenu():
	print 'Hello'
menubar.add_cascade(label='File',menu=submenubar)
l_file = ['open','new','save','save as']
for item in l_file:
	submenubar.add_command(label=item,command=printMenu)
root['menu']=menubar
root.mainloop()