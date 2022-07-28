'''
unpack a tuple in several variables
'''
my_tuple = ('asha', 25, 'female', 'guntur')

# Unpacking the tuple
(name, age, gender, place) = my_tuple
print('After unpacking')
print(f'name - {name}')
print('age - {}'.format(age))
print('gender - %s'%(gender))
print('Place - ', place)

# Cannot be unpacked
# (name, age, place) = my_tuple