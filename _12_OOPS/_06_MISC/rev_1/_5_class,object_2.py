
# With functions  :
# 1. STATE
eid = 100
name = 'Madhu Nettem'
sal = 25000.0

# BEHAVIOR
def emp_details(empid,name,salary):
    sal = salary + salary*10/100
    #print("The emp details are  :",empid,name,salary)

emp_details(eid,name,sal)

# 4 With OOPs

class Employee:
    # State
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def update_hike(self, h_perc):  # Update
        self.sal += self.sal * h_perc / 100
        print(self.name," got hike %:", h_perc)
    # Behavior
    def get_details(self):  # Retrieval
        print("Employee details : ",self.eid,self.name, self.sal)

madhu = Employee(501,'Madhu Nettem',25000)
madhu.get_details() # Employee.get_details(madhu)
madhu.update_hike(12)
madhu.get_details() # Employee.get_details(madhu)

kiran = Employee(502,'Kiran G',15000)
kiran.update_hike(15)
kiran.get_details() # Employee.get_details(madhu)

print("------------------------------------")





# Student, Teacher, Pen, Book, Phone, Laptop ......

# With Functions

pid = 123
pname = "Reynolds"
price = 10

def get_pen_details(penid,pen_name,p_price):
    print("Pen details are : ",penid,pen_name,p_price)

get_pen_details(pid,pname,price)

# With OOPs
class Pen:

    def __init__(self, pid, pname, price):
        self.pid = pid
        self.pname = pname
        self.price = price

    def get_pen_details(self):
        print("Pen details are : ", self.pid, self.pname, self.price)


mypen = Pen(123, "Reynolds", 10)
mypen.get_pen_details()