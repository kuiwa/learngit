# -*- coding: utf-8 -*-

# define function of counting cheese and crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# count cheeses
	print "You have %d cheeses!" % cheese_count
# count crackers
	print "You have %d boxes of crackers!" % boxes_of_crackers
# print some words
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# start to involve the function	with number
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers =50

# arguments are avariable
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# arguments with math
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# arguments with number and math symbol and variable
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)