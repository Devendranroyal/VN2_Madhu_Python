'''
Smallest number from list
code to find the smallest element in the list
'''
list1 = [56, 43, 95, 72, 21, 86, 9, 98, 51]
min_num = list1[0]
for n in range(1, len(list1)):
    if list1[n] < min_num:
        min_num = list1[n]
print('Smallest num in list1 :', min_num)
