# -*- coding: utf-8 -*-
# file: client.py
#
from Tkinter import *
import socket
class Window:
	def __init__(self, root):
		label1 = Label(root, text='IP')
		label2 = Label(root, text='Port')
		label3 = Label(root, text='Data')
		label1.place(x=5, y=5)
		label2.place(x=5, y=30)
		label3.place(x=5, y=55)
		self.entryIP = Entry(root)
		self.entryIP.insert(END,'127.0.0.1')
		self.entryPort = Entry(root)
		self.entryPort.insert(END,'1051')
		self.entryData = Entry(root)
		self.entryData.insert(END, 'Hello')
		self.Recv = Text(root)
		self.entryIP.place(x=40, y=5)
		self.entryPort.place(x=40, y=30)
		self.entryData.place(x=40, y=55)
		self.Recv.place(y=115)
		self.send = Button(root, text='发送数据', command=self.Send)
		self.send.place(x=40,y=80)
	def Send(self):
		try:
			ip = self.entryIP.get()
			port = int(self.entryPort.get())
			data = self.entryData.get()
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.connect((ip, port))
			client.send(data)
			rdata = client.recv(1024)
			self.Recv.insert(END, 'Server:' + rdata .decode() + '\n')
			client.close()
		except:
			self.Recv.insert(END, '发送错误\n')
root = Tk()
window = Window(root)
root.mainloop()