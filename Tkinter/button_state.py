# -*- coding: utf-8 -*-

from Tkinter import *

root = Tk()
def statePrint():
	print 'state'
for r in ['normal','active','disabled']:
	Button(root,text=r,state=r,width=20,command=statePrint).pack()
b = Button(root,text='button',state='active',width=20,command=statePrint)
b.pack()
root.mainloop()