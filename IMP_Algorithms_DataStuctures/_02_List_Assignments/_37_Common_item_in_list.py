'''
Finding common elements in two list
conver them to sets and find their union
'''

colors1 = ['Blue', 'Black', 'Pink', 'White', 'Indigo']
colors2 = ['Red', 'Blue', 'Indigo', 'Yellow', 'Pink']

def common_ele(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    common = list(s1 & s2)
    return common

print(common_ele(colors1, colors2))