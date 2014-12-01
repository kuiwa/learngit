# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
cv = Canvas(root,bg='white')
rt1=cv.create_rectangle(10,10,100,100,tags=('r1','r2','r3'))
cv.create_rectangle(10,10,100,100,tags=('r1','r2','r3'))
#cv.move(rt1,200,100)
cv.scale(rt1,0,0,1,2)
cv.pack()
root.mainloop()