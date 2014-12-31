# -*- coding: utf-8 -*-
# file: tkinterMessageBox.py
#
from Tkinter import *
import tkMessageBox
def cmd():
	global n
	global buttontext
	n = n + 1
	if n == 1:
		tkMessageBox.askokcancel('Python tkinter','askokcancel')
		buttontext.set('skquestion')
	elif n == 2:
		tkMessageBox.askquestion('Python tkinter','askquestion')
		buttontext.set('askyesno')
	elif n == 3:
		tkMessageBox.askyesno('Python tkinter','askyesno')
		buttontext.set('showerror')
	elif n == 4:
		tkMessageBox.showerror('Python tkinter','showerror')
		buttontext.set('showwarning')
	else:
		tkMessageBox.showinfo('Python tkinter','showinfo')
		buttontext.set('askokcancel')
n = 0	
root = Tk()
buttontext = StringVar()
buttontext.set('askokcancel')
button = Button(root,
				textvariable = buttontext,
				command = cmd)
button.pack()
root.mainloop()