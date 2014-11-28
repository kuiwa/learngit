# -*- coding: utf-8 -*-
from Tkinter import *
root = Tk()
s1 = Scale(root,orient=HORIZONTAL,label='choice:')
s1.set(50)
print s1.get()
s1.pack()
root.mainloop()