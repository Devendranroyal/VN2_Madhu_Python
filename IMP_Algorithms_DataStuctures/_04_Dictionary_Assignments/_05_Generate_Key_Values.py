'''
Generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
'''
from random import choice, randrange


def random_dict(n, l):
    random_dict = {}
    for i in range(0,l):
        element = randrange(n+1)
        random_dict[element] = element* element
    return random_dict


print('New dictionary - ',random_dict(10, 5))