'''
Multiply all the items in a dictionary
'''
dict2 = {6: 36, 2: 4, 3: 9, 1: 1, 4: 16}


def prod(d):
    prod = 1
    for i, j in d.items():
        prod *= (i * j)
    return prod


if __name__ == '__main__':
    print('Product of items - ',prod(dict2))