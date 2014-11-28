# -*- coding: utf-8 -*-

from Tkinter import *
root = Tk()
t = Text()
for i in range(1,10):
	t.insert(1.0,'0123456789\n')
a = 'test_mark'
def forwardChars():
	t.mark_set(a,CURRENT+'+5c')
def backwardChars():
	t.mark_set(a,CURRENT+'-5c')
def forwardLines():
	t.mark_set(a,CURRENT+'+5l')
def backwardLines():
	t.mark_set(a,CURRENT+'-5l')
def lineStart():
	t.mark_set(a,CURRENT+' linestart')
def lineEnd():
	t.mark_set(a,CURRENT+' lineend')
def wordStart():
	t.mark_set(a,CURRENT+' wordstart')
def wordEnd():
	t.mark_set(a,CURRENT+' wordend')
t.mark_set(a,CURRENT)
Button(root,text='forward 5 chars',command= forwardChars).pack(fill=X)
Button(root,text='backward 5 chars',command=backwardChars).pack(fill=X)
Button(root,text='forward 5 lines',command=forwardLines).pack(fill=X)
Button(root,text='backward 5 lines',command=backwardLines).pack(fill=X)
Button(root,text='line start',command=lineStart).pack(fill=X)
Button(root,text='line end',command=lineEnd).pack(fill=X)
Button(root,text='word start',command=wordStart).pack(fill=X)
Button(root,text='word end',command=lineEnd).pack(fill=X)
def insertText():
    t.insert(INSERT,'insert')
def currentText():
    t.insert(CURRENT,'current')
def markText():
    t.insert(a,'mark')
Button(root,text = 'insert jcodeer.cublog.cn',command = insertText).pack(fill = X)
Button(root,text = 'current jcodeer.cublog.cn',command = currentText).pack(fill = X)
Button(root,text = 'mark jcodeer.cublog.cn',command = markText).pack(fill = X)
t.pack()

t.pack()
root.mainloop()