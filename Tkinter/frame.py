# -*- coding: utf -*-

from Tkinter import *
root = Tk()
for fm in ['red','blue','yellow']:
	Frame(height=20,width=400,bg=fm).pack()
root.mainloop()