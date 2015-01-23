#
import datetime
def tranDate(date):
	dateB = []
	for i in date.split('/'):
		dateB.append(int(i))
	return dateB
def days(date1, date2):
	dayDict = { 1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334 }
	days = 0
	mon1, day1, year1 = tranDate(date1)
	mon2, day2, year2 = tranDate(date2)
	if year1 == year2:
		days += abs((dayDict[mon1] + day1) - (dayDict[mon2] + day2))		
	else:
		if year1 < year2:
			mon1, day1, year1, mon2, day2, year2 = mon2, day2, year2, mon1, day1, year1
		days += 365 - dayDict[mon2] - day2
		days += 365 * (year1 - year2 - 1)
		days += dayDict[mon1] + day1
	return days
def daysB(date1, date2, today=False):
	mon1, day1, year1 = tranDate(date1)
	mon2, day2, year2 = tranDate(date2)
	Date1 = datetime.date(year1, mon1, day1)
	Date2 = datetime.date(year2, mon2, day2)
	if today:
		return datetime.date.today() - Date2
	return Date1 - Date2
if __name__ == '__main__':
	while True:
		date1 = '1/20/2015'
		print 'date1 is %s' % date1
		date2 = raw_input('Enter date2: > ')
		print days(date1, date2)
		print daysB(date1, date2)
		print daysB(date1, date2, today=True)
		break
