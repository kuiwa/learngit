# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
lb = Listbox(root)
s1 = Scrollbar(root)
s1.pack(side=RIGHT,fill=Y)
lb['yscrollcommand']=s1.set
for i in range(100):
	lb.insert(END,str(i))
lb.pack(side=LEFT)
s1['command']=lb.yview
root.mainloop()