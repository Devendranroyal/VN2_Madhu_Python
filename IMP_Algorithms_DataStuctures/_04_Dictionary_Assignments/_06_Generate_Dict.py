'''
Print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys
'''
from random import choice, randrange


def random_dict(n, l):
    random_dict = {}
    for i in range(0,l):
        element = randrange(0,n+1)
        random_dict[element] = element* element
    return random_dict


if __name__ == '__main__':
    print('New dictionary - ', random_dict(15, 10))