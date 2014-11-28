# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
root.title('hello root title')
t1 = Toplevel()
t1.title('hello Toplevel title')
t1.geometry('400x300')
Label(t1,text='hello label').pack()
root.mainloop()