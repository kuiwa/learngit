#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
print re.match(r'^\d{3}\-\d{3,8}$', '010-1231145')
#email = raw_input('Please input your Email: ')
email = '123@1.1'
#print email
print re.match(r'^[0-9a-zA-Z\_]+', 'a11')
print re.match(r'^[0-9a-zA-Z\_]+\@[0-9a-zA-Z]+\.[a-z]+', email)