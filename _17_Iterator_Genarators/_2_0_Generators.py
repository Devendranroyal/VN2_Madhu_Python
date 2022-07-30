
# https://www.programiz.com/python-programming/generator#:~:text=Python%20generators%20are%20a%20simple,one%20value%20at%20a%20time).
# https://www.programiz.com/python-programming/generator
'''
Python 2.x
--------------
range  - Iterator   -- Speed of execution
xrange - Generator  -- Memory management
    
Python 3.x 
-----------
range  - Generator

What are generators in Python?
 => There is a lot of overhead in building an iterator in Python
    We have to implement a class with __iter__() and __next__() method,
    keep track of internal states,raise StopIteration when there was no values to be returned etc.
    This is both lengthy and counter intuitive.
  
 => Generator comes into rescue in such situations.
 => Python generators are a simple way of creating iterators
     All the overhead we mentioned above are automatically handled by generators in Python.
=> A generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

How to create a generator in Python?

=> It is fairly simple to create a generator in Python. 
=> It is as easy as defining a normal function with yield statement instead of a return statement.

=> If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. 
   Both yield and return will return some value from a function.

=> The difference is that, while a return statement terminates a function entirely, yield statement pauses the function saving all its states and 
   later continues from there on successive calls.
'''
'''
Generators in Python :
=======================
There is a lot of work in building an iterator in Python. 
We have to implement a class with __iter__() and __next__() 
method, keep track of internal states, and raise StopIteration when there are no values to be returned.

This is both lengthy and counter intuitive. Generator comes to the rescue in such situations.

Python generators are a simple way of creating iterators. 
All the work we mentioned above are automatically handled by  generators in Python.

Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over 
(one value at a time).
'''
#Iterator

class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        print(result)

pow = PowTwo(3)
pow.__next__()
pow.__next__()
pow.__next__()

print("-----------Generator Function-------------")

def pow_two_gen(max=0):
    n = 0
    while n < max:  # 0 1 2
        yield 2 ** n  # value will be produced lazily   1 2 4 8 16 32 64 128 256 512
        n += 1

for each in pow_two_gen(3):
    print(each)

print("-----------Generator Function-------------")

def pow_two_gen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
for each in pow_two_gen(3):
    print(each)
    pass
