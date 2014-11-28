# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
cv = Canvas(root,bg='white')
rt = cv.create_rectangle(10,50,100,200,outline='red',stipple='gray12',fill='blue')
cv.pack()
cv.coords(rt,(40,40,80,80))
root.mainloop()