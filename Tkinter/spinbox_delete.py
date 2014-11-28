# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
def printSpin():
	sb.delete(0)
	print sb.get()
sb=Spinbox(root,value=(1,12,123,1234,12345,123456,1234567),command=printSpin)
sb.pack()
root.mainloop()