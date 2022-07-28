#https://julien.danjou.info/blog/2016/python-exceptions-guide

'''
Exception handling:
try
except  - same level,super level
        - multiple except blocks /single except block(e1,e2,e3)
        - Exception
else
finally
'''




'''




TypeError         : can only concatenate str (not "int") to str
TypeError         : __init__() missing 1 required positional argument: 'name'
TypeError         : __init__() takes 3 positional arguments but 4 were given
ZeroDivisionError : division by zero

OS : windows/linux

UI           P.L        D.B
--------------------------------------
html         Python     Oracle
js           Java       MySQL
jq           .Net       Postgresql
aj
node
angular

'''

'''
x = 10
ZeroDivisionError zde = ZeroDivisionError("division by zero")
Employee madhu = Employee(100,'Madhu',10000)
'''

#print(x/y)
'''
1. Open file, DB Connection
2, Write data into file/Read data from File
3. Exception occured


Success : try finally
Failure : try except finally
'''


'''
print(10)

x = 10
print(x)

try     : python code which causes exception
except  : exception handling mechanism
finally : closing operations

madhu = Employee(10,"Madhu",123213)
Employee madhu = Employee(10,"Madhu",123213)
ae    = ZeroDivisionError("Division by Zero")

try:
    x = int(input("Enter value of x: "))
    y = int(input("Enter value of y: "))
    print("----- :: try ::Before exception----------")
    print("Division is :", x/y)
    try:
        pass
    except:
        pass
    finally:
        pass
    print("----- :: try ::After exception----------")
except ZeroDivisionError as zde:
    print(" :: except :: Please enter y value other than Zero :: ===> ",zde)
else:
    print("-------------ELSE BLOCK EXECUTED---------")
finally:
    print(" :: finally :: Closing connections, file operations")

print("---------------------")
def sum(a,b):
    return a+b

result = sum(10,20)
print("Result is :",result)



class Employee:
    def __init__(self,id,name):
        print("Object created")
    
madhu = Employee(10,"Madhu")


    
list1 = [1,2,3]
print(list1[5])

try     : The code which causes exception/error
except  : handles the exception
finally : closing operations

try:
    1
    2
    3
    4
    5
except:
    1
    2
    3
finally:
    1
    2
    3
    

Sc1 : if exception occurs at line 2 in try block,
            -Python stops executing remaining statements
            -Goes to except block,executes except block
            -And executes finally block

Sc2 : if no exception in try block,
            -Python executes all statements in try block
            And executes finally block
'''




