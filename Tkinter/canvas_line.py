# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
cv = Canvas(root,bg='white')
d = [(0,'none','bevel'),(1,'first','miter'),(2,'last','round'),(3,'both','round')]
for i in d:
	cv.create_line((10,10+i[0]*20,110,110+i[0]*20),
	arrow = i[1],
	arrowshape = '8 10 3',
	joinstyle = i[2],)
cv.pack()
root.mainloop()
	
	