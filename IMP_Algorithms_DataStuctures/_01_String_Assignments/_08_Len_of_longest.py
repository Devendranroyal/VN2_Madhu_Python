'''
length of longest string
functionality : length of the longest substring in the string
Convert the string to list first. create a new list with lengths of each element in the list.
find the max length with max().
retrun max len
input : string
'''
str1 = str(input('Enter a string'))


def max_length(string):
    list1 = string.split()
    len_list = []
    for i in list1:
        len_list.append(len(i))
    return max(len_list)


print('Input String :', str1)
print('Length of longest String: ', max_length(str1))
