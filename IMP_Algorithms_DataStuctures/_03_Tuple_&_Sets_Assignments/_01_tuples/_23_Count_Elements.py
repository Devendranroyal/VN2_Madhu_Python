'''
Count the elements in a list until an element is a tuple
'''
my_tuple = [34, 74, 29, 'asha', True, (34, 52, 1), 63, 67]
tuple2 = [56, 23, 'abcd', True, (3, 6, 65), [3, 7]]


# Method -1 using isinstance()
def ele_count(tup):
    counter = 0
    for i in tup:
        if isinstance(i, tuple):
            break
        counter += 1
    return counter


print(f'No of elements before a tuple - {ele_count(my_tuple)}')


# Method -2 for loop
def ele_count2(tup):
    count = 0
    for i in tup:
        if type(i) == tuple:
            break
        count += 1
    return count


print(f'No of elements before a tuple - {ele_count2(tuple2)}')

