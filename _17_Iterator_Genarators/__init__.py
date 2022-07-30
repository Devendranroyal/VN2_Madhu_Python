'''
EVERYTHING IS AN OBJECT IN PYTHON
'''

'''

Iterator  : Speed of execution
Generator : Memory Management 


Iterator  : Using for loop 
Generator : Generator function    --> 'yield' in function
            Generator Expression  --> Comprehension mechanism
                                          - List comprehension
                                          - Set comprehension
                                          - Dict comprehension

2.X :   range()   : Iterator 
        xrange()  : Generator
        
3.X :   range()   : Generator

'''
print("--------GENERATOR in 3.X-----------")
for i in range(10):
    print(i)

var = print("--------ITERATOR-----------")
list1 = [1, 2, 3, 4, 5, 6]
for each in list1:
    print("Element in list :",each)
print("End of for loop")

# 2  Steps executed when we use sequence in for loop
list1.__iter__() # will be called only once
list1.__next__() # will be called len of seq + 1 times


'''
In for loop :
=================
range(genrator)(3.x)   2.x ==> range(iterator),xrange(generator)  
string Iterator
list   Iterator
tuple  Iterator
byte arrays 
buffers

Iterator  --  When we require faster iteration, irrespective of memory constraints.
Generator --  When memory constraints exists.

Python 2.x
------------
range  - Iterator   -- Memory will be allocated for all 1L values
xrange - Generator  -- Memory will be created for one value at a time
                       0 - Memory X
                       1 - Memory X
                       2 - Momery
    
Python 3.x
------------
range - Generator

'''