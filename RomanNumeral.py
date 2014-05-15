#!/usr/bin/env python
'''
provides functions to convert a number to its roman numeral repesentation. 
'''

__author__  = "Torsten Blank"
__email__   = "Torsten.Blank@gmail.com"

import functools

#define some exceptions
class RomanError(Exception): pass
class OutOfRangeError(RomanError): pass
class NotAnIntegerError(RomanError): pass

def getRomanDIP(number):
    ''' convert a number in its roman numeral. This algorithm can be found in "Dive Into Python" (http://diveintopython.org/) '''
    romanNumeralMap = (('M',  1000),('CM', 900),('D',  500),('CD', 400),('C',  100),('XC', 90),('L',  50),('XL', 40),
                       ('X',  10),('IX', 9),('V',  5),('IV', 4),('I',  1))
    result = ""
    for numeral, integer in romanNumeralMap:
        while number >= integer:
            result += numeral
            number -= integer
    return result

def getDigits(number):
    ''' create a list of digits from number. First entry is the lowest digit. '''
    # error if not an integer
    if int(number) <> number:
        raise NotAnIntegerError, "ERROR: Not an integer"
    # create and return the digits list
    digits = list(map(int, str(number)))
    return digits[::-1]

def getRoman(number):
    ''' convert a number in its roman numeral. This algorithm uses magic with lists and dicts. '''  
    # error if not in range (1,3999)
    if number <= 0 or number >= 4000:
        raise OutOfRangeError, "ERROR: Out of range (1-3999)"
    # define generic and numeral symbols
    romanNumeralVars=['a', 'b' ,'c']
    romanNumeralChars=['I', 'V', 'X', 'L', 'C', 'D', 'M']
    result = ""
    # loop through each digit
    for index, digit in enumerate(getDigits(number)):
        # generate a generalized roman numeral with vars a,b,c 
        part = (digit*'a').replace(9*'a', "ac").replace(5*'a', 'b').replace(4*'a', 'ab')
        # replace a,b,c by the roman "characters" according to the digit-index
        replDict = dict(zip(romanNumeralVars, romanNumeralChars[index*2:index*2+3]))
        part = functools.reduce(lambda s,c: s.replace(c, replDict[c]), replDict, part)
        result = part + result
    return result

# if loaded as the main module, print the roman numerals from 1 to 3999 and test with alternative algorithm 
if __name__ == '__main__':
    for n in range(1,4000):
        rn = getRoman(n)
        rnDIP = getRomanDIP(n)
        print("%s -> %s" % (n, rn))
        if rn != rnDIP:
            print("ERROR for number %s" % n)
            exit(1)

