'''
Length of first 3 chars
Write a Python function to get a string made of its first three characters of a specified string.
If the length of the string is less than 3 then return the original string.
'''
str1 = 'Indigo red'


def three_chars(string):
    return string[0:3]


print('Input String :', str1)
print('First 3 chars : ', three_chars(str1))