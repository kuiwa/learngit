# -*- coding: utf-8 -*-
# file: tkinterDialog.py
#
from Tkinter import *
from tkMessageBox import *
class MyDialog:
	def __init__(self, root):
		self.top = Toplevel(root)
		label = Label(self.top, text='Please Input')
		label.pack()
		self.entry = Entry(self.top)
		self.entry.pack()
		self.entry.focus()
		button = Button(self.top, text='OK', command=self.OK)
		button.pack()
	def OK(self):
		self.input = self.entry.get()
		self.top.destroy()
	def get(self):
		return self.input
class MyButton():
	def __init__(self, root, type):
		self.root = root
		if type == 0:
			self.button = Button(root, text='Create', command = self.Create)
		else:
			self.button = Button(root,
								text = 'Quit',
								command = self.Quit)
		self.button.pack()
	def Create(self):
		d = MyDialog(self.root)
		self.button.wait_window(d.top)
		showinfo('Python','You input:\n' + d.get())
	def Quit(self):
		self.root.quit()
root = Tk()
MyButton(root, 0)
MyButton(root, 1)
root.mainloop()