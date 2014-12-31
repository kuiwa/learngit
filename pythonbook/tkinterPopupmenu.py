# -*- coding: utf-8 -*-
# file: tkinterPopupmenu.py
#
from Tkinter import *
root = Tk()
menu = Menu(root, tearoff=0)
menu.add_command(label='Copy')
menu.add_command(label='Paste')
menu.add_separator()
menu.add_command(label='Cut')
def popupmenu(event):
	menu.post(event.x_root,event.y_root)
root.bind("<Button-3>", popupmenu)
root.mainloop()