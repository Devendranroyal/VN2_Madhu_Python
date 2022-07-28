# WHY LOOPS

i = 1
while i > 10:
   print("Value is : ", i)
   i += 1

print("-----------Result with class-----------")


# take data for all 10 students using list or dictionary
s_marks = [30, 45, 67, 32, 5, 7, 86, 43, 99, 100, 0, 13]
          # [[1,30,'Madhu.N'],[],[]]
# s_marks = {1:[30,'Madhu N'],
#            2:[45, 'Rama']}
#            3:[67, 'Raja'
#            }

# STATE
marks = int(input("Enter exam marks  :"))

# BEHAVIOR

 # 1. Validation
if marks >= 0 and marks <= 100:
    # print("Valid input")
    if marks >= 35:
        print("RESULT : PASS")
        if marks >= 60:
            print("---FIRST CLASS----")
            if marks == 100:
                print("-----PERFECT-----")
            elif marks >= 90:
                print("----GOOD----------")
        elif marks >= 50 and marks < 60:
            print("---SECOND CLASS----")
        elif marks >= 35 and marks < 50:
            print("----THIRD CLASS----")
    else:
        print("RESULT : FAIL")
else:
    print("Invalid marks")

print("--------------------------------------")

# I REQ. Gathering : Print numbers from 1 to 10
# 1
# Code duplication, we can't extend when requirement changes

# State    : Is changing in each iteration
# Behavior : Same: Printing the data

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)


# I REQ. Gathering : Print numbers from 1 to 10

# Maths: 2 subprocesses
# write current number
# +1 in each iteration
# check whether values is <= 10
'''
1 2 3 4 5 6 7 8 9 10 

'''




'''
while <condition>:
    <stmts. body> 
'''
print("------------while loop----------------")
i = 1
while i <= 10:  # 3. check whether value reaches to 10
    print(i)    # 1. write it on paper
    i += 1      # 2. increment the value

print("End of program")




print("-----End of while loop-----")

'''
Print numbers between 1 to 10 except 5.

P1: Print number        1 2 3 4 6 7 8 9 10
P2: Increment number
P3: Check number <= 10
P4: Check num == 5
'''
print("----Numbers between 1 to 10 except 5----")
i = 1
while i <= 10:
    if i != 5:
        print(i)
    i = i+1

print("----Even Numbers between 1 to 10 ----")

i = 1
while i <= 10:
    if i % 2 == 0 :
        print(i)
    i += 1

print("------Numbers between 1 to 30 divisible by 3 and 5")

i = 1
while i <= 30:
    if i % 3 == 0 and i % 5 == 0:
        print("Value : ", i)
    i += 1







print("------Numbers between 1 to 100 divisible by 4 or 5 or 7")

i = 1
while i <= 100:
    if i % 4 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i)
    i += 1

'''
# STATE 
--------
1. Data initialization     x = 1

# BEHAVIOR
------------
2. Condition verification  while x <= 10
3. Business logic               print(x)
4. Operation on input data      x += 1
'''

print("--------------")
# II REQ. Gathering : Print numbers from 10 to 1
# 10 9 8 7 6 5 4 3 2 1
# STATE
x = 10
while x >= 1:
    print(x)
    x -= 1

# SDLC - Agile methodology

# I REQ. Gathering : Print numbers from 15 to 100
'''

    

'''
'''
# II - ANALYSIS
        1. Functional analysis : We need to print the numbers between starting and 
                                 ending number given by customer
        2. Technical analysis  : STATE    :  input: start end (int)
                                 BEHAVIOR :  Loops : while  
III.  Design : NA
'''
# IV. DEVELOPMENT
print("-----------While 15 to 30-----------")
print("--------WIHTOUT VALIDTAION---------")
    # STATE
start = int(input("Enter number1 :"))
end = int(input("Enter number2 :"))
    # BEHAVIOR
while start <= end:  # less than or equal 15 <= 15
    print(start)
    start += 1
print("***** End of program *****")

# V. TESTING:    tester found that validation is missing
'''
Test cases                                    Exp output           Act. output     Result
----------------------------------------------------------------------------------------------
    T1. Give lower,upper value and test      Print numbers b/w     As Expected          PASS 
    T2. Give upper,lower value and test      Should dispaly error  Its not displaying   FAIL
'''

# As a developer, will fix the issue by adding validation
print("--------AFTER FIXING THE ISSUE---------")
start = int(input("Enter number1 :"))
end = int(input("Enter number2 :"))
if start <= end:
    while start <= end:
        print(start)
        start += 1
else:
    print("### start val should be less than end  val ###")

print("***** End of program *****")



'''



'''