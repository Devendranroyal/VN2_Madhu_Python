x = 10

# Data types  "[1,2,3,4]"
x = int(input("Enter number:"))  # 10 --> '10'  --> int('10') --> 10
print(x, type(x))

x = input("Enter name : ")
print("Name is : ", x, type(x))

x = 10   # integer
x = 10.5  # float
x = True   # boolean
msg = 'Hello World'  # string
# char c = 'A' in other languages
# Data structures

msg = 'Hello World'         # string  # 'c' "Madhu"
list1 = [12, 23, 30, 443, 53]     # list  [43,23,564,32]  [10,10.4,True,'M','Madhu'] [[1,2],[3,4]]
tup1 = (1, 2, 3, 4, 5)      # tuple
dict1 = {1: 1, 2: 2, 3: 3}  # dictionary {'eid':100,'name':'MadhuN','sal':10000}  datatypes+str+tuple
set1 = {1, 2, 3, 4, 5, 6}   # set

# while
i = 1
while i <= 10:
    print(i)
    i += 1
print("---Outside loop---")



# for loop
'''
    collection of elements
    Sequence        
    
# Maths  :  collection of elements   : matrix             sequence   set       
# Python :  data structures          : string list tuple  range      dict set  
                                       <bytearrays, buffers>
SYNTAX:
--------
for <var> in <sequence>:
    # perform business logic
'''
print("--------For loop with String-------")
# REQ: Print each character of string
course = "PYTHON-PROGRAMMING-LANGUAGE"
         #0123456789..................

for char in course:  # char = 'P'
    print(char.lower())

print("----------End-----------------------")

print(10)  # SINGLE USAGE

x = 10
print(x)  # MULTIPLE TIMES USAGE



# SINGE TIME USAGE
# -------------------------
for element in 'Python World':
    print("Character : ", element)

# MULTIPLE TIME USAGE
# -------------------------
msg = 'Python world'
for element in msg:
    print("Character : ", element)

# further business logic
print("data is : ", msg)

# String with for loop
for char in 'Welcome to Python':
    print("Char : ", char)

for char in 'aflkdsfdsalfsdf  324324SDFDSF@!#@!$#@%fsdfsd dsfdsFDSf!@#@!#!@':
    print("Char : ", char)


print("----FOR LOOP WITH LIST-------------")
# List with for loop
for val in [1, 2, 3, 4, 5, 6, 7]:
    print("List data :", val)

list1 = [1, 2.5, True, 'Madhu', [1,2,3], 5.0, False, 7]
     #  0    1    2      3        4       5    6     7
for val in list1:
    print("List data :", val)

print("Further usage : ", list1)

print("----FOR LOOP WITH TUPLE-------------")
# Tuple with for loop
for val in (1, 2, 3, 4, 5, 6, 7):
    print("Tuple data :", val)
print("----------------------------")

print("----FOR LOOP WITH DICTIONARY-------------")

# Dictionary with for loops
e_data = {'eid': 100, 'name': 'Madhu Nettem', 'sal': 10000}

for key, val in e_data.items():  # [('eid',100), ('name','Madhu Nettem'), ('sal',10000)]
    print("Dict data :", key, val)
print("--------------------------------")

for x in e_data.keys():     # ['eid', 'name', 'sal']
    print("Dict key :", x)
print("--------------------------------")

for val in e_data.values():   # [100, 'Madhu Nettem', 10000]
    print("Dict val :", val)

print("--------------FOR LOOP WITH SET---------------------")
# set with for loop
set1 = {1, 2, 3, 4, 5, 6}
for val in set1:
    print("Set value : ", val)

# Decimal number   0 to 255 1 byte
'''
 ASCII TABLE   
    -----------------------
    -----------------------
    7  6  5  4  3  2  1  0

0 to 255 -  ASCII TABLE    A 65  a 97
367  ---     10000001 
'''