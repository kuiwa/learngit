# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
cv = Canvas(root,bg='white')
rt3=cv.create_rectangle(10,10,100,200,tags=('r1','r2','r3'))
rt2=cv.create_rectangle(20,20,100,200,tags=('s1','s2','s3'))
rt1=cv.create_rectangle(30,30,100,200,tags=('y1','y2','y3'))
cv.addtag_above('r4',rt2)
cv.addtag_below('r5',rt2)
cv.itemconfig(cv.find_above(rt2),outline='red')
for item in [rt1,rt2,rt3]:
	print cv.gettags(item)

cv.pack()
root.mainloop()