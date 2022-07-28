'''
Remove even elements and print list
'''
list2 = [56, 43, 95, 72, 21, 86, 98, 51]
new_list2 = []
for i in list2:
    if i%2==1:
        new_list2.append(i)
print("After removing even elements- updated List = ", new_list2)

