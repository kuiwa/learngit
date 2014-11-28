# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
mbYes,mbYesNo,mbYesNoCancel,mbYesNoAbort = 0,1,2,4

def MessageBox():
	mbType = mbYesNo
	textShow = 'Yes'
	if mbType == mbYes:
		textShow = 'Yes'
	elif mbType == mbYesNo:
		textShow = 'YesNo'
	elif mbType == mbYesNoCancel:
		textShow = 'YesNoCancel'
	elif mbType == mbYesNoAbort:
		textShow = 'YesNoAbort'
	t1 = Toplevel(height=200,width=400)
	Label(t1,text=textShow).pack()
Button(root,text='Button',command=MessageBox).pack()
root.mainloop()