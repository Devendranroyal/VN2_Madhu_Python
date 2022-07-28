'''
find the repeated items of a tuple
'''
import collections

# Method 1
# Convert to list and count the variables
tuple1 = (34, 45, 72, 18, 72, 92, 63, 72, 92, 18)


def ele_counter(tup):
    l1 = []
    for i in tup:
        if tup.count(i) > 1:
            if i in l1:
                pass
            else:
                l1.append(i)
    return l1


print(f'Repeated Elements in tuple1 - {ele_counter(tuple1)}')
print()


# Method- 2
tuple2 = [45, 72, 8, 'hyd', 45, True, 92, 72 ]
tuple3 = [True, 34, 'abc', 48, 24]


def rep_ele(tup):
    flag = False
    val = collections.Counter(tup)
    # print('val - ', val)
    unique_list = list(set(tup))
    # print(f'Unique list - {unique_list}')
    repeated_elements = []
    for i in unique_list:
        if val[i] >= 2:
            flag = True
            repeated_elements.append(i)
    if not flag:
        return 'Duplicates do not exist'
    return repeated_elements


print(f'Repeated elements in tuple2 - {rep_ele(tuple2)}')
print(f'Repeated elements in tuple3 - {rep_ele(tuple3)}')