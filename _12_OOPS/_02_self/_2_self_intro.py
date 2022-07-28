
def get():
    print("Function get()")


print("Function name :", get)  # Function name    x = 10   get = <func addr>
get()  # Function call

# print("Employee address : ",Employee)

'''
Here python will load the class Employee and provides memory for class body'''
x = 10
# Employee = <body of Employee>

class Employee:
    # STATE
    def __init__(self, eid, name, sal):
        print("Self address  ", self)
        self.eid = eid
        self.name = name
        self.sal = sal
    # BEHAVIOR
    def get_e_info(self):
        print("Employee details are : ", self.eid, self.name, self.sal)

print("Employee address : ", Employee)

madhu = Employee(100, 'Madhu Nettem', 15000)  # object creation
madhu.get_e_info()
print("Madhu salary : ", madhu.sal)

print("Employee address : ", Employee)
print("Employee object  : ", madhu)   # address
'''
Step1 : 2 parts : 
             I. Employee  
            II. (100, 'Madhu Nettem', 15000)
Step2 : Python will check and find the address of Employee
Step3 : First python creates empty object(wrapper) of Employee class
        Employee class __init__ method will be called, passes 
                1. Address of empty object to self parameter         ==> self
                2. the tuple of arguments will be passed to remaining parameters  ==> (eid, name, sal) 
Step4 : Data passes to local variables (eid, name, sal)               
Step5 : self.eid = eid 
                    LHS eid = instance variable
                    RHS eid = local variable 
        ==> Local variable eid data,we are setting to instance variable 
        
        self.name = 'Madhu Nettem'
        self.sal = '15000'

        -  Inside object data will be initialized.
        - __init__ method helps to initialize the STATE of object(instance)


'''

print("Madhu object : ", madhu)
madhu.get_e_info()

# string list tuple dictionary set
msg = 'Hello world'  # STATE     # str("Hello world")
msg.capitalize()     # BEHAVIOR
list1 = [1, 2, 3, 4, 5]  # STATE # list([1,2,3])
list1.append(10)     # BEHAVIOR


# STATE
item_id = 1001
name = 'Chocolate'
price = 15

def get_final_price(i_id, c_name, c_price):
    if c_price <= 5:
        disc = 5*10/100
        final_price = c_price - disc
        print("Final price : ", final_price)
    elif c_price >=5 and c_price <= 10:
        pass

get_final_price(item_id, name, price)