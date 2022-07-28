'''
variable

write opertaion  x = 10, x =True, x = "name"

Read operation print(x), id(x), type(x)

one value can assign to multiple variables x =y =z = 10
1. value
2. type
3. reference

single variable cannot assign to multiple values at a time, it is possible only in list, tuple, set dictionary

x = 10 = 20 = 30
x = 20 when i assign a new value the existing reference will be removed and assign with new reference.

when the reference count is 0 , that value will be moved to garbage collection.

After use del(x) , reference will be removed and moved to garbage collection.

local variable- use single time created inside function

global variable- use multiple times created inside/outside of function ( Global)

#   Implicit casting:
Implicit type casting means conversion of data types without losing its original meaning.
This type of typecasting is essential when you want to change data types without changing
the significance of the values stored inside the variable



Explicit conversion or cast is a process of passing information to the compiler that the program
is trying to perform conversion with the knowledge of possible data loss.

For Example, if we are converting a higher numeric value into a lower one
int(10) to float(10)
float(10.5) to int(10)



Data type	Storage size
Byte	    1 byte
Boolean	    2 bytes	True or False
Integer	    4 bytes
float -     8 bytes
'''


x = 10  # 4 bits
y = float(x) # 8 bits
print(type(x), type(y), x, y)
#  <class 'int'> <class 'float'> 10 10.0


# Explicit casting:
a = 10.5
b = int(a)
print(type(a), type(b), a, b)
# <class 'float'> <class 'int'> 10.5 10


# integer
print("==========")
x = 100  # write opertaion
print(x)
print(id(x))
print(type(x)) # Read operation

# float

a = 124.55
print(a, type(a))

# boolean

y = True
z = False

print(id(y), id(z))

# string

name = "shyam123566"
print(type(name), id(name))


# collections - To store group of individual values
# list, tuple-(), set{}, dictionary{key:value}
#List -[]
x = [1, 2, 10.5, True, "string"]
print(x, type(x), id(x))
print(id(x[1]))

x = 11   # write
print(x) # read


x =y =z = 10  # possible
print(id(x), id(y), id(z))

x = 100
x = 200
x = 300
print(x)