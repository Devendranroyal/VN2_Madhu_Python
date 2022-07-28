'''
Get the maximum and minimum value in a dictionary.
'''
test_dict = {'acd': 7, 'for': 2, 'hgs': 81, 'abd': 6, 'msd': 1}
roll_dict = {'maya': 6, 'misha': 73, 'asha': 65, 'nishi': 47, 'nikhil': 76, 'madhu': 61}

least_key = [key for key in test_dict if all(test_dict[temp] >= test_dict[key] for temp in test_dict)]

max_key = [key for key in test_dict if all(test_dict[temp] <= test_dict[key] for temp in test_dict)]

# print('Keys with minimum values are :', least_key)
# print('Keys with max value :', max_key)
print('min value of test_dict :', test_dict[least_key[0]])
print('max value of test_dict :', test_dict[max_key[0]])

print('------------------------------------------------------------------------------')
key_max = max(roll_dict.keys(), key=(lambda k: roll_dict[k]))
key_min = min(roll_dict.keys(), key=(lambda k: roll_dict[k]))

print('max value of roll_dict :', roll_dict[key_max])
print('min value of roll_dict :', roll_dict[key_min])