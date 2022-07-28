'''
Apply hike based on rating on a scale of 5.
If rating is 4 to 5 - 30%
             3 to 4 - 20%
             2 to 3 - 10%
             <2     -  no hike

Fields: Instance variables
        Class variables
Methods : Instance method
          Class method
          Static method
'''

# class
class Employee:
    # local variables   - eid, name, sal
    # instance variables - self.eid self.name self.sal - instance variables

    def __init__(self, eid, name, sal):
        # print("Self address : ", self)
        self.eid = eid
        self.name = name
        self.sal = sal
        self.address = ''

    def update_address(self, addr):
        self.address = addr
        # business logic

    # instance methods
    def get_edata(self):
        print("Employee information : ", self.eid, self.name, self.sal, self.address)

    def apply_hike(self, rating):
        print("Employee hike with rating : ", rating)
        hike = 0
        if rating >= 4 and rating <= 5:
            hike = self.sal*30/100
            print(" Hike is :: ", hike)
        elif rating >= 3 and rating < 4:
            hike = self.sal*20/100
            print(" Hike is :: ", hike)
        elif rating >= 2 and rating < 3:
            hike = self.sal*10/100
            print(" Hike is :: ", hike)
        else:
            print(" Hike is :: ", 0)
        self.sal = self.sal + hike
        print("Employee information : ", self.eid, self.name, self.sal)

madhu = Employee(100, 'MadhuN', 15000)   # CREATE
madhu.get_edata()                        # RETRIEVAL
madhu.update_address("Whitefield ITPL")  # UPDATE
madhu.get_edata()
rate = int(input("Please enter rating: "))
madhu.apply_hike(rate)

print("-------------------------------")
himaja = Employee(101, 'Himaja CR', 25000)
himaja.get_edata()
rate = int(input("Please enter rating: "))
himaja.apply_hike(rate)

print("-------------------------------")
abhi = Employee(101, 'Abhiram Naren K', 30000)
abhi.get_edata()
points = int(input("Please enter rating: "))
abhi.apply_hike(points)


e_data = [[100, 'Prakash', 25000], [101, 'XYZ', 35000], [102, 'Venkatesh', 30000]]
rating = {100: 4, 101: 2, 102: 4}

print("-----------BULK SALARY HIKE-----------")
for erecord in e_data:
    print("---------------------------------------")
    e_id = erecord[0]
    ename = erecord[1]
    esal = erecord[2]
    emp = Employee(e_id,ename,esal)
    emp.get_edata()
    rating = rating[e_id]
    emp.apply_hike(rating)
    #emp.get_edata()
    print("---------------------------------------")

