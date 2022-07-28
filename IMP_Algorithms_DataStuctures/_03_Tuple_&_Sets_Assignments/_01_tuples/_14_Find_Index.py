'''
find the index of an item of a tuple.
'''
my_tuple = (34, 73, 28 , 99, 45, True, 'Hyderabad')
# Index
print(f'Index of element True is :  {my_tuple.index(True)}')
print(f'Index of element Hyderabad is : {my_tuple.index("Hyderabad")}')
# Throws ValueError if element is not found
# print(f'Index of element 54 is : {my_tuple.index(54)}')