# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
cv = Canvas(root,bg='white')
d = {1:'error',2:'info',3:'question',4:'hourglass'}
for i in d:
	cv.create_bitmap((20*i,20*i),bitmap=d[i])
	cv.pack()
root.mainloop()