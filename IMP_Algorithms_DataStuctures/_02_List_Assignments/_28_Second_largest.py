'''
Finding Second Largest num
'''


roll_nums = [45, 34,83, 15, 64, 64,  23, 92, 39]
# print(max(roll_nums))

def second_largest(lst):
    list1 = list(set(lst))  # To remove duplicates
    index_of_ele = list1.index(max(list1))
    list1.pop(index_of_ele)     # Removing largest
    return max(list1)

if __name__ == '__main__':
    print('Second largest element is - %s'%(second_largest(roll_nums)))