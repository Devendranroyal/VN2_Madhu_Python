'''
add an item in a tuple.
'''
# Method -1
# Reassigning to tuple
my_tuple = (4, 6, 2, 8, 3, 1)
print('Tuple before adding element : ', my_tuple)
# Tuples are immutable , Therefore new elements cannot be added
# reassigning values again
my_tuple = my_tuple + (9,)
print('After adding : ', my_tuple)

# Adding items in a specific index
my_tuple = my_tuple[:5] + (15, 20, 25) + my_tuple[:5]
print('After adding :', my_tuple)
print()

# Method -2
# Convert to list , append elements and convert to tuple again
tuple2 = ('asha', 'nikhil', 'hyderabad', 'Guntur', 'nishi')
print('Before appending tuple2 - ', tuple2)
list2 = list(tuple2)
list2.append(25)
list2.append('Bangalore')
# Converting to tuple
tuple2 = tuple(list2)
print('After appending tuple2 - ', tuple2)
