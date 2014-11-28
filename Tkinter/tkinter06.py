# -*- coding: utf-8 -*-

from Tkinter import *

def printEventInfo(event):
	print 'button clicked'
	
root = Tk()
button = Button(root,text='button')
button.bind("<Return>",printEventInfo)
button.pack()
button.focus_set()
Button(root,text='FLAT',relief=FLAT).pack()
Button(root,text='GROOVE',relief=GROOVE).pack()
Button(root,text='RAISED',relief=RAISED).pack()
Button(root,text='RIDGE',relief=RIDGE).pack()
Button(root,text='SOLID',relief=SOLID).pack()
Button(root,text='SUNKEN',relief=SUNKEN).pack()
Label(root,text='red',bg='red').pack()
Label(root,text='blue',bg='blue').pack()
Label(root,text='yellow',bg='yellow').pack()

Label(root,bg='red',width=10,height=3).pack()
Label(root,bg='blue',width=10,height=3).pack()
Label(root,bg='yellow',width=10,height=3).pack()
Label(root,bg='green',width=10,height=3).pack()
Label(root,bg='lightblue',width=10,height=3).pack()
Label(root,text='Error',compound='left',bitmap='error').pack()
Label(root,text="Hourglass",compound='left',bitmap='hourglass').pack()
Label(root,text="info",compound='left',bitmap='info').pack()
Label(root,text='questhead',compound='left',bitmap='questhead').pack()
Label(root,text='question',compound='left',bitmap='question').pack()
Label(root,text='warning',compound='left',bitmap='warning').pack()
Label(root,text='gray12',compound='left',bitmap='gray12').pack()
Label(root,text='gray25',compound='left',bitmap='gray25').pack()
Label(root,text='gray50',compound='left',bitmap='gray50').pack()
Label(root,text='gray75',compound='left',bitmap='gray75').pack()
Label(root,text='welcome to jcodeer.cublog.cn',bg='yellow',width=40,height=3,wraplength=80).pack()
Label(root,text='123456789012345678901234567',bg='lightblue',width=40,height=3,wraplength=100,justify='left').pack()
Label(root,text='Chaoyang',bg='red',width=40,height=3,anchor='ne').pack()

root.mainloop()