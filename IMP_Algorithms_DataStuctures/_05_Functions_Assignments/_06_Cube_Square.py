'''
find cube/square of a number
'''
import math
num = float(input('Enter a num : '))


def sq_cube(n):
    cube = math.pow(n, 3)
    square = math.pow(n, 2)
    # cube = n ** 3
    # square = n ** 2
    print(f'cube of {n} is {cube}')
    print(f'square of {n} is {square}')


if __name__ == '__main__':
    sq_cube(num)