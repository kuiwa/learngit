# -*- coding: utf-8 -*-

from Tkinter import *
def callCheckbutton():
	print "You check this button"
root = Tk()
Checkbutton(root, text='check python',command=callCheckbutton).pack()
root.mainloop()
