# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
def printSpin():
	print sb.get()
sb=Spinbox(root,from_=0,to=10,command=printSpin)
sb.pack()
root.mainloop()