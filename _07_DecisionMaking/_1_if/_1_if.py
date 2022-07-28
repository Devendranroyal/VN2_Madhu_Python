
a = 10
if a == 10:
    print("Welcome to Hello World")
    print("Welcome again")
print("-----End of if-----")

print("-----------------------------------")

age = 10
# and = 10
And = 10
'''
# True ==> non-zero         non None
           -5,6,4.5,-3.6    'M' [1,2] (1,) {1:1,2:2}, {1,2,3}
# False ==> zero            None
            0               ''  [] () {} {}
'''

x = 100
is_active = True
is_perm = False

if x == 10:
    print("Value of x: ", x)
print("----hello-----")

if 10+20:
    print("Hello")

if 10+'hello':
    print("ERROR")
'''
Operators:
-----------
Arithmetic ops ==> add/sub/mul/div/mod/floordiv 
                                ----> VALUE ==> zero(False)/nonzero(True)

Assignment ===>  x = 10         ----> VALUE ==> zero(False)/nonzero(True)

Comparison ===> == != > < >= <= ----> True/False
Logical   ====>  and or not     ----> True/False
Membership ===>  in not in      ----> True/False
Identity   ===>  is is not      ----> True/False

Water and Coffee
------------------
True and True*   = True
True and False*  = False
False* and True   = False
False* and False  = False

Coffee or Tea:
----------------
True* or True = True
True* or False = True
False or True* = True
False or False* = False

True --> nonZero              nonNone 
         10 -10 10.4 -3.4     'Hello' [1,2,3] (1,2,3) {1:1,2:2} {1,2,3}

False --> 0                   None 
                              '' [] ()  {} set({})
if True{
print("Executed");
}
'''

x = 10  # Direct/Final/Absolute value 10
print("Value of x: ", x)
x = 10+20  # addition ops 30
print("Value of x: ", x)
'''
After if <condition> can be:
True              False
--------------------------------------
10,10.4,'Hello'    None '' [] () {} {}
-10,-5
Any operation which gives final result as True/False   0/non0  None/notNone


'''
x = 10+5
print("----------------if conditions----------------")
if x == 15:
    print("Executed successfully")
    print("Condition is True")

print("------End of if-------")



if '':
    print("Will not execute2")

if 'hello':
    print("Hello executed")


if 10 < 20:
    print("Yes.Condition is True")

if 10 > 20:
    print("No. Condition is False1")

if not 10 > 20:
    print("No. Condition is False2")

if False:
    print("No execution.")

if True:
    print("Will execute1")

if not False:
    print("Will execute")

print("--Hello World---")

if None:
    print("None exec:")
if not None:
    print("Not none value : ")

if 'Madhu':  # [1,2,3], (1,2,3), {1:1,2:2}  {1,2,3,4}
    print("Name exececuted")
if '':  # []  () {}
    print("Empty string")

if not '':
    print("Empty string occurance")


print("Arithmetic :", 10 + 20)
print("Relational :", 10 >= 20)
print("10 and 20 :", 10 and 20)  # 20 True and True --> True
print("10 and 0  :", 10 and 0)   #  0 True and False --> False
print("0 and 20 :", 0 and 20)    #  0 False and True --> False
print("0 and 0 :", 0 and 0)      #  0 False and False --> False
print("10 or 20 :", 10 or 20)
print("10 or 0 :", 10 or 0)
print("0 or 20 :", 0 or 20)
print("0 or 0 :", 0 or 0)
print("Membership :", 10 in [10, 20, 30])
print("Identity    :", 10 is 10)

x = 20
if x == 10:
    print("X value")

'''
Arithmetic ops: +-*/ // %       ==> 0 / nonzero 
Relational ops: > >= < <= == != ==> True/False
Assignment ops:                     x = 10  x = -10.4
                                    x = 0   x = None
Logical  ops   :                ==> True/False
Bitwise       :                 ==> 0 or 1   False/True
Membership    : in not in       ==> True/False
Identity      : is is not       ==> True/False

'''

'''
1. Single condition     : 1 ==> if 


2. Multiple conditions  : 2 ==> if else
                          3 ==> if elif else            # if   else if    else 
                          4 ==> if elif elif else
                          5 ==> if elif elif elif else
                          ....

3. nested conditions    : nested if 

                            10th exam   
                            -----------
L1:            1. PASS                            2. FAIL 
L2:         1.continue     2. disc.           1. retry    2. stop 
L3:    1.Inter   2.Diploma        
L4:  1.MPC  2. BiPC
L5:        1.Govt  2.Pvt

'''
'''
SDLC Process:
-------------
S1 : REQUIREMENT : If user entered value is 20,
                   then print  "Welcome to Python World" message

S2: ANALYSIS :   Functional Analysis
                 Technical Analysis

S3: DESIGN: 
            Step1 : Take the user input
            Step2 : Compare the user(customer) provided input with given value(20)
            Step3 : If True, print the message "Welcome to Python World"

S4 : Development
S5 : Testing
S6 : Deployment/Production
'''
print("----------if---------------")
# S4: DEVELOPMENT      # Business logic implementation

val = int(input("Enter number: "))    # S1
if val == 20:                         # S2
    print("Welcome to Python World")  # S3

print("--------------------------------")

# S5 : Testing
'''
        Positive scenarios  : 20  
        Negative scenarios  : 15 25 0 -5  -20 -25
'''

'''
Condition : Success ==> True  nonZero nonNone
            Failure ==> False Zero    None
 True    / False 
 Non 0   / 0  
 nonNone / None
 
1. Single condition : if 
'''
# arithmetic
if 10+20:  # 30
    print("Successfully executed 10+20")  # Indentation

if True:
    print("True condition")

if False:
    print("False condition")

if not False:
    print("Print False condition")


if True or False:
    print("OR - condition ")

if True and True:
    print("AND - condition")

if 0:
    print("Value 0")
if None:
    print("Value None")
if not 0:
    print("Value 1")
if not None:
    print("Value not None")

if 10-20:
    print("Addition is success")

if 10 < 20:
    print("End of the program")



if 10 < 20 or 4 < 5:
    print("YES")



