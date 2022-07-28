# Everything is an object in Python

# string list tuple dictionary set
age = 10
age = int(10)  # int --> class,   10 --> argument
print("Age : ", age)
'''
age = int(10)                        object creation   
      Employee(100,'Madhun',15000)
'''
age = int(10)  # int() float() long() str() list() tuple() dict() set()
print(age)
print(id(age), type(age))

li = [1, 2, 3]  # list([1,2,3])
print("List : ", li)   # Content
li = list([1, 2, 3])


# li.xyz()


msg = 'Hello World'  # str('Hello World')
msg = str('Hello World')


'''
madhu = Employee(100, 'MadhuN')
li = list( [1,2,3] )
list    -  classname -> builtins.py module 
[1,2,3] -  argument 
li      -  object**/ instance*/ ref. variable 
'''


# madhu = Employee(100,'MadhuN',1000) ==> object creation

print(li, id(li), type(li))

print(type(10.5), type(True), type('Hello'), type((1, 2, 3)))

print(li)  # list1.__repr__()   str() vs repr()

dict1 = {1: 1, 2: 2}
dict1.keys()

