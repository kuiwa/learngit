# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
cv = Canvas(root,bg='white')
cv.create_rectangle(100,100,200,200,fill='red',outline='green',dash=255,width=10)
cv.pack()
root.mainloop()