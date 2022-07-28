'''
Sum all the items in a dictionary
'''
dict2 = {6: 36, 2: 4, 3: 9, 8: 64, 13: 169, 1: 1, 11: 121, 4: 16}


def sum1(d):
    sum = 0
    for i, j  in d.items():
        sum += (i + j)
    return sum


if __name__ == '__main__':
    print('Sum of items - ',sum1(dict2))