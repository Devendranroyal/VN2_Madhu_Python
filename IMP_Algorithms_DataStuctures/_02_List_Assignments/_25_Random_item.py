'''
Select a random item from the list
'''
import random

flowers = ['rose', 'jasmin', 'crysanthamum', 'lillies', 'dafodils', 'marigold']


def random_element(lst):
    return random.choice(flowers)

print('Random element returned is - {} '.format(random_element(flowers)))
