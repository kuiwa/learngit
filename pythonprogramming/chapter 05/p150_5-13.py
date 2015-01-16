# -*- coding: utf-8 -*-
#
" Change hour:min to mins"
def changeTime(hour, min):
	return (hour * 60 + min)
	
if __name__ == '__main__':
	while True:
		time = raw_input('Enter time(hour:min): > ')
		try:
			hour_min = time.split(':')
			hour = int(hour_min[0])
			min = int(hour_min[1])
		except (ValueError,IndexError) as e:
			print 'Error: ' + str(e)
		else:
			print changeTime(hour, min)
			break