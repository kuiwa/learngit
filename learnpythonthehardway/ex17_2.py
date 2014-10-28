# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copy from %s to %s." % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The %s file is %d bytes long." % (from_file, len(indata))
print "Does %s file exist? %s" % (to_file, exists(to_file))
print "Hit RETURN to continue, or press CTRL+C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

in_file.close()
out_file.close()

print "Alright, all done."
