#!/usr/bin/python3.5

# Using charachter classes in reg ex

"""
\d
Any numeric digit from 0 to 9.

\D
Any character that is not a numeric digit from 0 to 9.

\w
Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)

\W
Any character that is not a letter, numeric digit, or the underscore character.

\s
Any space, tab, or newline character. (Think of this as matching “space” characters.)

\S
Any character that is not a space, tab, or newline.

"""

import re

regEx = re.compile(r'[aeiouAEIOU]')

s = str(input("Enter a string: "))

# The findall() methods returns all matching strings of expressions in form of a list
mo = regEx.findall(s)

print("Expressions: " + str(mo))

# ^ is used to specify the character expressions not matching the elements
regEx2 = re.compile(r'[^aeiouAEIOU]')
mo = regEx2.findall(s)
print("Expressinos not matching reg ex: " + str(mo))

# The ^ also indicates that the regular expression should start with this expression
# The $ indicates that the regular expression should end with the preceding expressino

# ^abc$ indicates the exp must start with a and end with c consisting b
regEx3 = re.compile(r'^[Hh]ello$')
st = str(input("Enter a string to check regular exp with ^ and $"))
mo = regEx3.findall(st)
print("Expression found:  " + str(mo))







 
