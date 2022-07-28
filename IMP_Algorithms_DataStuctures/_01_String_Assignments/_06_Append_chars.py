'''
Code to append characters to the sring
functionality : append chars at end of string
Strings are immutable. Therefore we convert string to list, append chars and then convert it into the string
input : string
'''
str1 = str(input('Enter a string :'))
str_append = str(input('Enter chars to append :'))
list_of_str1 = []
for i in str1:
    list_of_str1.append(i)
if len(list_of_str1) == len(str1):
    for i in str_append:
        list_of_str1.append(i)
# converting list into string
appended_string = ''
for i in list_of_str1:
    appended_string += i
print('Given String : ', str1)
print('Appended String: ', appended_string)