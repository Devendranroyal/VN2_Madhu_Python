'''
Check if a given key already exists in a dictionary.
'''
dict1 = {'nikhil': 40, 'asha': 2, 'bavana': 1, 'disha': 3, 'Nishi': 28, 'priya': 30}


def check_key(x):
    if x in dict1:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')


check_key('asha')
check_key('Misha')