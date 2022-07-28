'''
code to replace a substring with other string
input : string
Method 1
print('------------------method 1---------------')
str1 = str(input('Enter a string : '))
str_replace = str(input('Enter a sub-string to replace:'))
list_str1 = str1.split()
pos = int(input('Enter the position of substring to be replaced : '))
list_str1[pos] = [str_replace]

replaced_string = ' '.join(list_str1[0 : pos] + list_str1[pos] + list_str1[pos+1:])
print('Sring before replacement :', str1)
print('Replaced String :', replaced_string)
'''
print('--------------------method 2------------------')
str1 = str(input('Enter a string : '))
target_str = str(input('Replace the substring : '))
sub_str = str(input('With the substring : '))
    #str(input('Enter the position of substring to be replaced : '))
list_str2 = str1.split()
for n, i in enumerate(list_str2):
    if i == target_str:
        list_str2[n] = sub_str
str_after_replacement = ' '.join(list_str2)
print('Sring before replacement :', str1)
print('Replaced String :', str_after_replacement)