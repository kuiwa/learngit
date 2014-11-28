# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
ws = []
panes = PanedWindow(orient = VERTICAL)
panes.pack(fill=BOTH,expand=1)
for w in [Label,Button,Checkbutton,Radiobutton]:
	ws.append(w(panes,text='hello'))
for w in ws:
	panes.add(w)
panes.forget(ws[0])
panes.remove(ws[-1])
panes.paneconfig(Label(panes,text='paneconfig'),after = ws[1])
root.mainloop()