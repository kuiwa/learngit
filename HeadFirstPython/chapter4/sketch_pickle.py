# -*- coding: utf-8 -*-
# file: sketch_pickle.py
#
import pickle
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
	with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
		pickle.dump(man, man_file)
		pickle.dump(other, other_file)
	with open('man_data.txt', 'rb') as man_file:
		manfile = pickle.load(man_file)
		nester.print_lol(manfile)
except IOError as err:
	print('File error: ' + str(err))
except pickle.PickleError as perr:
	print('Picking error: ' + str(perr))