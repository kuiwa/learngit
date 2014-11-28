# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
cv = Canvas(root,bg='white')
rt = cv.create_rectangle(10,50,100,200,tags='r1')
cv.pack()
print cv.gettags(rt)
cv.itemconfig(rt,tags=('r2','r3','r4'))
print cv.gettags(rt)
root.mainloop()