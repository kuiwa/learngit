# -*- coding: utf-8 -*-

s = 'a b c'
print s.split(" ")
st = 'hello world'
print st.split('o')
print st.split('o', 1)

import os
print os.path.split('c:\\Program File\\123.doc')
print os.path.split('c:\\Program File\\')