'''
To sort (ascending and descending) a dictionary by value
'''
dict1 = {'nikhil': 40, 'asha': 2, 'bavana': 1, 'disha': 3}

l = list(dict1.items())  # convet the given dict. into list
print('dict1 - ',dict1)
l.sort()  # sort the list
# print('Ascending order is', l)
dict_ascend = dict(l)
print('Ascending order is', dict_ascend)

l.sort(reverse=True)  # sort in reverse order
dict_descend = dict(l)
# print('Descending order is', l)
print('dict in descending order - ', dict(l))