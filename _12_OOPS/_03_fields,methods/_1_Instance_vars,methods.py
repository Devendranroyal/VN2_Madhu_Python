'''
Instance variables
Instance methods
'''
x = 10
print("Value x: ", x)

def func1():
    print("Funciton1 body")

func1()
print("Function name : ", func1)

'''
CLASS -    STATE     -  Fields
                            - Instance Variables*
                            - Class Variables
           BEHAVIOR  -  Methods
                            - Instance Methods*
                            - Class Methods
                            - Static Methods
                            

'''

# x = 100
class Employee:
    # Fields  - STATE
    # Methods - Behavior
    pass

class Employee:
    # local variables   - eid, name, sal
    # instance variables - self.eid self.name self.sal - Instance Variables
    def __init__(self, eid, name, sal):
        print("Self address : ", self)
        self.eid = eid
        self.name = name
        self.sal = sal
        x = sal

    # instance methods
    def get_edata(self):
        print("Employee information : ", self.eid, self.name, self.sal)
        print("value of x : ", x)

print("---Employee-------", Employee)

madhu = Employee(100, 'MadhuN', 15000)
madhu.get_edata()
Employee.get_edata(madhu)



# madhu.get_edata()  # Employee.get_edata(madhu)




li1 = [1, 2, 3]  # list1 is of type class list
li1.append(100)  # list.append(li1,100)
li1.pop()        # list.pop(li1)
