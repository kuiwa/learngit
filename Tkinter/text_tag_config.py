# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
t = Text(root)
t.tag_config('a',foreground='red',background='black')
t.tag_config('b',foreground='green')
t.tag_lower('b')
t.insert(1.0,'1234567890',('b','a'))
t.pack()
root.mainloop()