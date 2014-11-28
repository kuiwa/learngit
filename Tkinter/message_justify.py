# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
for i in [LEFT,RIGHT,CENTER]:
	Message(root,text='LEFT RIGHT CENTER',justify=i).pack()
root.mainloop()