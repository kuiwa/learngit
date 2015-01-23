#
num = raw_input('Please enter numbers with space seperator:> ')
aList = num.split()
aList.sort(reverse=True)
print aList
