# REQ : Find sum of 2 given numbers

# 1. STATE
'''
num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))

'''
num1 = 10
num2 = 20


# 2. BEHAVIOR
def sum(n1, n2):
    result = n1 + n2
    print("Addition : ", result)

sum(10, 20)
sum(num1, num2)
sum(5 + 5, 10 + 10)

'''
9,10 : num1,num2  ==> Variables     : 10,20      ==> values
14   : n1,n2      ==> Parameters
17,18,19 :        ==> arguments     

'''
print(100)
print(40+60)


# Student result based on marks
# Validation

'''
Function can be defined without paramters, with any no of parameters

list1 = [1,2,3,4]
list1.remove(1)      # remove expecting argument.  def remove(var):
list1.copy()         # copy - 0 arguments          def copy():
list1.insert(1, 100) # 2 arguments                 def insert(ind, val):

'''
def get_data(eid,name,sal,address):
    print(eid,name,sal,address)


print("Get data : ", get_data(100,'Madhu',10000,'Bangalore'))









