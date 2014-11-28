# -*- coding: utf-8 -*-

from Tkinter import *

def printEventInfo(event):
	print "event.time = ", event.time
	print "event.type = ", event.type
	print "event.WidgetId = ", event.widget
	print "event.KeySymbol = ", event.keysym
	
root = Tk()
b = Button(root,text='Button2')
b.bind("<Return>", printEventInfo)
b.pack()
b.focus_set()
b1 = Button(root,text='30x1',width=30,height=2)
b2 = Button(root,text='30x2')
b2['width'] = 30
b2['height'] = 3
b3 = Button(root,text='30x3')
b3.configure(width=30,height=3)
b1.pack()
b2.pack()
b3.pack()

root.mainloop()