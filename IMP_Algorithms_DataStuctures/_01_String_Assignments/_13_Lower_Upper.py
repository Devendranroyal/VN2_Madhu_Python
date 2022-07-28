'''
13
Upper lower case of a string


print('----------------------------Method 1------------------')

str1 = 'Another Fun Day'
list1 = []
for i in str1:
    if i.isupper():
        # check the case of the char
        # If upper case convert to lower case
        list1.append(i.lower())
    elif i.islower():
        list1.append(i.upper())
    else:
        list1.append(i)
str2 = ''
str2 = ''.join(list1)
print(str2)
'''
print('----------------------------Method 2 (short syntax)-----------')
str2 = 'Good Days Are Yet To Come'
str3_new = (i.lower() if i.isupper() else i.upper() for i in str2)
print(str3_new)   # str3_new is generator object
print(type(str3_new))
print(''.join(str3_new))





# case_rev_str =''.join(c.lower() if c.isupper() else c.upper() for c in str2)
# print(case_rev_str)