
'''
Generator expressions :
 - are a high-performance, memory–efficient generalization of list comprehensions and generators
 # https://dbader.org/blog/python-generator-expressions
 # https://www.geeksforgeeks.org/generator-expressions/

'''
# Generator
class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

rep = Repeater(10)
rep.__iter__()
rep.__next__()

def repeater(value):
    while True:
        yield value
print(repeater(10).__next__())