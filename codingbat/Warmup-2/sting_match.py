# -*- coding: utf-8 -*-

'''
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
'''

def string_match(a, b):
  num = min(len(a), len(b))
  count = 0
  # because the compared substring's length is 2, so num need to minus 1
  for i in range(num-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count