# -*- coding: utf-8 -*-
# file: tkinterColorChooser.py
#
from Tkinter import *
from tkColorChooser import *
def ChooseColor():
	r = askcolor(title = 'askcolor')
	print r
root = Tk()
button = Button(root,text='Choose Color', command = ChooseColor)
button.pack()
root.mainloop()