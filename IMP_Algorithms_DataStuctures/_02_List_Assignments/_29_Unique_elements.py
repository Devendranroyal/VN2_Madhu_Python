'''
get unique values from list
'''

list1 = [45, 23, 48,34, 98, 82, 34, 67]
unique_ele = []

def unique_elements(lst):
    for i in lst:
        if lst.count(i) == 1:
            unique_ele.append(i)

unique_elements(list1)
print('Unique elements in the list are - %s'%(unique_ele))