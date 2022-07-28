'''
Printing elements in ascending order
'''

li1 = [23, 45, 32, 92, 28, 83, 27]


def ascending_ord(lst):
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                temp = lst[i];
                lst[i] = lst[j];
                lst[j] = temp;
    return lst


print(ascending_ord(li1))
