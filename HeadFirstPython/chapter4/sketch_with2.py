# -*- coding: utf-8 -*-
# file: chapter4/sketch.py
#
import nester
man = []
other = []
try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			line_spoken = line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass
	data.close()
except IOError as err:
	print ('The datafile is missing!' + str(err))
try:
	with open('man_data.txt', 'w') as man_file:
		nester.print_lol(man, fh=man_file)
	with open('other_data.txt', 'w') as other_file:
		print (other, file=other_file)
	#with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
except IOError as err:
	print ('File Error: ' + str(err))
	