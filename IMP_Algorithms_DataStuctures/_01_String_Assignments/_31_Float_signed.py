'''
31. print the following floating numbers upto 2 decimal places with a sign
'''

num1 = float(input('Enter num1 : '))
num2 = float(input('Enter num2 : '))


def num_format(num):
    print('Actual num : ', num)
    print('After formatting : ' + '{:.2f}'.format(num))


num_format(num1)
num_format(num2)
print('-------------------------------------------------------')

num3 = float(input('Enter a num3 :'))

print('using round() for num3 : ', round(num3, 2))
print('After formatting : %.2f' %num3)


