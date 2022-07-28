'''
convert a list to a tuple
'''

from _00_Assignments._02_List_Assignments._49_List_to_Dict import colors
print(f'List of colors - {colors}')


def convert_to_tup(l1):
    l1 = tuple(l1)
    return l1


if __name__ == '__main__':
    print(f'Tuple of colors - {convert_to_tup(colors)}')
