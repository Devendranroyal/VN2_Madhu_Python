

class Employee:
    pass

'''
converts as below
                        class Employee:
                            def __init__(self):
                                pass
'''
print("Employee class @ ", Employee)
obj = Employee()

# Default constructor
class Employee:

    def __init__(self):  # Default constructor
        pass  # to perform any generic action


    def getedata(self, eid, sal):
        print("Employee Data", eid, sal)

madhu = Employee()
madhu.getedata(101, 10000)  # Employee.getedata(madhu,101,10000)





# while defining class, default constructor is not mandatory.
# Python give automatically



# Employee CRUD Operations

'''
REQUIREMENT :
1. Create an employee with eid,name,sal  #
2. Retrieve emp details 
3. Give hike for employee based on experience
    Acceptance Criteria : 0 to 2 exp  => 5% hike
                          2 to 3 exp  => 10% hike
                          3 to 5 exp  => 20% hike
                          5+          => 30% hike
                          
4. Delete emp once he exits from company

GUI  -->  Backend             ---> Database

UI  --->  Python/Java/.Net    --->  Oracle/Postgresql/Mysql/Mongodb
'''

print("-----------Employee hike---------------")

class Employee:
    # create employee
    def __init__(self, eid, name, sal):  #emailid,mobiileno,perm_address,pre_add,joining_date,bloodgr,gendder
        self.eid = eid
        self.name = name
        self.sal = sal

    # 2. Retrieve emp details
    def get_emp_info(self):
        print("Employee details : ", self.eid, self.name, self.sal)

    # 3. Update emp sal based on exp
    '''
        3. Give hike for employee based on experience
        Acceptance Criteria : 0 to 2 exp  => 5% hike
                              2 to 3 exp  => 10% hike
                              3 to 5 exp  => 20% hike
                              5+          => 30% hike
    '''
    def update_emp_sal(self, exp):
        # Server validations
        if exp < 0:
            print("Please enter valid experience.")
            return None
        if exp >= 0 and exp < 2:
            hike = (self.sal * 5) // 100
            self.sal = self.sal + hike
        elif exp >= 2 and exp < 3:
            hike = (self.sal * 10) // 100
            self.sal = self.sal + hike
        elif exp >= 3 and exp < 5:
            hike = (self.sal * 20) // 100
            self.sal = self.sal + hike
        elif exp >= 5:
            hike = (self.sal * 30) // 100
            self.sal = self.sal + hike
        print("Employee  after hike : ", self.eid, self.name, self.sal)

    def delete_emp(self):
        pass


# Data hard coding
madhu = Employee(100, 'Madhu N', 1500000)
madhu.get_emp_info()
madhu.update_emp_sal(4)


'''
UI PAGE:
---------
EmmpID: 101
name  : Madhu Nettem
exp   : -10 
Mobileno : 34232443243

# client validations 
# server validations
'''