# -*- coding: utf-8 -*-
'''
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
'''

def near_hundred(n):
    minus100 = abs(n - 100)
    minus200 = abs(n - 200)
    return (minus100 <= 10 or minus200 <= 10)