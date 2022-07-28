'''
Code to count character in string
functionality  : to giv the count of how many times a character is repeated
input : string
'''
import string
str1 = str(input('Enter a string :'))
resp = {}
for i in str1:
    if i in str1:
        resp[i] = resp.get(i, 0) + 1
        pass
    else:
        resp[i] = resp.count(i)
#print(resp)
#for x in resp:
    #print(x ,' : ', resp[x])
print(resp)
print(resp.get('h',1)+1)