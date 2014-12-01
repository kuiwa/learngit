# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
cv = Canvas(root,bg='white')
def printWindow():
	print 'window'
bt = Button(cv,text='button',command=printWindow)
cv.create_window((10,10),window=bt,anchor=W)
cv.create_line(10,10,20,20)
cv.create_line(30,30,100,100)
cv.pack()
root.mainloop()