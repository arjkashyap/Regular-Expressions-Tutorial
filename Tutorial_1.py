# Regular expressions tutorial number 1.

import re

# r'' is used to specify a raw string.
# A raw string is the one which does not take \ as an escape chracter.

regex = re.compile(r'[+]\d\d \d{10}')           # reg expression specified and compiled to the regex object
st = str(input("Enter a phone number to check."))       
mo = regex.search(st)                           # mo contains the matched object of the reg exp 

# mo.group() method returns a tuple which contains all the matched expressions from the string.

print("Number is : " + str(mo.group()))     

# Example 2 ip address:
print("Example 2: ")
regex2 = re.compile(r'\d{3}[.]\d{3}[.]\d{3}[.]\d{3}')
ip = str(input("Enter an ip address."))
mo = regex2.search(ip)
print("Ip: " + str(mo.group()))
