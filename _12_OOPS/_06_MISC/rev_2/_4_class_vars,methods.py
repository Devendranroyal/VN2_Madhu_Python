'''
 Class :
    Class Variables +
    Instance Variables +

    Class Methods
    Instance Methods
    Static Method

OOPs:
--------
class object
class   - logical
object  - physical

encapsulation - binding the data members(Fields) and member methods(Methods)

variable - value
parameter - argument

In OOPs:
---------
fields/variables - instance vars   / class vars    / local vars
methods          - instance methods/ class methods / static methods

instance vars - individual copy


'''


# BEFORE
class Employee:  # This approach is wrong
    #1.STATE
    def __init__(self, eid, name, sal, comp_name):
        self.eid = eid
        self.name = name
        self.sal = sal
        self.comp_name = comp_name
    #2.BEHAVIOR
    def get_emp_details(self):
        print("Emp details are :",self.eid,self.name,self.sal,self.comp_name)

madhu = Employee(101,'Madhu Nettem',15000,'ORACLE')
madhu.get_emp_details() # ==> Employee.get_emp_details(madhu)
prakash = Employee(102,'PrakashS',20000,'ORACLE')
prakash.get_emp_details()
kiran = Employee(103,'Kiran Kumar',25000,'ORACLE')
kiran.get_emp_details()

'''
 Disadvantage with above code :
     We are using common/sharable (comp_name) data in __init__ method
    which causes memory wastage.

Solution : Define it as class variable as below
'''
print("---------------With class variables,class Methods---------------")
x = 10

class Employee:
    # class variables
    comp_name = 'ORACLE' # Initialized while class loading
    c_address = "Whitefield,Bangalore"

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    @classmethod
    def get_comp_name(cls):  # class method
        print("Get company name : ", cls.comp_name, cls.c_address)

    def get_emp_details(self):
           print("Emp details are :",self.eid, self.name, self.sal,self.comp_name,self.c_address)

print("Employee class object ",Employee)

Employee.get_comp_name()

madhu = Employee(101,'Madhu Nettem',15000)
madhu.get_emp_details()
print("Employee class object ",madhu)


