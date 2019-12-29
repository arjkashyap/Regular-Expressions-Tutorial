#!/usr/bin/python3.6

# Matching using a wild card character
# The dot ( . ) will match any single character except for a new line

import re

regEx = re.compile(r'.at')
s = "The cat with the hat sat on the mat with a bat _at"
mo = regEx.findall(s)

print("Matched characters: " + str( mo ))

# The dot can also be used along with *
# Like stated earlier, * is greedy method to match any or none character

regEx2 = re.compile(r'First Name: (.*) Last Name: (.*)')
firstName = str( input("Enter First Name: ") )
lastName = str( input("Enter Last Name: ") )

st = "First Name: " + firstName + " Last Name: " + lastName
mo2 = regEx2.findall(st)

for i in mo2:
    print(i, end = '')

# Passing re.DOTALL as an argument in re.compile() wil match all chracters including newline
# ex: re.compile(r'.*', re.DOTALL)
