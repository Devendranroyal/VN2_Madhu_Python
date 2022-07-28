'''
Last part of string
Write a Python program to get the last part of a string before a specified character.
'''
str1 = 'The night is dark, shining bright with *s all over'
separator = str(input('Enter a character to separate with : '))

before_part = str1.rsplit(separator,1)
print(before_part[0])