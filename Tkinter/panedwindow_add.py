# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
panes = PanedWindow(orient = VERTICAL)
panes.pack(fill=BOTH,expand=1)
for w in [Label,Button,Checkbutton,Radiobutton]:
	panes.add(w(panes,text='hello'))
root.mainloop()