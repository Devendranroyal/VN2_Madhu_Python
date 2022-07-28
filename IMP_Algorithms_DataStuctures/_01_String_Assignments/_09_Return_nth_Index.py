'''
Code to return nth index character from string
'''
str1 = str(input('Enter a string: '))
n = int(input('Index : '))

def nth_index(string):
    list1 = []
    for i in string:
        list1.append(i)
    return list1[n]


print('Input String : ',str1)
print(n, 'th index char is :',nth_index(str1))