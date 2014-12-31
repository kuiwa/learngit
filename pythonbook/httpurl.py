# -*- coding: utf-8 -*-
# file: httpurl.py
#
from Tkinter import *
import urllib
class Window:
	def __init__(self, root):
		self.root = root
		self.entryUrl = Entry(root)
		self.entryUrl.place(x=5, y=15)
		self.get = Button(root, text='下载页面', command=self.Get)
		self.get.place(x=160,y=12)
		self.edit = Text(root)
		self.edit.place(x=5, y=50)
	def Get(self):
		url = self.entryUrl.get()
		page = urllib.urlopen(url)
		data = page.read()
		self.edit.insert(END, data)
		page.close()
root = Tk()
window = Window(root)
root.minsize(580,380)
root.mainloop()