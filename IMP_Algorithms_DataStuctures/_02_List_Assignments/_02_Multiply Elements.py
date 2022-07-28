'''
find the product of all the list elements
input : list
'''
list1 = [45,67,23,67,23,56,32]
product = 1
for i in list1:
    product *= i
print('list1 = ', list1)
print('Product of all List elements = ', product)