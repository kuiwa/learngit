# -*- coding: utf-8 -*-
from Tkinter import *
root = Tk()
Spinbox(root,from_=0,to=100,increment=5,value=(0,2,30,40)).pack()
root.mainloop()