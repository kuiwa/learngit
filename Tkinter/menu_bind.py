# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Language',menu=filemenu)
def printItem():
	print 'popup menu'
	
for k in ['python','java','C++','PHP']:
	filemenu.add_command(label=k,command=printItem)
	filemenu.add_separator()

def popup(event):
	menubar.post(event.x_root,event.y_root)
root.bind('<Button-3>',popup)
root.mainloop()