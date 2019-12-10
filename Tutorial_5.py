#!/usr/bin/python3.5


# Matching one or more group using Plus
# The Plus symbol requires the preceding group to be entered atleast once and can be any number of times

import re

reExp = re.compile(r'(B|b)at(wo)+man')
s = str(input("Enter wo in batman any number of times greater than zero: "))

mo = reExp.search(s)

print("Expression found: " + str(mo.group()))



