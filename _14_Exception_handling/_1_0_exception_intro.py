'''
Traceback (most recent call last):
  File "C:/Users/madhu/git_projects/Batch_13/B13_PythonTraining/_13_Exception_handling/_1_Introduction.py", line 20, in <module>
    x = int(input("Enter numerator value :"))
ValueError: invalid literal for int() with base 10: 'dfgads'
'''
'''
Requirement: As an end user i will give 2 values,
             display division result for the same.
   
   If failure:  User entered other than nums  --- Display failure message
   If success:  User entered numbers          --- Display result
                 - If abnormal situation 
                             ---------------Display the exception message           
'''
# Before Exception handling
print("----Before Exception handling----")

x = int(input("Enter numerator value :"))
y = int(input("Enter denominator value :"))
print("Division :", x / y)  # 0/any value = 0   any value/0 = infinity
print("Remaining Code")
print("---------------------------------")

'''
Blocks   : if else elif for while  function class

Blocks to handle the exception
===============================    
try*      : Code which causes the exception
except*   : to handle exception occured in try block
else
finally
'''

# After Exception handling
print("----After Exception handling----")
try:
    x = int(input("Enter numerator2 value :"))
    y = int(input("Enter denominator2 value :"))
    result = x / y #  any value/0 = infinity
    print("Division :", result)  #  any value/0 = infinity
    print("---Division result usage---")
    print("---In try block3 ---")
except:
    print("EXCEPTION :: Please enter denominator other than 0")
print("---Remaining code II---")
print("---------------------------------")


# After Exception handling
print("----After Exception handling----")
try:
    x = int(input("Enter numerator3 value :"))
    y = int(input("Enter denominator3 value :"))
    result = x / y #  any value/0 = infinity
    print("Division :", result)  #  any value/0 = infinity
    print("---Division result usage---")
    print("---In try block3 ---")
except ZeroDivisionError as e:  # ZeroDivisionError e = ZeroDivisionError("ERROR MSG")
    print("EXCEPTION occured : ", e)
print("---Remaining code II---")
print("---------------------------------")


'''
ATM money transfer
pinno
amount 
10,000
Amount: System Issue 

hdfc bank   : api call rest 
CANARA bank : atm machine exception 
'''