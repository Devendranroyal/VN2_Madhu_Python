'''
# Without EH
print("Start of program")
x = int(input("Enter numerator value :"))   # ValueError
y = int(input("Enter denominator value:"))  # ValueError
li = [1,2,3,4]
print(li[2])   # IndexError
print("Division :", x / y)  # ZeroDivisionError
print("Hello world")
print("---------------------------------")
'''
# Handling multiple exceptions
'''
HANDLING MULITPLE EXCETIONS

To handle multiple exceptions,write mulitple except blocks
Below code is not proper 
'''
print("Start of program")
try:
    print("----While Exception handling----")
    x = int(input("Enter numerator value :"))  # ValueError
    y = int(input("Enter denominator value:"))
    li = [5, 12, 23, 32]
    print("List val:", li[4])  # IndexError
    print("Division :", x / y)  # ZeroDivisionError
    print("Hello world")
    print("---------------------------------")
except Exception as e:
    print("** Error occured :  ==> ", e)

print("----REMAINING PIECE OF CODE-----")