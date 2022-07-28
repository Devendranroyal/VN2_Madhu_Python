# Defining a Class
class Employee:
    # STATE   : fields(parameters)
    def __init__(self, eid, name, sal=10000):
        self.eid = eid  # instance variables / local variables
        self.name = name
        self.sal = sal
    # BEHAVIOR method(function)
    def get_edata(self): # instance method
        print("Employee details are : ")
        print(self.eid, " ", self.name, " ", self.sal)

# Object/Instance creation
madhu = Employee(101,'Madhu Nettem',20000)  # State initialization
madhu.get_edata() # Employee.get_edata(madhu)


'''
# front end 100 upload data structures numbers boolean string list tuple dict set
# [[101,'Madhu Nettem',10000], [101,'Madhu Nettem',10000], [], [],......]
e_data = {'emp1':{'empid':101,
        'ename':'Madhu Nettem',
        'salary':10000},
'emp2':{'empid':102,
        'ename':'Murali',
        'sal':20000}
}

for key,data in e_data:
    eid= data['eid']
    name = data['ename']
    sal = data['sal']
    e_ojb = Employee(eid,name,sal)
    #insert into Employee values()

x = 10
print(type(x))
print(type(madhu))
'''

#Pass values dynamically
eid = int(input("Enter emp id : "))
name = input("Enter emp name : ")
sal = input("Enter emp sal : ")
madhu = Employee(eid,name,sal)
madhu.get_edata()



from _12_OOPs._4_bike import Bike

bike1 = Bike("Pulsar 150CC ",'Black',100000)
bike1.get_bike_details()
