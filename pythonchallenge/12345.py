# -*- coding: utf-8 -*-

import urllib.request  
import re  
  
nextno = 12345  
      
for i in range(500):  
	page = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % (nextno))  
	text = page.read().decode("utf-8")  
	nextno = re.search('and the next nothing is (\d+)', text)  
	if nextno:  
			nextno = nextno.groups()[0]  
			print(nextno+'\n')  
	else:  
			print(text)  
			break  