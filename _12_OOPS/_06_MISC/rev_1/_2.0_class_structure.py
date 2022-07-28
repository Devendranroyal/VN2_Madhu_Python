
print("------------Using functions static data---------------------")
# STATE
empid = 101
ename = 'Madhu N'
salary = 10000

# BEHAVIOR
def get_edata(eid,name,sal):
    print("Employee details are : ")
    print(eid, " ", name, " ", sal)

get_edata(empid,ename,salary)


print("------------Using functions dynamic data---------------------")
# STATE
empid = 10 # input("Enter emp id : ")
ename = 'Madhu' #input("Enter emp name : ")
salary = 10000 #input("Enter emp salary : ")

# BEHAVIOR
def get_edata(eid,name,sal):
    print("Employee details are : ")
    print(eid," ",name," ",sal)

get_edata(empid,ename,salary)


print("------------Using OOPs---------------------")

class Employee:
    '''
    empid = 101
    ename = 'Madhu N'
    salary = 10000

    empid = input("Enter emp id : ")
    ename = input("Enter emp name : ")
    salary = input("Enter emp salary : ")
    '''
    # STATE
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal
    '''
    def get_edata(eid,name,sal):
        print("Employee details are : ")
        print(eid," ",name," ",sal)
    '''
    # BEHAVIOR
    def get_edata(self):
        print("Employee details are : ")
        print(self.eid, " ", self.name, " ", self.sal)

# Defining a Class
class Employee:
    # STATE   : fields(parameters)
    def __init__(self, eid, name, sal):
        self.eid = eid  # instance variables / local variables
        self.name = name
        self.sal = sal
    # BEHAVIOR method(function)
    def get_edata(self):
        print("Employee details are : ")
        print(self.eid, " ", self.name, " ", self.sal)

# Object/Instance/Reference variable creation
madhu = Employee(101,'Madhu Nettem',10000)  # State initialization
madhu.get_edata()

x = 10

class Student:
    # STATE
    def __init__(self,sid, sname, marks):
        self.sid = sid
        self.sname = sname
        self.marks = marks

    # BEHAVIOR
    def get_sdetails(self):
        print("Student details are : ")
        print(self.sid," ",self.sname," ",self.marks)

prakash = Student(10,'Prakash',10)   # x = Student(10,'Prakash',10)
prakash.get_sdetails()               # x.get_datails()

Student(10,'Prakash',10).get_sdetails()

x = 10  # State
print(x) # Behavior
print("--------------")
print(10)




