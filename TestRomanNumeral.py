#!/usr/bin/env python
'''
print the roman numerals of 10 random numbers
'''

from RomanNumeral import getRoman
import random

random.seed()
for i in range(0,10):
    n = random.randint(1,3999)
    print("%s -> %s" % (n, getRoman(n)))
