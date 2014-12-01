# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
cv = Canvas(root,bg='white')
txt = cv.create_text((10,10),text='hello text',anchor=W)
cv.select_from(txt,2)
cv.select_to(txt,7)
cv.pack()
root.mainloop()