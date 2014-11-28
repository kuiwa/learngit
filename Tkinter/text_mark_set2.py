# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
t = Text(root)
t.tag_config('b',foreground='blue')
for i in range(10):
	t.insert(1.0,'0123456789\n')
t.mark_set('start','3.1')
t.mark_set('end',END)
t.tag_add('b','start','end')
t.pack()
root.mainloop()