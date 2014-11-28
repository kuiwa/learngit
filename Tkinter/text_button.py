# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
t = Text(root)
for i in range(10):
	t.insert(1.0,'0123456789\n')
def printText():
	print 'button in text'
bt = Button(t,text='button',command=printText)
t.window_create('2.0',window=bt)
t.pack()
root.mainloop()