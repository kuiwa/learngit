# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
print root.pack_slaves()
Label(root,text='pack').pack()
print root.pack_slaves()
root.mainloop()