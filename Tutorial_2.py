#!/usr/bin/python3.5
# Regular expressions tutorial number 2.

# Matching regex using the pipe method
# a | b is used to specify a or b 
import re

regEx = re.compile(r'[b/B]atman|[s/S]uperman')
s = str(input("Enter Batman or Superman: "))
mo = regEx.search(s)

print("Expression matched: " + str(mo.group()))

s = str(input("Enter anything related to bat ex: batmobile "))
re2 = re.compile(r'([B|b])at(mobile|cave|man|woman)')
mo2 = re2.search(s)

print("Expression matched " + str(mo2.group()))
print("Exp group index 1: " + str(mo2.group(1)))
