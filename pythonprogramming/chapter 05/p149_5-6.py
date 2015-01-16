# -*- coding: utf-8 -*-
#
def calculate(l):
	a = l[0]
	op = l[1]
	b = l[2]
	if op == "+": result = a + b
	elif op == "-": result = a - b
	elif op == "*": result = a * b
	elif op == "/": result = a / b
	elif op == "%": result = a % b
	elif op == "**": result = a ** b
	else: result = 'wrong operator!'
	return result
if __name__ == '__main__':
	while True:
		s = raw_input('Enter the expression: >')
		l = s.split()
		try:
			floatA = float(l[0])
			floatB = float(l[2])
		except (ValueError,IndexError) as e:
			print 'Error: ' + str(e)
			continue
		l = [floatA, l[1], floatB]
		result = calculate(l)
		if result == 'wrong operator!':
			print result
		else:
			print "%s = %s" % (s, result)
			break
			