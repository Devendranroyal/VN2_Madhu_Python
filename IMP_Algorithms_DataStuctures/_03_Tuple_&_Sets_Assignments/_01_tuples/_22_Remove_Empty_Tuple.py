'''
to remove an empty tuple(s) from a list of tuples
'''
l = [(34, 73, 'abc'),(), (3, 98, 65), ('asha', 'nikhil', 'akhil')]


# Method 1 , Generator obj will be returned
def empty_tup(l1):
    l1 = (tup for tup in l if tup)      # if tup means True if element exists , false if element doesn't exist
    return l1


print('Generator obj after removing empty tuples - ',empty_tup(l))


# Method 2
def rmv_emt_tuple(l1):
    for i in l1:
        if len(i) == 0:
            l1.remove(i)
    return l1


print('After removing empty tuple by method2 - ', rmv_emt_tuple(l))