'''
Class variable     : Will be initialized when class is loaded by interpreter
                    and memory allocation will be done at the loading itself
Instance variable : When we create an object for class,these will get initialized
'''


# Different ways of creating class

# 1. only class vars,  class methods

class Employee:
    office = 'ORACLE'
    def __init__(self,eid):
        self.eid = eid

    @classmethod
    def get_info(cls):
        print("Class EMP DATA :", cls.office)

Employee.get_info()

emp = Employee(101)
emp.get_info()  # This is not proper way of calling

# 2. only instance vars, instance methods            # Refer _4_instance_vars_methods.py

# 3. Combination of instance,class vars, methods      # Refer 28th line

'''
Usage of 
----------
Class vars     in  Class methods      YES
Instance vars  in  Instance Methods   YES
Class vars     in  Instance Methods   YES
Instance vars  in  Class methods       NO
'''

class Employee:
    # class variables
    comp_name = 'ORACLE' # Initialized while class loading
    c_address = "Whitefield,Bangalore"

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    @classmethod
    def get_comp_data(cls):  # class method
        print("Get company name : ", cls.comp_name, cls.c_address)

    def get_emp_details(self):
           print("Emp details are :",self.eid, self.name, self.sal,self.comp_name,self.c_address)

madhu = Employee(100,'Madhu N',100000)
madhu.get_emp_details()  # Employee.get_emp_details(madhu)
madhu.get_comp_data()    # Employee.get_comp_data(madhu)


'''
Class:
  class vars
  constructor
  class method
  instance method


instance method : obj.methodname()           # This is better
                  classname.methodname(obj)  # This is not correct approach

class method : classname.methodname()   # This is better
               obj.methodname()         # This is not correct approach

class variable : classname.var # This is better
                 self.var      # This is not correct approach     
        

class method    : implement behavior only on class variables
instance method : implement behavior only on instance variables
                  implement behavior  on  both (class+instance) variables
                  

'''


'''
Class structure:
-----------------

class Employee:

    #1. Class variables
    #2. Instance variables

    #3  Class Methods      
    #4  Instance Methods
    #5  Static Methods

eid name salary mobileno emailid office o_adress e_address attendance empcount (sharable+Modifiable)
I   I      I     I          I     C       C       I          C          C

2 Types of class variables:
----------------------------
c_name            sharing
c_address         sharing 
empcount - 91     sharing + modify     
attendance  - 11  sharing + modify 


'''
print("----------------------------------")
class Employee:
    e_count = 0
    def __init__(self,eid,name,sal):
        self.eid = eid
        self.name = name
        self.sal = sal
        Employee.e_count += 1

    def get_edata(self):
        print("Employee details are :",self.eid,self.name,self.sal)
        print("Emp count now  :",Employee.e_count) # self.e_count

madhu = Employee(1,'Madhu N',20000)
madhu.get_edata()
yogi = Employee(2,"Yogeswar",15000)
yogi.get_edata()
print(Employee.e_count)
