#!/usr/bin/python3.5

# Matching pattern once or more than once using star

import re

regEx = re.compile(r'([H|h|A|a])*')
s = str(input("How do you laugh: "))

mo = regEx.search(s)
print("Expression: " + str(mo.group()))

