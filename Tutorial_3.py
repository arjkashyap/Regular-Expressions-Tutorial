#!/usr/bin/python3.5
#Optional matching with question mark ?

import re

# ? is preceded by an expression which is optional
regEx = re.compile(r'[b/B]at(wo)?man')
t
s = str(input("Batman/woman: "))
mo = regEx.search(s)
print("Phone number: " + str(mo.group()))

regEx2 = re.compile(r'(\+\d{2})?( )?(\d{10})')
s2 = str(input("Enter phone number: "))
mo2 = regEx2.search(s2)
print("Phone number: " + mo2.group())
