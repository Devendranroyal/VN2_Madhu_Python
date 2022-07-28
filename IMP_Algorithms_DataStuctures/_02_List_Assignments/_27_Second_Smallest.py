'''
Finding a second smallest number
'''

roll_nums = [45, 34,83, 15, 64, 64,  23, 92, 39]
# print(min(roll_nums))

def second_smallest(lst):
    list1 = list(set(lst))  # To remove duplicates
    index_of_ele = list1.index(min(list1))
    list1.pop(index_of_ele)     # Removing smallest
    return min(list1)

if __name__ == '__main__':
    print('Second smallest element is - %s'%(second_smallest(roll_nums)))