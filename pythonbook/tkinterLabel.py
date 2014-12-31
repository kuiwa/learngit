# -*- coding: utf-8 -*-
# file: tkinterLabel.py
#
from Tkinter import *
root = Tk()
label1 = Label(	root,
				anchor = E,
				bg = 'blue',
				fg = 'red',
				text = 'Python',
				width = 30,
				height = 5)
label1.pack()
label2 = Label(	root,
				text = 'Python GUI\ntkinter',
				justify = LEFT,
				width = 30,
				height = 5)
label2.pack()
label3 = Label(	root,
				text = 'Python GUI\ntkinter',
				justify = RIGHT,
				width = 30,
				height = 5)
label3.pack()
label4 = Label(	root,
				text = 'Python GUI\ntkinter',
				justify = CENTER,
				width = 30,
				height = 5)
label4.pack()
root.mainloop()