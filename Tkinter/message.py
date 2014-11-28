# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
Message(root,text='hello Message').pack()
Message(root,text='hello width',width=60).pack()
Message(root,text='aspect'*2,aspect=400).pack()
root.mainloop()