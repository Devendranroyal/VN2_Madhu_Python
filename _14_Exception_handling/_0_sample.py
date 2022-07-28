
# Exception handling
'''
Traceback (most recent call last):
  File "C:/Users/madhu/git_projects/_14_Exception_handling/mypractice/test1.py", line 11, in <module>
    print("Result is ", in_val + 10)
TypeError: must be str, not int
'''
print("--Before list----")
list1 = [11, 22, 33, 45]
print(list1[4])
'''
- It will load the exception class IndexError 
- It will create object of IndexError with message
    IndexError("list index out of range")
- Throws object to console as we are not hanlding expception
'''
# print(100/0)
print("--After list----")
in_val = input("Enter value : ")
print("Result is ", in_val + 10)
print("End of program")
