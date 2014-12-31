# -*- coding: utf-8 -*-
# file: tkinterFileDialog.py
#
from Tkinter import *
from tkFileDialog import *
def FileOpen():
	r = askopenfilename(title = 'FileOpen',
		filetypes=[('Python','*.py *.pyw'),('All files', '*')])
	print r
def FileSave():	
	r = asksaveasfilename(title = 'FileSave',
		initialdir = r'E:\Python',
		initialfile = 'test.py')
	print r
root = Tk()
button1 = Button(root,
				text = 'File Open',
				command = FileOpen)
button1.pack(side='left')
button2 = Button(root,
				text = 'File Save',
				command = FileSave)
button2.pack(side='left')
root.mainloop()