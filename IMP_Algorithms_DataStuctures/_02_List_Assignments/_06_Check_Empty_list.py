'''
6 . Check if the list is empty
'''
list1 = []
list2 = [56, 43, 95, 72, 21, 86, 98, 51]

# if len(list1) == 0:
#     print('list1 is empty')
# else:
#     print('list1 is not empty')

def empty_lst(lst):
    if not lst:
        return 'not empty'
    else:
        return 'empty'


print('list1 is ', empty_lst(list1))
print('list2 is ', empty_lst(list2))
