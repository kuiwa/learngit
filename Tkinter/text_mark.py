# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
t = Text(root)
for i in range(1,10):
	t.insert(1.0,'0123456789\n')
def insertText():
	t.insert(INSERT,'jcodeer')
def currentText():
	t.insert(CURRENT,'jcodeer')
def endText():
	t.insert(END,'jcodeer')
def selFirstText():
	t.insert(SEL_FIRST,'jcodeer')
def selLastText():
	t.insert(SEL_LAST,'jcodeer')
	
Button(root,text='insert jcodeer at INSET',command=insertText).pack(fill=X)
Button(root,text='insert jcodeer at CURRENT',command=currentText).pack(fill=X)
Button(root,text='insert jcodeer at END',command=endText).pack(fill=X)
Button(root,text='insert jcodeer at SEL_FIRST',command=selFirstText).pack(fill=X)
Button(root,text='insert jcodeer at SEL_LAST',command=selLastText).pack(fill=X)
t.pack()
root.mainloop()