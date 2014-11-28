# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
t = Text(root)
for i in range(10):
	t.insert(1.0,'0123456789\n')
print t.get('1.0','2.3')
t.mark_set('start','3.1')
t.mark_set('end',END)
t.tag_add('b','start','end')
t.insert('b.first','first')
t.insert('b.last','last')
print t.get('start','end')
t.pack()
root.mainloop()