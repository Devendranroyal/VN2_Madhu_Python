'''
Count the number of elements within the range
'''

list_of_nums = [45, 23, 48,34, 98, 34, 82, 82, 34, 67]


def ele_in_range(lst, min, max):
    count = 0
    for i in lst:
        if min < i < max:
            count += 1
    return count

if __name__ == '__main__':
    print(f'No of elements within the range = {ele_in_range(list_of_nums, 25 ,90)}')