# -*- coding: utf-8 -*-
# file: tkinterRCButton.py
#
from Tkinter import *
root = Tk()
r = StringVar()
r.set('1')
radio = Radiobutton(root,
					variable = r,
					value = '1',
					indicatoron = 0,
					text = 'Radio1')
radio.pack()
radio = Radiobutton(root,
					variable = r,
					value = '2',
					indicatoron = 1,
					text = 'Radio2')
radio.pack()
radio = Radiobutton(root,
					variable = r,
					value = '3',
					indicatoron = 2,
					text = 'Radio3')
radio.pack()
radio = Radiobutton(root,
					variable = r,
					value = '4',
					indicatoron = 3,
					text = 'Radio4')
radio.pack()
c = IntVar()
c.set(1)
check = Checkbutton(root,
					text = 'Checkbutton',
					variable = c,
					indicatoron = 0,
					onvalue = 1,
					offvalue =2)
check.pack()
root.mainloop()