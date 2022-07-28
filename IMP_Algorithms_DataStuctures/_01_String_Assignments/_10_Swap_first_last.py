'''
Code to swap first and last characters
convert the string into list and git the indices of first and last elements.
swap elements. copy it into a new string
'''
str1 = 'The sky is dark'


def swap_str(string):
    list1 = []
    for i in str1:
        list1.append(i)
    list1[0], list1[len(list1) - 1] = list1[len(list1) - 1], list1[0]
    str2 = ''
    for i in list1:
        str2 += i
    return str2


print('Input string : ', str1)
print('After swapping : ', swap_str(str1))
