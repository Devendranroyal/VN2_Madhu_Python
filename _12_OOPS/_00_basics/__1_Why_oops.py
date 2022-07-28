
'''
Object Oriented Programming System
'''

'''
Class/Object
------------------
Encapsulation
Abstraction
Inheritance
Polymorphism
'''

# REQUIREMENT : Find sum of  given two numbers

# STATE :   -  Data Initialization  ==> Data types/data structures
n1 = 10  # int(input("Enter number1"))
n2 = 20  # int(input("Enter number2"))

# BEHAVIOR   - Implementation       ==>  Functions
def get_sum(num1, num2):
    result = num1 + num2
    return result



def get_sum():
    n1 = int(input("Enter nno1"))
    n2 = int(input("Enter nno2"))
    return n1+n2

print("Sumn: ",get_sum())

str = 'hello' # str("hello")
str.split()
'''
Employee  / GMAIL ACCOUNT (SIGNUP/LOGIN/UPDATE/DELETE ACC)
CRUD operations:
-----------------
    - CREATE EMPLOYEE
    - RETRIEVE EMP DETAILS SINGLE/PARTIAL/ALL
    - UPDATE EMP DETAILS   SINGLE/PARTIAL/ALL
    - DELETE EMP DETAILS   SINGLE/PARTIAL/ALL
    
'''

# print("Sum of 2 numbers is : ", get_sum(n1, n2))


'''if elif else 
   for while 
   functions 
   class 
   try except else finally 
   with
'''

'''
Why OOPs
 - Security for STATE
 - Grouping Behavior 
'''


# class structure
'''
class <class-name>:
    # STATE
    # BEHAVIOR

class Addition:
    #1. STATE
    n1 = 10
    n2 = 20
    
    #2. BEHAVIOR
    def get_sum(num1, num2):
        result = num1 + num2
        return result
'''

# REQ : Display each employee information   CRUD -> RETRIEVAL
'''
1. CRUD 
2. STATE  (Data type/structures)
3. BEHAVIOR
'''
# A1 :: Using Functions
print("---------Using Functions-----------")
'''
Disadvantages:
    1. Security for data
    2. Grouping of behavior
'''
    # 1. STATE
empid = 100  # int(input("Enter empid :"))
name = 'Madhu Nettem'  # input("Enter name : ")
sal = 15000  # float(input("Enter sal :"))

    # 2. BEHAVIOR
def get_einfo(eid, ename, esal):
    print("Employee details are ", eid, ename, esal)

get_einfo(empid, name, sal)

'''
Direct initialization : int x = 10;

int x;  # Declaration
x = 10  # Initialization

'''

# Using OOPs  -- Class
# Step 1:
class Employee:
    # 1. STATE
    empid = 100  # int(input("Enter empid :"))
    name = 'Madhu Nettem'  # input("Enter name : ")
    sal = 15000  # int(input("Enter sal :"))

    # 2. BEHAVIOR
    def get_einfo(eid, ename, esal):
        print("Employee details are ", eid, ename, esal)

print("---------Using OOPs-----------")


# Step 2:
class Employee:
    # 1. STATE  # Declaration
    def __init__(self, empid, name, sal):
        self.empid = empid
        self.name = name
        self.sal = sal

    # 2. BEHAVIOR  ---> Method
    def get_einfo(self):
        print("Self : ", self)
        print("Employee details are ", self.empid, self.name, self.sal)

# UI ---> Python ---> Database
# object creation
x = 10
madhu = Employee(100, 'Madhu Nettem', 15000)  # Initialization
print("Madhu : ", madhu)
madhu.get_einfo()

# objection creation
x = int(10)  # int(10)
list1 = list([1, 2, 3])   # [1,2,3]  [] list()
list1.append(100)
print("Type of list1: ", type(list1))
name = 'Hello'  # str("Hello")


print("--------------Student example in OOPs--------------")

class Student:
    # 1. STATE
    def __init__(self, r_no, name, marks):
        self.r_no = r_no
        self.name = name
        self.marks = marks
    # 2. BEHAVIOR
    def get_sinfo(self):
        print("Student details are ", self.r_no, self.name, self.marks)

jai = Student(23, 'Jaipal C.G.', 65)
jai.get_sinfo()

print("--------------TELEVISION example in OOPs--------------")

class Television:
    # STATE
    def __init__(self, tid, name, price, color):
        self.tid = tid
        self.name = name
        self.price = price
        self.color = color

    # BEHAVIOR
    def get_telinfo(self):
        print("Television info : ", self.name, self.price, self.color)

samsung = Television('L0001', 'Samsung', 25400, 'Black')
samsung.get_telinfo()


# 50 different class examples
