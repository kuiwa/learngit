#!/usr/bin/env python
# -*- coding: utf-8 -*-

# number of cars
cars = 100
# max passenger number in a car
# use floating point
space_in_a_car = 4.0
# total number of drivers
drivers = 30
# number of passengers
passengers = 90
# number of can't driven car
cars_not_driven =seven@52827 cars - drivers
# each dirver for each car
cars_driven = drivers
# total passengers number
carpool_capacity = cars_driven * space_in_a_car
# passenger number for each car
average_passengers_per_car = passengers / cars_driven

# print available cars
print "There are", cars, "cars available."
# print available drivers
print "There are only", drivers, "drivers available."
# some car will be empty.
print "There will be", cars_not_driven, "empty cars today."
# max number of passengers can be transport
print "We can transport", carpool_capacity, "people today."
# number of passengers that we have
print "We have", passengers, "to carpool today."
# number of passengers in each car
print "We need to put about", average_passengers_per_car, "in each car."

# show how can I print without spaces between words in print.
# 
print "Hey %s there." % "you"
