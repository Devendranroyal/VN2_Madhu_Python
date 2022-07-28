
'''
class structure
    # 1. Fields  - STATE
         class variables    - at class level,when state is shared among objects
         instance variables - at instance level, inside init method.
                              When each object required separate data

    # 2. Methods - BEHAVIOR
   C  I
   -----
   T  F     class method       - cls parameter,which works only on class variables
   F  T     instance method    - self parameter,which works on only instance variables
   T  T                                                         both instance,class variables
                                                            only class variables XXX
   F  F     static method       - generic method

'''
class Employee:
    def __init__(self):
         pass

    @staticmethod
    def get_edata():
        print("Employees info : generic behavior")

# no need to create object to call class methods
Employee.get_edata()  # Employee.get_edata(Employee)

#2 way - Don't do it
obj = Employee()
print("Object address : ",obj)
obj.get_edata()  # ==> Employee.get_edata(obj)

print("------All methods---------")
class Employee:
    e_count = 0
    office = 'ORACLE'

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal
        Employee.e_count += 1

    @classmethod
    def get_edata(cls):
        # print("Employees info : ",Employee.e_count,Employee.office)
        print("Employees info : ", cls.e_count, cls.office)


    def get_empinfo(self):
        print("Employee details : ", self.eid, self.name, self.sal)
        print("Class data : ", Employee.e_count, Employee.office)
        print(Employee.get_edata())
        print(self.get_edata())   # XXX

    @staticmethod
    def get_edata():
        print("Employees info : generic behavior")


# to call class method
Employee.get_edata()
# to call instance method
madhu = Employee(101, 'Madhu Nettem', 15000)
madhu.get_empinfo()
madhu.get_edata()
Employee.get_edata()


print("-----static method--------")

# i want a behavior which neither deals with class variables nor instance variables

class Employee:
    @staticmethod
    def getinfo():
        print("Static method implementation")

Employee.getinfo()



'''
class Employee:
    1. STATE
    ----------
    # class variables
    # instance variables ==> init method
    
    2. BEHAVIOR
    -------------
    # class method      : works only on class variables 
    # instance method   : works only on instance variables (OR)
                          works on both instance/class variables 
    # static method     : neither on class nor on instance variables 
'''
'''
class var                  instance var
-------------------------- ----------------------------
while loading class        at the time of object creation

class var                  instance var
class methods              instance methods

instance variables cant be used inside class method **

++ Within instance methods we can use class variables *****
viceversa is not True ==> within class methods we can't use instance varibales
'''


# UI --->   Python ---> Database

# Currently working as Software Engineer in Oracle from  Jun 2020 to till date
'''
Current employer: Oracle 
Designation : Software Engineer
From Date: June - 2020
To Date  : June - 2022

100 employees:
---------------
excel sheet
csv 

txt file 
---------
100,Madhu Nettem,15000,Bangalore,Oracle
101,
102,
....

Client                    Server      Drive

UI(Youtube)       --->    Python     ---->  Database

 
{'filenmae':
 'size':
 'ext':
 'format':
 'content':
 'drivepath':
}                         
                          
                          
                          
pdf file 
'''




