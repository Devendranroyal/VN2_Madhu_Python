
'''
#1 one time usage
print(10)

# 2 or more places
x = 10
print(x)         XXX ---> print(10)
print(x+100)     XXX ---> print(10+100)
'''


def sum1(num1, num2):
    res = num1 + num2
    return res

sum1(10 ,20) # No use

# 1 one time usage
print("Sum is : ", sum1(10, 20))

# 2 two or more places
output = sum1(10, 20)
print("First usage: ", output)
print("Second usage: ", output)

def sum2(num1, num2):
    res = num1 + num2
    print("Addition is : ", res)

sum2(10 ,20)   # Direct function call
n1 = 10
n2 = 20
sum2(n1, n2)


# IF function has return type
# 1  Single time
print("Type 1 :", sum1(10, 20))  # print(10)
print("Type 1 :", sum1(10, 20) + 100)

# 2 Mulitple times
output = sum1(10, 20)
print(output)   # x = 10 print(x)
print(output + 100)
print(output + 200)



# IF function has no return type
sum2(10, 20)                # We are not expecting function return type

print("------------------Function details------------------  ")

def getdata():
    print("I am in getdata")
    return 100

print("Function call  : ", getdata())
print("Function name**: ", getdata)
print("Function type  : ", type(getdata))
print("Function name  : ", id(getdata))




class Employee:
    pass
print("Class details  ")

print("----Name :", Employee)
print("----Type :", type(Employee))
print("----Type :", id(Employee))

# Concept : We can pass "function name" as an argument to any other function

print("---------Variable concept------")
x = 10
print(x, type(x))   # x.__str__()

x = 10
y = 20
print("Sum function call ", sum1(x, y))  # sum1(x, foo(10))
print("Sum function def  ", sum1)

# https://realpython.com/primer-on-python-decorators/

'''
Functions:
============
1. First Class functions
2. Nested Functions
3. Returning Functions
'''
print("----------Function calls------------------")

def foo(bar):
    # print("Output is :", bar + 1)
    return bar + 1
# 1
foo(10) # if print statement is there inside function
# 2
print(foo(10))  # if return stmt exists
# 3
x = foo(10)   # if return stmnt exits and output is being used in 2 or more places
print(x)

print("Sum result1 : ", sum1(10, 20))
print("Sum result2 : ", sum1(10, foo(19)))


print("Comparison :", foo(20) > 3+ 10)  # functions return a value based on the given arguments.
print("----------Function calls------------------")

'''
                Steps execution 174 line:
                1. foo(20) - function call   will get response         ==> 21   
                2. 3+10    - perform arithmetic ops. and give result   ==> 13
                3. compare function response with arithm ops result   ==> 21 > 13  => True
                4. Give result to print function

                print("Comparison ", 10)      # 0
                print("Comparison ", 10+20)   # 1
                print("Comparison ", 10+20 == 30)   # 2
                print("Comparison ", 10+20 == 10+30)   # 3
                print("Comparison ", foo(10+20) == 10+30)   # 4
'''


def foo2(bar):
    return bar + 1


foo2(2)
print(foo2(3))
print(type(foo2))
print(foo2)

print("---Function calling Chain-----")


def x():
    print("x function")
    print(10 / 0)


def y():
    print("y function")
    x()


def z():
    print("z function")
    y()


z()

# 1. FIRST CLASS FUNCTIONS:
print("============1. FIRST CLASS FUNCTIONS=============")

'''
Here foo_func requires function name why because we have used 
the same parameter during function call

X                Y                       Z        
Animisha   <--   Kritika             <--  Tejaswini                 
            10K
          --->                     --> 

foo(bar)           medium(f_name, var)  <==    get_data()
   return bar+1      out = f_name(var)                  functionname -   foo  
                     return out                         args         -   10 
                                                 resp = medium(foo, 10)
                                                 # business logic    

'''

print(" *** Without first class function  ***")


# foo - Animisha
# get_data - Tejaswini

def foo(bar):  # Animisha
    return bar + 1


def get_data():  # Tejaswini
    res = foo(100)  # We are calling other function from our function
    print("Val from foo is : ", res)


get_data()

print(" *** With first class function  ***")


def foo(bar):  # Animisha
    return bar + 1


def mediator(foo_func, val):  # Kritika
    output = foo_func(val)  # foo(100)
    return output


def get_daata():  # Tejaswini
    res = mediator(foo, 100)
    print("Val from foo is : ", res)


get_daata()

print("------------------------------------")
