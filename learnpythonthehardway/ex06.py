
# -*- coding: utf-8 -*-


# use %d...% to show 10
x = "There are %d types of people." % 10
# binary variable
binary = "binary"
# do_not variable
do_not = "don't"
# use %s to define y variable
y = "Those who know %s and those who %s." % (binary, do_not)

# show x
print x
# show y
print y

# put x into a sentence and use %r to print x
# %r is best for debugging.
print "I said: %r." % x
# put y into a sentence and use %s to print y
print "I also said: '%s'." % y
# hilarious愉快的
hilarious = False
# 笑话评估
joke_evaluation = "Isn't that joke so funny?! %r"

# print evaluation result
print joke_evaluation % hilarious

# w variable
w = "This is the left side of..."
# e variable
e = "a string with a right side."

# concentrate w and e
print w + e