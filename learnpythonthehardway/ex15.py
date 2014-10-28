# -*- coding: utf-8 -*-

# import argv parameter from sys module
from sys import argv

# define two variable with argv 
script, filename = argv

# define txt equal file content
txt = open(filename)

# print filename and file content
print "Here's your file %r:" % filename
print txt.read()
txt.close()

# can type the different filename
print "Type the filename again:"
file_again = raw_input("> ")

# define txt_again equal the second filename
txt_again = open(file_again)

# print the second file content
print txt_again.read()
txt_again.close()