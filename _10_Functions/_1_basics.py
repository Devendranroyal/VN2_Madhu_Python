'''
Data structures : State     - NOUN
Function        : Behavior  - Verb/Adverb

print()  : prints the given content
id()     :
type()   :

int() float() complex()
bool()

str() 40+
list() 10+
tuple() 2+
dict() 10+
set() 3+



'''
#include<stdio.h> prinf scanf

# builtins.py
# Function calling/Invocation
print("Hello World")

# REQ: Adding 2 numbers

       # I. STATE : Customer input
num1 = int(input("Enter number 1 :"))  # 10  Static way
num2 = int(input("Enter number 2 :"))  # 20  Static way

       # II. BEHAVIOR: Business Logic
result = num1 + num2

# III. Give response to user
print("Addition is : ", result)


print(10,20)
print("------------")


'''
# Find sum of 2 given numbers
--------------------------------
STATE    ==> I.  ==> 10,20  
BEHAVIOR ==> II, III. Perform addition and give result 

STATE:
--------
       # I. Customer input
num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))

BEHAVIOR:
----------
       # II. Business Logic
result = num1 + num2
       # III. Give response to user
print("Addition is : ",result)


# FUNCTIONS
Advantages: - Avoids code duplication ==> Achieves Code reusability
            - When enhancements are required, 
                        we need "code changes" in only one place 

# Functions:
----------------
f(x) = 2x**2+3x+1.

def f(x):
    res = 2x**2+3x+1
    

    
f(x) = 2x2+3x+1. Find the value of f(x) when x is 10
f(10) = 2(10*10)+3(10)+1
      = 2(100)+30+1
	  = 200+30+1
f(10) = 231

Find the behavior  of f(x) when x value ranges from -2 to 2
f(-2) = 2(-2*-2)+3(-2)+1  = 3
f(-1) = 2(-1*-1)+3(-1)+1  = 0
f(0)  = 2(0*0)+3(0)+1  	  =	1
f(1)  = 2(1*1)+3(1)+1     = 6
f(2)  = 2(2*2)+3(2)+1     =15

f(x) = 2x2+3x+1    # Function definition
f(2)               # Function calling by passing value
2(2*2)+3(2)+1      # Function execution
15                 # Function end result 
'''

# REQ: Find sum of 2 numbers

# I. Solution without functions
print("I. Addition in normal way")
    # I. STATE
num1 = int(input("Enter number 1 :"))   # 1. Customer input
num2 = int(input("Enter number 2 :"))

    # II. BEHAVIOR
result = num1 + num2             # 2. Business Logic
print("Addition is : ", result)  # 3. Give response to user

# Problem with above code
'''
Code duplication ==we should achieve==> Code reusability
'''

# II. Solution with functions
print("II. Addition using functions")

    # I. STATE
num1 = int(input("Enter number 1 :"))   # 1. Customer input
num2 = int(input("Enter number 2 :"))

    # II. BEHAVIOR
# 2. Business Logic
# 3. Give response to user
def add(n1, n2):    # n1,n2 paramters
    result = n1 + n2
    print("Addition is : ", result)

add(num1, num2)   # num1, num2 arguments
add(-10, -20)
add(10, 20)       # 10,20 arguments
add(0, -20)
add(-20, 0)
add(0, 10)
add(10, 0)
add(0, 0)
add(10+20, 40+50)
