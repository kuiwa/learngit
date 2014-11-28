# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
def printSpin():	
	sb.insert(END,'.00')
sb=Spinbox(root,from_=1,to=100,command=printSpin)
sb.pack()
root.mainloop()