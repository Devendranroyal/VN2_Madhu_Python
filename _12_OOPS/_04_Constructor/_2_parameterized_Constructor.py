''''''
'''

# Defining Constructor
    - Default constructor
    - Parameterized constructor
            - Positional arguments
            - Default arguments
            - keyword arguments

'''

# 1. Positional arguments

class Employee:
    # Parameterized Constructor
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def getedata(self):
        pass

madhu = Employee(200, 'MadhuN', 10000)


# 2. Default arguments example
class Employee:
    # parameterized constructors
    def __init__(self, eid=None, name=None, sal=None):  # Constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal

    def getedata(self):
        print("Employee info : ", self.eid, self.name, self.sal)


madhu = Employee()
madhu.getedata()

chandra = Employee(201)
chandra.getedata()

chandra = Employee(201, 'Chandra Sekhar')
chandra.getedata()

madhu = Employee(200, 'MadhuN', 10000)
madhu.getedata()


# 3. Keyword arguments
farooq = Employee(name='Raja', sal=20000)
farooq.getedata()
