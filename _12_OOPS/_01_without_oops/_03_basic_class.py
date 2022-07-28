# OOPs concepts
'''
Class Object
-------------------
Encapsulation
Abstraction
Inheritance
Polymorphism
'''
x = 10
print(x, type(x), id(x))


'''
# STATE    - data structures  - Fields
# BEHAVIOR - functions        - Methods

variables, value                 #   x = 10
parameters, arguments            # functions  
fields, methods                  # Inside class 

'''

# Retrieve employee information  with hike 10% in an organization
# emp_data = [{'eid':100,'ename':'Madhu N','sal':10000},.......]
# Without oops concepts
  # 1. Retrieve the emp data - RETRIEVAL/READ

print("-----Without oops concepts--------")
    # STATE
emp_id = 100
emp_name = 'Madhu Nettem'
e_sal = 10000
    # BEHAVIOR
def get_edata(eid, name, sal):
    sal = sal + sal*10/100
    print("Employee after Hike :", eid, " - ", name, " - ", sal)

get_edata(emp_id, emp_name, e_sal)

'''
variables - fields
functions - methods

'''
print("-----With oops concepts--------")
# class definition
class Employee:
    # STATE   # fields
    def __init__(self, eid, ename, sal):  # parameters
        self.eid = eid      # RHS --> Local variables eid,name,sal
        self.ename = ename  # LHS --> Instance variables *  self.eid, self.ename,self.sal
        self.sal = sal      # self -> instance/object/reference variable

    # BEHAVIOR  # methods
    def update_sal(self, rating):
        print("Employee info during joining :", self.eid, " - ", self.ename, " - ", self.sal)
        if rating >= 3:
            self.sal = self.sal + self.sal*30/100
        elif rating >= 2:
            self.sal = self.sal + self.sal * 20 / 100
        else:
            self.sal = self.sal + self.sal * 10 / 100
        print("Employee info after 1 year  :", self.eid, " - ", self.sal)


# object creation

madhu = Employee(100, 'Madhu Nettem', 10000)  # madhu - object*/reference/instance  RHS - Object creation
madhu.update_sal(3)
e_data = [[100, 3], [101, 2], [102, 5]]
for emp in e_data:
    pass
'''
UI ---->   Python  ----> DATABASE

# DATABASE 1L
data = 'select * from employee'
data = [{'eid':101,'name':'xyz','sal':2000,'rating':4},{},{}]
for record in data:
    emp = Employee(record['eid'], record['ename'],record['sal'])
    emp.update_sal(record['rating'])
    # SAVE to database 
'''
abhiram = Employee(101, 'Abhiram Naren,', 15000)
abhiram.update_sal(2)

'''
        x = 10   # int(10) float(10.4)   bool(True)    str("Hello")
  varible = value     
parameter = argument    
object    = object creation
/instance/
ref. variable  

'''
kiran = Employee(104, 'Kiran Kumar', 15000)
kiran.update_sal(5)

prakash = Employee(106, 'Prakash Kumar', 20000)
prakash.update_sal()

# declaration     - int x
# initialization  - int x = 10

list1 = list([1, 2, 3])

# list1 is an object of type list class(builtins.py)
# madhu is an object of type Employee class


print("-----------Student class-----------------")
class Student:
    # STATE
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks

    # BEHAVIOR
    def get_student_details(self):
        print("Student details : ", self.sid, self.name, self.marks)

s_id = int(input("Enter student id : "))
sname = input("Enter student name : ")
smarks = int(input("Enter student marks : "))

dilip = Student(s_id, sname, smarks)
dilip.get_student_details()

venkat = Student(55, 'Venkata', 90)
venkat.get_student_details()

print("Venkat object :", venkat, id(venkat), type(venkat))
# 10 int 10.5 float "hello" string

# class   n no of objects

print(dilip)
print(venkat)