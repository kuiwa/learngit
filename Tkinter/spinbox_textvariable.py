# -*- coding: utf-8 -*-
from Tkinter import *
root = Tk()
v = StringVar()
sb=Spinbox(root,values=(0,2,30,40,-1),increment=2,textvariable=v)
v.set(20)
print v.get()
sb.pack()
root.mainloop()