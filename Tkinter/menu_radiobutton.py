# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Language',menu=filemenu)
vLang = StringVar()
def printItem():
	print 'vLang = ',vLang.get()
for k in['python','java','C++','PHP']:
	filemenu.add_radiobutton(label=k,command=printItem,variable=vLang)
root['menu']=menubar
root.mainloop()