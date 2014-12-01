# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
root.geometry('800x600')
lb = Label(root,text='hell place')
lb.place(x=50,y=100,anchor=NW)
lb1 = Label(root,text='place1',bg='green')
lb2 = Label(root,text='place2',bg='red')
lb1.place(relx=0.5,rely=0.5,anchor=CENTER,x=-200,y=-200)
lb2.pack()
root.mainloop()