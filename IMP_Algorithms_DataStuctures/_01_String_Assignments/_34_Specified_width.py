'''
34. print the following integers with '*' on the right of specified width

{:0>6d} - if the symbol is '>', * is padded on left to make its width 6
{:0<7d} - if the symbol is '<', * is padded on right to make its width 7

Note - they can be padded with any character like $, # etc
'''
num1 = int(input('Enter num1 : '))
num2 = int(input('Enter num2 : '))


def padding_nums(num):
    print("Actual num : %d"%num)
    print('padding for width 6 :','{:*>6d}'.format(num))
    print('padding for width 8 :','{:*>8d}'.format(num))


padding_nums(num1)
padding_nums(num2)