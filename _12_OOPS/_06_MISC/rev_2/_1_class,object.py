'''
# Store emp details and display his details

CRUD    Datatype                State              Behavior
-----------------------------------------------------------------------
CR      int str float           eid ename sal      display_emp_details()
'''

# 3 With Functions
print("--------------With Functions-------------------")

#STATE
empid = 100           # int(input("Enter employee id : "))
name = 'Madhu Nettem'
salary = 25000

# BEHAVIOR
def emp_details(eid,ename,sal):
    sal = sal + sal*10/100
    print("The emp details are  :",eid,ename,sal)

emp_details(empid,name,salary)

# 4 With OOPs
print("--------------With OOPs      -------------------")
class Employee:

    # STATE
    def __init__(self, eid, name, sal):
        self.eid = eid                    # Fields/Instance variables
        self.name = name                  # State initialization
        self.sal = sal

    # BEHAVIOR
    def emp_details(self):
        self.sal = self.sal + self.sal * 10 / 100
        print("The emp details are  :", self.eid, self.name, self.sal)

x = 10             # variable value
# details(x)       # argument
# def details(x,y):  parameters
# madhu ==>          object
madhu = Employee(100,'Madhu Nettem',25000) # Object creation   ==> Equals to 13,14,15 lines

madhu.emp_details()   # ==> Employee.emp_details(madhu)






