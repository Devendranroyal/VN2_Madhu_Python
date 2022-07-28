'''
32.print the following floating numbers with no decimal places
'''
num1 = float(input('Enter num1 : '))
num2 = float(input('Enter num2 : '))


def only_decimal(num):
    print('Actual num before formmating:', num)
    print("Method 1 : {:.0f}".format(num))
    print('Method 2 : %.0f' % num)
    print('Method 3 using round() : ',round(num))


only_decimal(num1)
only_decimal(num2)