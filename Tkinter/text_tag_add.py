# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
t = Text(root)
t.tag_config('b',foreground='blue')
for i in range(10):
	t.insert(1.0,'0123456789\n')
t.tag_add('b','2.5','2.end')
t.pack()
root.mainloop()