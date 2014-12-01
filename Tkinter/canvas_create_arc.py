# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
cv = Canvas(root,bg='white')
d = {1:PIESLICE,2:CHORD,3:ARC}
for i in d:
	cv.create_arc((10,10+60*i,110,110+60*i),style=d[i],start=30,extent=30)
	print i, d[i],
cv.pack()
root.mainloop()