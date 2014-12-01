# -*- coding: utf-8 -*-

from Tkinter import *
from tkSimpleDialog import *
root = Tk()
print askinteger(title='prompt',prompt='input ainteger:',initialvalue=100)
print askfloat(title='float',prompt='input a float',minvalue=0,maxvalue=11)
print askstring(title='string',prompt='input a string')
root.mainloop()