'''
Largest number from list
code to find the largest element in the list
'''
list1 = [56,43,95,72,21,86,98,51]
max_num = list1[0]
for n in range(1,len(list1)):
    if list1[n] > max_num:
        max_num = list1[n]
print('largest num in list1 :', max_num)