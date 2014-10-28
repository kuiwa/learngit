# -*- coding: utf-8 -*-

from sys import argv

script, first_argv = argv
print "The first argument is ", first_argv
first_argv = raw_input("please change first_argv: ")
print "Now, the first argument is ", first_argv