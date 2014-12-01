# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
root.geometry('800x600')
lb1 = Label(root,text='hello Place',bg='green')
bt1 = Button(root,text='button',bg='red')
lb1.place(relx=0.5,rely=0.5,anchor=CENTER)

bt2 = Button(root,text='button in root',bg='yellow')
bt2.place(anchor=W)
bt1.place(in_=lb1,anchor=NW)
root.mainloop()