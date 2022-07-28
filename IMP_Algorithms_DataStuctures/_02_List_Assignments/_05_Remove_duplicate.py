'''
Remove duplicates from list
check the count iof each element in list
If count is greater than 1 , them remove element
'''
list1 = [56, 43, 95, 51, 72, 21, 56, 86, 95, 9, 98, 51]
for i in list1:
    if list1.count(i) > 1:
        list1.remove(i)
print(list1)