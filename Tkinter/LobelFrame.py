# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
for lf in ['red','blue','yellow']:
	LabelFrame(height=200,width=300,text=lf).pack()
root.mainloop()