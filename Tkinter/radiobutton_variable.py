# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
v = IntVar()
v.set(1)
dic_text = {1:'python',2:'C++',3:'Java'}
for i in dic_text.values():
	Radiobutton(root,variable=v,text=i,value=i).pack()
root.mainloop()