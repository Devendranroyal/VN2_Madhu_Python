# Passing Arguments
'''
1. Positional arguments (Required arguments)
2. Default arguments
3. Keyword arguments (Named arguments)
'''
x = 10    # int x = 10

# list1.append()  list1.remove(100) list1.pop(3)
# Find sum of 3 numbers
# Find division of 2 numbers : def divide(n1,n2):

# 1. Positional arguments (Required arguments)
print("--------1. Positional arguments--------------")

# UI --> Python --->  Database
         # ----------------------

def sum(n1, n2, n3):   # sum(int n1, int n2, int n3) sum(int n1, String n2, List n3)
    print("In sum method : with vals :", n1, n2, n3)
    res = n1 + n2 + n3
    print("Sum is : ", res)

sum(10, 20, 30)
# sum(10, 20)            # TypeError: sum() missing 1 required positional argument: 'n3'3#
# sum(10, 20, 30, 40)    # TypeError: sum() takes 3 positional arguments but 4 were given

x = 10
x = 20

# 2. Default arguments

print("--------2. Default arguments-------------")
# Function overloading
def sum(n1, n2, n3 = 1000):   # int float bool str  list tuple dict set
    res = n1 + n2 + n3
    print("Sum is : ", res)

sum(10, 20)      # n3 = 1000
sum(10, 20, 30)  # n3 = 1000 will be overriden with 30
# sum(10)          # sum() missing 1 required positional argument: 'n2'
# sum(10, 20, 30, 40)  # Additional argument

list1 = [10, 32, 43, 32, 63, 32, 13, 56]
# Remove 32
list1.remove(32)
list1.pop(3)
list1.pop()   # def pop(ind = -1):
                   # body



def feedback(rating=10, comments = None):
    print(rating, comments)

print("Feedback : ", feedback())
print("Feedback : ", feedback(9))
print("Feedback : ", feedback(4, 'Average'))
print("Feedback : ", feedback(comments='Good'))


def sum(n1, n2=500, n3=1000):
    res = n1 + n2 + n3
    print("Result : ", res)

sum(10)
sum(150, 250)
sum(150, 250, 350)

# print("Zero argument    :", sum())
print("One argument     :", sum(10))
print("Two argument     :", sum(10, 20))
print("Three argument   :", sum(10, 20, 30))
#print("Extra arguments  :",sum(10,20,30,40))

def sum(n1 = 100, n2 = 500, n3 = 1000):
    res = n1 + n2 + n3
    return res

print("Zero argument    :", sum())
print("One argument     :", sum(10))
print("Two argument     :", sum(10, 20))
print("Three argument   :", sum(10, 20, 30))

'''
def sum(n1=2000, n2, n3=1000):
    res = n1 + n2 + n3
    print("Sum is : ",res)
'''



# insert into employee values(100,'Madhu',3000)
# insert into employee(eid, sal, ename ) values(100,3000, 'Madhu')

# 3. Keyword arguments (Named argument)
print("--------3. Keyword arguments-------------")

def sum(n1, n2, n3):
    res = n1 + n2 + n3
    print("Sum1 is : ", res)

sum(10, 20, 30)           # 1.Positional/Required
sum(n1=10, n2=20, n3=30)  # keyword arguments
sum(n2=20, n1=30, n3=10)  # keyword arguments
sum(n3=20, n1=30, n2=10)  # keyword arguments

def get_order_info(mobile, ref_no, order_no, quantity, price):
    print("Order details :")
    print(order_no, ref_no, quantity, price, mobile)

get_order_info(8975435643, 9865432132, 1234, 40, 65876)

get_order_info(mobile=8975435643,
               quantity=40,
               price=65876,
               order_no=1234,
               ref_no=9865432132)



def sum(n1, n2, n3 = 45):
    res = n1 + n2 + n3
    print("Sum is : ", res)

# sum(10)
sum(10, 20)
sum(10, 20, 30)            #  Positional
sum(n2=10, n3=20, n1=30)   # Keyword
sum(n2=10, n1=30)          # Default + Keyword
sum(n1=30, n2=10)          # Positional + Default + Keyword

list1 = [1, 2, 3, 4]
list1.insert(1, 1000)   # def insert(index, value)
# list1.insert(1000)
print(list1)

list1.pop()             # def pop(index = -1):
list1.pop(2)
print(list1)

def append(n1,n2):
    print("Appending to list",n1+n2)

print("Append : ", append(10,20))