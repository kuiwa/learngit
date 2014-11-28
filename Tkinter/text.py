# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
t = Text(root)
t.insert(1.0,'0123456789\n')
t.insert(1.0,'abcdefg\n')
t.insert('2.end','end')
t.insert(2.11,'zxy')
t.pack()
root.mainloop()