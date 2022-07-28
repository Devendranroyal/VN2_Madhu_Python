'''
Remove odd index values
functionality : Remove the chars at off index
input: string
'''
str1 = str(input('Enter String: '))


def rem_index(string):
    list_of_str1 = []
    for n, i in enumerate(string, 0):
        if n % 2 == 0:
            list_of_str1.append(i)
    str2 = ''
    for i in list_of_str1:
        str2 += i
    return str2


print('Input string : ', str1)
print('After removing : ', rem_index(str1))
