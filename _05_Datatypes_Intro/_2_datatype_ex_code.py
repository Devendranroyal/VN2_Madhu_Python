''''''
'''
Datatypes/Structures: STATE
Functions           : BEHAVIOR

Functions:
-----------
print()
type()  id()
int()   float() complex() bool()
'''
# float x = 10+20-30/54*23
x = 10+20-30/54*23
print("Value of x: ", x)
print("Type of x : ", type(x))
print("Address of x: ", id(x))

print("-----------------------")
sal = 10000.32
print("Value of sal: ", sal)
print("Type of sal : ", type(sal))
print("Address of sal: ", id(sal))

print("------------------------")
is_active = True
print("Status of active : ", is_active)
print("Type of active : ", type(is_active))
print("Address of active : ", id(is_active))
print("------------------------")

print("---------Type of values----------")

# Type conversions int() float() complex() bool()

# float to int
print("====float to int======")

x = 100.42
print("Value of x: ", x, type(x))

# Convert above number to integer
x = int(x)  # Here python creates new value 100
print("Value of x: ", x, type(x))

print("====int to float======")
# int to float
x = 10
print("Value of x: ", x, type(x))
x = float(x)
print("Value of x: ", x, type(x))

# convert bool and viceversa
print("====bool to int and viceversa======")
# Boolean
'''
True   - True
         non 0
         not None
         
False  - False
         0
         None
'''
x = 100
print("Value of x: ", x, type(x))
x = bool(x)
print("Value of x: ", x, type(x))


x = 0
print("Value of x: ", x, type(x))
x = bool(x)
print("Value of x: ", x, type(x))


# None    not None

x = 'hello'  # not None
x = bool(x)
print("hello -->", x, type(x))

x = ''   # None
x = bool(x)
print("Empty str --> ", x, type(x))

x = [] # list
x = () # tuple
x = {} # dicitonary
x = set({}) # set