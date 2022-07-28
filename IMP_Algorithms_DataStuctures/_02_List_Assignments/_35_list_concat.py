'''
Create a list by concatenating a given list which range goes from 1 to n
'''

l1 = ['r', 't', 'g', 's', 'u']
n = 4


def concat_lis(lst, num):
    new_list = ['{}{}'.format(x, y) for y in range(1, num + 1) for x in lst]
    return new_list


print(concat_lis(l1, n))