# -*- coding: utf-8 -*-
# file: tkinterSimpleDialog.py
#
from Tkinter import *
from tkSimpleDialog import *
def InStr():
	r = askstring('simpledialog',
					'askstring',
					initialvalue='string')
	print r
def InInt():
	r = askinteger('simpledialog','askinteger')
	print r
def InFlo():
	r = askfloat('simpledialog','askfloat')
	print r
root = Tk()
button1 = Button(root,text = 'Input String', command = InStr)
button1.pack(side='left')
button2 = Button(root,text = 'Input Interger', command = InInt)
button2.pack(side='left')
button3 = Button(root,text = 'Input Float', command = InFlo)
button3.pack(side='left')
root.mainloop()