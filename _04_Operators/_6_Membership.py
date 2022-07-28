
# Membership operator  in    not in
# 1 in 1  whatsapp group  min 2 members
# Dattypes : int float boolean :: cant check membership
# DataStructures: Membership : String List Tuple Dictionary Set
str1 = 'Hello World'
list1 = [1, 2, 3, 4, 5, 6]
tup1 = (1, 2, 3, 4, 5, 6)
dict1 = {1: 1, 2: 2, 3: 3}
set1 = {1, 2, 3, 4, 5, 6}

# in not in

print(1 in list1)
print(8 not in tup1)
print(8 not in dict1)
print(6 in set1)
print(7 not in set1)
print(10 in set1)

import copy
list1 = [1, 2, 3, 4, 5, 6]
# list2 = [1, 2, 3, 4, 5, 6]  # shallow copy deep copy

list2 = list1
list2 = list1.copy()  # list1.deecopy()

print(list1 == list2, id(list1), id(list2))
print(list1 is list2, id(list1), id(list2))

