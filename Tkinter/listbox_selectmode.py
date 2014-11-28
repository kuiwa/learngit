# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
lb = Listbox(root,selectmode=BROWSE)
lb1 = Listbox(root,selectmode=MULTIPLE)
lb2 = Listbox(root,selectmode=EXTENDED)
for item in ['python','tkinter','widget']:
	lb.insert(END,item)
	lb2.insert(END,item)
lb.pack()
lb2.pack()
root.mainloop()