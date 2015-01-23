# -*- coding: utf-8 -*-
#
" Change hour:min to mins"
def changeTime(time):
	if ':' in time:
		try:
			hour_min = time.split(':')
			hour = int(hour_min[0])
			min = int(hour_min[1])
		except (ValueError,IndexError) as e:
			print 'Error: ' + str(e)
		else:	
			return (hour * 60 + min)
	else:
		try:
			min = int(time)
		except (ValueError) as e:	
			print 'Error: ' + str(e)
		else:
			return '%s:%s' % divmod(min, 60)
if __name__ == '__main__':
	while True:
		time = raw_input('Enter time(hour:min): > ')
		print changeTime(time)
		break