# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
t = Text(root)
t.tag_config('b',background='blue')
for i in range(10):
	t.insert(1.0,'01233445\n')
t.mark_set('start','3.1')
t.mark_set('end',END)
t.tag_add('b','start','end')
t.insert('b.first','1st')
t.insert('b.last','end')
t.pack()
root.mainloop()