# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
root.geometry('800x600')
fm1 = Frame(root,bg='red',width=40,height=40)
fm2 = Frame(root,bg='blue',width=40,height=40)
fm3 = Frame(fm1,bg='yellow',width=20,height=20)

lb1 = Label(fm1,text='label1',bg='green')
lb1.place(in_=fm1,relx=0.5,rely=0.5,anchor=CENTER)
bt1 = Button(fm1,text='button1',bg='red')
bt1.place(in_=fm3,anchor=W)
fm1.pack()
fm2.pack()
fm3.pack()
root.mainloop()