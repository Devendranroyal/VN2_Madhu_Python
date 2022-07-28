'''
35. to display a number with a comma separator
'''
# var1 = 50000000
var1 = int(input('Enter a number :'))
var2 = int(input('Enter a number :'))


def separator(num):
    print('Before formatting : %d'%num)
    print('Formatted num : '+'{:,}'.format(num))


print()
separator(var1)
print()
separator(var2)

