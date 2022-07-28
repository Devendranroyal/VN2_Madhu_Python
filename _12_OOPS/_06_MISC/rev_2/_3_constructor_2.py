#1  . With Default Constructor:
print("----------Default Constructor---------------")
class Employee:

    # Default constructor
    def __init__(self):
        pass

    def get_id(self,eid):
        print("Emp details are  ",eid)

    def get_name(self, ename):
        print("Emp details are  ", ename)

    def get_sal(self, sal):
        print("Emp details are  ", sal)

    def get_emp_details(self,eid,ename,sal):
        print("Employee details are : ",eid,ename,sal)


madhu = Employee()
madhu.get_id(10)
Employee().get_name('Madhu Nettem')
Employee.get_sal(2000)
madhu.get_emp_details(10,'Madhu Nettem',2000)

#1 . With Parameterized Constructor:
print("----------Parameterized Constructor---------------")
class Employee:
    OFFICE_NAME = 'ORACLE'
    # Parameterized constructor
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    #2.BEHAVIOR
    def get_emp_details(self):
        print("Emp details are :",self.id,self.name,self.sal)

madhu = Employee(10,'MadhuNettem',10000)   # sum(10,20)
madhu.get_emp_details()


eid = int(input("Enter id"))
name = int(input("Enter name"))
sal = int(input("Enter Salary"))
madhu = Employee(eid,name,sal)   # sum(x,y)

