class EmployeeInformation:
       c_name = "ORACLE"
       c_addr = {'flatno':'45/3',
                 'landmark':'Near Videhi Hospital',
                 'area': 'ITPL',
                 'location':'Whitefield',
                 'city': 'Bangalore',
                 'pin':560037
                 }

       def __init__(self,eid,ename,sal,dept,tech_details):
           self.eid = eid
           self.ename = ename
           self.sal = sal
           self.dept = dept
           self.tech_details = tech_details

       def get_emp_details(self):
            print("Employee details are :",self.eid,self.ename,self.sal,self.dept)
            print("and his technology stack  in current project : ")
            for tech in self.tech_details:
                print(tech)

            print("His company complete addreess : ")
            for key,val in EmployeeInformation.c_addr.items():
                print(key,"    :",val)



madhu = EmployeeInformation(100,'Madhu Nettem',10000,15,['Python','Djago','Postgresql','Docker'])

tech_skills = ['Python', 'Djago', 'Postgresql', 'Docker']
madhu = EmployeeInformation(100, 'Madhu Nettem', 10000, 15, tech_skills) # this is better approach
madhu.get_emp_details()
