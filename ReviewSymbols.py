"""
Following is a brief sumamry of all notations covered so far:

? -     Matches zero or one of the preceding group.
* -     Matches zero or more of the preceding group.
+ -     Matches one or more of the preceding group.
{n}  -  Matches exactly n of the preceding group.
{n, } - Matches n or more times the preceding group.
{, m} - Matches zero to m time the preceding group.
{n, m}- Matches the preceding group min n times or max m times.
{n, m}? or +?- Performs a non-greedy search for the preceding pattern.
^spam -  States the string must start with spam.
spam$ - States the string must end with spam.
. -     Matches any character except the newline characters.

\d \w \s - Matches Digit, Word, or Space character respectively.
\D \W \S - Matches anything except Digit, Word, or Space character.
[abc] - Matches any char between brackets.
[^abc]- Matches any char not between the brackets
"""
