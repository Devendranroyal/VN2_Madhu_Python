'''
slice a tuple
'''
my_tuple1 = (45, 83, 28, 93, True, 'Blr', 99, 'python', 'orange')
flowrs = ('Roses', 'lilies', 'daffodils', 'lotus', 'jasmine', 'Marigold')
my_tuple2 = (flowrs, 'fruits', 'colors', 'essentials')

slice1 = my_tuple1[3:6]
print('Slice of my_tuple', slice1)

# Slices till last element if the index is out of range
slice2 = flowrs[2:8]
print(f'Slice of flowrs - {slice2}')

# Negative Index
slice3 = my_tuple2[0:3]
print('Slice3 - ',slice3)
