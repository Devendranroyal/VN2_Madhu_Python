'''
create the colon of a tuple
'''

from copy import deepcopy

tuple1 = (45, 'hello',[], 82, 63, True, 26)
print('tuple1 - {}'.format(tuple1))
# Making copy of tuple using deepcopy()
tuple2 = deepcopy(tuple1)
print('tuple2 - {}'.format(tuple2))
print('type of tuple1 - {}'.format(type(tuple1)))
print('type of tuple2 - {}'.format(type(tuple2)))
tuple2[2].append(99)
print('tuple2  - {}'.format(tuple2))