# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
root.geometry('80x80+0+0')
print root.pack_slaves()
Label(root,text='pack1',bg='red').pack(fill=Y,expand=1,side=LEFT)
Label(root,text='pack2',bg='blue').pack(fill=BOTH,expand=1,side=RIGHT)
Label(root,text='pack3',bg='green').pack(fill=X,expand=0,side=LEFT)
print root.pack_slaves()
root.mainloop()