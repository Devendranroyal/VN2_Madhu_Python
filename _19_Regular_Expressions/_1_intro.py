"""
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
"""
import re
#match function
#re.match(pattern=None, string=None, flags=None) # returns match object on success
                                                # None on failure
'''
pattern : This is the regular expression to be matched.
string  : This is the string, which would be searched to match the pattern at the beginning of string.
flags   : You can specify different flags using bitwise OR (|). 
          These are modifiers, which are listed in the table below.
Match object methods
--------------------
group(num=0) :  This method returns entire match (or specific subgroup num)
groups()     :  This method returns all matching subgroups in a tuple (empty if there weren't any)
'''

import re
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")