# -*- coding: utf-8 -*-

from Tkinter import *

root = Tk()
e = StringVar()
entry = Entry(root,textvariable=e)
e.set('readonly')
entry.pack()
entry['state'] = 'readonly'
root.mainloop()