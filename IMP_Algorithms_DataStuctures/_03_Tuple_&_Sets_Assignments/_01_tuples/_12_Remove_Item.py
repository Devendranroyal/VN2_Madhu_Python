'''
Remove item from tuple
'''

colors = ('Red', 'White', 'Mixed', 'White', 'Pink', 'yellow')
name = 'Mixed'


def rem_item(tup, item):
    # Convert to list
    li = list(tup)
    if item in li:
        li.remove(item)
        return tuple(li)
    else :
        return 'Element not found in tuple'


if __name__ == '__main__':
    print('After removing item - {}'.format(rem_item(colors, name)))
    print('After removing item - {}'.format(rem_item(colors, 'yel')))
