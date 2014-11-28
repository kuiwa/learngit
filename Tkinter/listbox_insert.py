# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
lb = Listbox(root)
for item in['python','tkinter','widget']:
	lb.insert(END,item)
lb.insert(0,'linux','windows','unix')
lb.insert(1,'OS')
lb.delete(1,3)
lb.selection_set(0,2)
lb.selection_clear(1)
print lb.size()
print lb.get(1,3)
print lb.curselection()
print lb.selection_includes(0)
lb.pack()
root.mainloop()
