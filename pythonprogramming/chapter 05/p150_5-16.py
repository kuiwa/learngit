# -*- coding: utf-8 -*-
#
"Use Payment funtion to calculate the balance"
def Payment(balance, paid):
	balance_paid = [[0, balance]]
	while balance - paid > 0:
		balance -= paid
		balance_paid.append([paid, balance])
	balance_paid.append([balance, 0])
	print 'Amount Remaining'
	print 'Pymy#   Paid       Balance'
	print '-----   ----       -------'
	for i,obj in enumerate(balance_paid):
		print '%4d    $%6.2f    $%6.2f' % (i, obj[0],obj[1]) 
	
if __name__ == '__main__':
	while True:
		balance = raw_input('Enter opening balance: ')
		paid = raw_input('Enter monthly payment: ')
		try:
			balanceF = float(balance)
			paidF = float(paid)
		except ValueError as e:
			print 'Error: ' + str(e)
		else:
			Payment(balanceF, paidF)
			break
