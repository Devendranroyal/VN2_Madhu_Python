'''
Traceback (most recent call last):
  File "C:/Users/madhu/git_projects/Batch_13/B13_PythonTraining/_13_Exception_handling/_1_1_Exception_handling.py", line 6, in <module>
    print("Division :", x / y)
ZeroDivisionError: division by zero
'''

'''
HANDLING MULITPLE EXCETIONS
'''
print("Start of program")
try:
    # print("----While Exception handling----")
    x = int(input("Enter numerator value :"))
    y = int(input("Enter denominator value:"))  # ValueError
    li = [1, 2, 3, 4]
    print("List data :", li[2])  # IndexError
    print("Division :", x / y)   # ZeroDivisionError
    print("Hello world")
    print("---------------------------------")
except ValueError as ve:
    print("** Value Error : ==> ", ve)
except IndexError as ie:
    print("** Index Error : ==> ", ie)
except ZeroDivisionError as zde:
    print("** Zero Division Error : **", zde)
except Exception as e:
    print("Exception occured : ", e)
print("End of program")
print("---Remaining code---")  #remaining piece of code

'''
Program Execution Flow:
-----------------------
Exception didn't happen :  1. Statements before try block
                           2. Statements in try block(ALL)
                           3. Statements after except block
                           
Exception occured       :  1. Statements before try block
                           2. Statements in try block,till the line of exception occurance
                           3. Statements in except block
                           4. Statements after except block     
                           
 - Python at a time,handles only one exception
 - If there is chance of multiple exceptions,handle using multiple except blocks
 -                 
'''
