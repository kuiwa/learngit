# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
cv = Canvas(root,bg='white')
rt = cv.create_rectangle(10,50,100,200,tags=('r1','r2','r3','r4'))
cv.pack()
cv.create_rectangle(20,100,200,200,tags='r3')
for item in cv.find_withtag('r3'):
	cv.itemconfig(item,outline='blue')
root.mainloop()