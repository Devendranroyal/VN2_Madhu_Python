'''
reverse a tuple.
'''
my_tuple = (34, 27, 28, 'abcd', 83, 'caucasian', True)


def rev_tuple(tup):
    my_list = list(tup)
    rev_list = []
    length = len(my_list)
    for i in range(1, length+1):
        x = my_list[length-i]
        rev_list.append(x)
        # print(rev_list)
    return tuple(rev_list)


print(f'Tuple before reversing - {my_tuple}')
print(f'Tuple after reversing - {rev_tuple(my_tuple)}')

# li= [34, 27, 28, 'abcd', 83, 'caucasian', True]
# print(li[7-7])