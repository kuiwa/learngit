# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
t = Text(root)
for i in range(10):
	t.insert(1.0,'0123456789\n')
t.tag_config('a',background='blue',underline=1)
def enterTag(event):
	print 'Enter event'
t.tag_bind('a','<Enter>',enterTag)
t.insert(2.0,'Enter event\n','a')
t.pack()
root.mainloop()