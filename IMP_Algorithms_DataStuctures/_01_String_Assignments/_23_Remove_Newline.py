'''
program to remove a newline in Python
'''
import re

str1 = 'asha\n nikhil\n Thumma'
list_of_str = []

final_str = ''
for i in str1:
    pass # list_of_str.append(i)
for i in str1:
    list_of_str.append(re.sub('\n', ' ', i))
final_str = ''.join(list_of_str)
print(str1)
print(final_str)