#!/usr/bin/env python
# -*- coding: utf-8 -*-

# How many CEs on CDM1 of CELL361?
print "Each CCU has %d CEs." % 32
print "So the number of CEs is", 32 * 6

print "If we minus one CCU, it becomes", 32 * 6 - 32
print "Each page on SDP can show %d CEs." % 16
print "So one CCU should be showed on %d pages." % ( 32 / 16 )

print "There are two CDMs on CELL361."
print "So the total number of CEs is", 32 * 6 + 32 * 5