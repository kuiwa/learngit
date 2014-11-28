# -*- coding: cp936 -*-
# 使用edit_xxx函数实现编辑常用功能
from Tkinter import *
root = Tk()
t = Text(root)
for i in range(10):
    t.insert(1.0,'0123456789\n')
t.pack()
# 定义回调函数
# 撤消回调函数
def undoText():
    t.edit_undo()
# 插入文本函数
def insertText():
    t.insert(1.0,'insert text')
Button(root,text = 'undo',command = undoText).pack(fill = X)
Button(root,text = 'insert text',command = insertText).pack(fill = X)

root.mainloop()
