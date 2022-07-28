'''
Merge two Python dictionaries
'''
dict1 = {'nikhil': 40, 'asha': 2, 'bavana': 1, 'disha': 3, 'Nishi': 28, 'priya': 30}
dict2 = {6: 36, 2: 4, 3: 9, 8: 64, 13: 169, 1: 1, 11: 121, 4: 16}
dict1.update(dict2)
print(dict1)