# -*- coding: utf-8 -*-

# 引用模块
from Tkinter import *

# resize是用来改变文字大小的，当进度条被拖动时调用
def resize(ev=None):
	# config函数通过设置组件的参数来改变组件，font是字体参数
	label.config(font='Helvetica -%d bold' % scale.get())

# 主窗口
top=Tk()
# 设置主窗口的初始大小600*400
top.geometry('600x400')
# 设置标签字体的初始大小
label=Label(top,text='Hello world!',font='Heivetica -12 bold')
# 管理和显示组件
label.pack(fill=Y,expand=1)
# 创建进度条，并设置进度条参数，from_是初值值，to是最大值，orient表示水平放置，command描述拖动进度条时的动作，即调用resize函数。
scale=Scale(top,from_=10,to=40,orient=HORIZONTAL,command=resize)
# 设置起始位置
scale.set(12)
scale.pack(fill=X,expand=1)
# 创建按钮，作用是退出,activeforegound表示按钮的被按下时的前景色，activebackground表示被按下时的背景色
quit = Button(top,text='QUIT',command=top.quit,activeforeground='white',activebackground='red')
quit.pack()
mainloop()