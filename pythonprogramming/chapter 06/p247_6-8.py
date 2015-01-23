# -*- coding: utf-8 -*-
#
def transNum(numInt):
	num2eng = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14: 'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'ninteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninty', 100:'hundred', 1000:'thousand'}
	eng = ''
	if 1000 <= numInt <= 9999:
		thousand, numInt = divmod(numInt, 1000)
		eng += '%s-%s ' % (num2eng[thousand], num2eng[1000])
	if 100 <= numInt <= 999:
		hundred, numInt = divmod(numInt, 100)
		eng += '%s-%s ' % (num2eng[hundred], num2eng[100])
	if 21 <= numInt <= 99:
		ty, numInt = divmod(numInt, 10)
		eng += '%s-%s' % (num2eng[ty*10],num2eng[numInt])
	elif 1 <= numInt <= 20:
		eng += '%s' % (num2eng[numInt])
	return eng
while True:
	num = raw_input('Enter a number:> ')
	try:
		numInt = int(num)
	except ValueError as e:
		print 'Error: ' + str(e)
	else:
		if 0 < numInt <= 9999:
			print transNum(numInt)
			break
		else:
			print 'the range of number is 0-9999!'

