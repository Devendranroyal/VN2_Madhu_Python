'''
Replace first occurrence of string
functionality : replace the first occurrence with the mentioned character
replace() : replaces part of string with given string
input : string
'''
str1 = str(input('Enter a string :'))
print('Replace char using replace()')
print(str1.replace('h','#',1))
print('\n')
print('Replace char using without replace()')
char = 'h'
new_string = ''
for i in str1:
    if i != char:
        new_string += i
    elif i == char:
        new_string += '#'
print(new_string)


