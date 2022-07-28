'''
Code to slice substring from given string.
use slice() to return substring from the string
input : string
'''
str1 = str(input('Enter a string :'))
begin = int(input('Enter the index to start with:'))
end = int(input('Enter the index to end with:'))
inc = int(input('no of steps to increment:'))
str2 = str1[begin: end: inc]
print('Input String : ', str1)
print('After Slicing : ', str2)