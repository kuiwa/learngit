# -*- coding: utf-8 -*-


def print_day_and_hour(day, hour):
	print "There are %d days in one week." % day
	print "There are %d hours in one day." % hour
	print "So There are %d hours in one week." % (day*hour)
	
from sys import argv
script, pre_day, pre_hour = argv
int_pre_day = int(pre_day)
int_pre_hour = int(pre_hour)
day = 7
half_day = 12
hour = 24
	
# arguments with number
print "1. ",
print_day_and_hour(7, 24)

# arguments with variable
print "2. ",
print_day_and_hour(day, hour)

# arguments with variable and number
print "3. ",
print_day_and_hour(day, 24)

# arguments with math and variable and numbers
print "4. ",
print_day_and_hour(day, 12 + 12)

# arguments with math and variable
print "5. ",
print_day_and_hour(7, half_day + half_day)

# arguments with input

print "please enter number 7: ",
in_day = int(raw_input())
print "please enter number 24: ",
in_hour = int(raw_input())
print "6. ",
print_day_and_hour(in_day, in_hour)

# arguments with input and variable
print "7. ",
print_day_and_hour(in_day, hour)

# arguments with input and number
print "8. ",
print_day_and_hour(7, in_hour)

# arguments with argv of sys module
print "9. ",
print_day_and_hour(int_pre_day, int_pre_hour)

# arguments with argv and variable
print "10. ",
print_day_and_hour(int_pre_day, in_hour)