'''
Traceback (most recent call last):
  File "C:/Users/madhu/git_projects/Batch_13/B13_PythonTraining/_13_Exception_handling/_1_1_Exception_handling.py", line 6, in <module>
    print("Division :", x / y)
ZeroDivisionError: division by zero
'''
print("Start of program")
try:
    print("----While Exception handling----")
    x = int(input("Enter numerator value :"))
    y = int(input("Enter denominator value:"))
    print("Division :", x / y)  # ZeroDivisionError("division by zero")
    list1 = [1, 2, 3, 4]
    print("List value : ", list1[10])  # IndexError("....")
    print("Hello world")
    print("---------------------------------")
except ValueError as ve:
    print("** ERROR : Please enter numbers for num/den values **", ve)
    # print(ve)
except ZeroDivisionError as zde:
    print("** ERROR : Please enter den. value other than 0 **", zde)
except IndexError as ie:
    print("** ERROR : Given index value doesnt exists **", ie)

print("----Remaining code----")  # remaining piece of code

