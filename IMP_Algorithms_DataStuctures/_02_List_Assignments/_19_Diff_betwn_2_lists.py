'''
Difference b/w 2 lists
Convert then to sets and find the difference
'''

list1 = [23, 54, 67, 53, 78, 98, 34]
list2 = [64, 45, 23, 67, 38, 98, 14]


def list_diff(li1 , li2):
    s1 = set(li1)   # list to set
    s2 = set(li2)
    diff_set = s1 -s2
    diff_list = list(diff_set)
    return diff_list


if __name__ =='__main__':
    print(list_diff(list1, list2))