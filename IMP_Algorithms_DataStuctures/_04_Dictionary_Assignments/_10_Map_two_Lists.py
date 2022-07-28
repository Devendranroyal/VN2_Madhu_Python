'''
Map two lists into a dictionary
'''
li1 = [24, 4, 93, 9, 63, 3, 2]
li2 = ['abcd', 'def', 'cat', 'sat', 'lambo', 'yel', 'con']
li3 = [34, 84, 45, 82, 22]


def map_to_dict(l1, l2):
    new_dict = {}
    if len(l1) == len(l2):
        for i in range(len(l1)):
            new_dict[l1[i]] = l2[i]
        return new_dict
    else:
        return 'Cannot be mapped , length of lists is not same'


if __name__ == '__main__':
    print('dict of li1 and li2 mapped - ', map_to_dict(li1, li2))
    print('dict of li1 and li3 mapped - ', map_to_dict(li1, li3))