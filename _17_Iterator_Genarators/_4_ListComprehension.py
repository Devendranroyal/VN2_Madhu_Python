'''
Generator Function -> yield
Generator expression -> comprehension
                        List/Set/Dict comprehension
'''


#  https://www.programiz.com/python-programming/list-comprehension
'''
List Comprehension :
-------------------
 => List comprehension provide a concise way to create lists
 
'''
'''
For loop vs List Comprehension :

REQ : Separate the letters of the word human and add the letters as items of a list.
'''
# Example 1: Iterating through a string Using for Loop

# Normal for loop

h_letters = []                       # 1. CREATE A EMPTY LIST
for letter in 'PYTHON':              # 2. ITERATE THROUGH SEQUENCE
    h_letters.append(letter)         # 3. APPENDING EACH ELEMENT INTO LIST

print("--Using for loop----------------", h_letters)

# List comprehension
h_letters = [letter for letter in 'PYTHON']
print("--Using LIST COMPREHENSION------", h_letters)

vals = [x**x for x in range(1, 11)]
print("--Using LIST COMPREHENSION------", vals)

vals = []
for x in range(10):
    vals.append(x*x)
print("--Using For Loop          ------", vals)

# Print even numbers between 1 to 100
print("-----Even numbers------")
ev_nos = [val for val in range(1, 101) if val % 2 == 0]
print("Even nos : ", ev_nos)
'''
data = [<expr> for variable in sequence]
1. Python will create empty list 
2. It will iterate through sequence('PYTHON') and 
   retrieves one by one element and gives to expression
3. Expression will be executed and appended to empty list 
'''

# Example 2: Iterating through a string Using List Comprehension
# REQ: Print list of even numbers between 0 to 30
print("-------------------Range func in list comprehension----------")
# Iterator
ev_nums = []
for i in range(30):
    if i % 2 == 0:
        ev_nums.append(i)
print("Range with for loop   :", ev_nums)
# List comprehension
ev_nums = [i for i in range(30) if i % 2 == 0]

print('Range with list compr :', ev_nums)

#Iterator

numbers = []
for i in range(100):
    if i%2 == 0:
        if i%5 == 0:
            numbers.append(i*i)
print("Range with for loop   :", numbers)

numbers = [i*i for i in range(100) if i%2 == 0 if i%5 == 0]
print("Range with list compr :", numbers)


print("-----List comprehension to for loop-----------")

numbers = [i*i for i in range(100) if i % 2 == 0 if i % 5 == 0]
print("List comprehension : ", numbers)

numbers = []
for i in range(100):
    if i % 2 == 0:
        if i % 5 == 0:
            numbers.append(i*i)
print("Normal for loop    : ", numbers)

'''
Syntax of List Comprehension :   [expression for item in sequence <conditions>]

                             Ex: [ letter for letter in 'human' ]
                             
List comprehension  can identify when it receives a string or a tuple and 
work on it like a list.
'''

# Using if with List Comprehension :
print("=========IF with List Comprehension==============")
number_list = [x for x in range(20) if x % 2 == 1]

number_list = []
for x in range(20):
    if x % 2 == 1:
        number_list.append(x)


# Nested IF with List Comprehension
print("=========Nested IF with List Comprehension==============")
num_list = [y**2 for y in range(100) if y % 2 == 0 if y % 5 == 0]
print("Using comprehension : " , num_list)

print("-------------OR--------------")
number_list = []
for y in range(100):
    if y % 2 == 0:
        if y % 5 == 0:
            number_list.append(y**2)
print("Using for loop      : ", number_list)

# if...else With List Comprehension
print("========= if...else  with List Comprehension==============")

obj = []
for i in range(10):
    if i % 2 == 0:
        obj.append("Even")
    else:
        obj.append("Odd")
print(obj)

print("-------------OR--------------")

obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(obj)

list1 = []
for i in range(10):
    if i % 2 == 0:
        list1.append("Even")
    else:
        list1.append("Odd")
print(list1)


        


print("----List comprehension with expression------------")

list1 = [3, 4, 5]
multiplied = [item*5 for item in list1] 
print(multiplied)


square = [item*item for item in list1] 
print(square)
'''
Key Points :
============
List comprehension is an elegant way to define and create lists based on existing lists.
List comprehension is generally more compact and faster than normal functions and loops for creating list.
However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
Every List comprehension can be rewritten in for loop but viceversa is not true
 '''
