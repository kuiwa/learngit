# -*- coding: utf-8 -*-

from Tkinter import *
from SimpleDialog import *
from SimpleDialog import *
root = Tk()
dlg = SimpleDialog(root,text='simplediaglog',buttons=['Yes','No','cancel'],default=0,)
print dlg.go()
root.mainloop()