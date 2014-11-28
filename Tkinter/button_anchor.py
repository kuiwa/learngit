# -*- coding: utf-8 -*-

from Tkinter import *

root = Tk()
anchor_a = ['n','s','e','w','ne','nw','se','sw']
for a in anchor_a:
	Button(root,text='anchor',anchor=a).pack()
for b in [0,1,2,3,4]:
	Button(root,text=['bd=',b],bd=b).pack()
for r in ['flat','groove','raised','ridge','solid','sunken']:
	Button(root,text=['r=',r],relief=r,width=30).pack()
root.mainloop()