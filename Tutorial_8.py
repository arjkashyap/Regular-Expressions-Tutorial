#!/usr/bin/python3.6

# Ignoring case in regular expressions
# Sometimes you just want to match the string regardless of case it is typed in
# In such case, re.I can be passed as an argument to re.compile() function

import re

#rex = re.compile(r'.*', re.I)
#s = str( input("Enter the Name: ") )
#mo = rex.findall(s)
#
#print(mo)


# Substitution using reg ex object
# Substition can be done via sub() method of object

regEx = re.compile('Agent \w+')
st = "Agent Desmond gave the secret Documents to Agent Blackwell."

st = regEx.sub('*****', st)
print(st)
