x = 10
print(x)
x = 10.5
print(x)
x = True   # 1 nonzero nonNone
print(x)
x = False  # 0  None
print("---------------------")

x = 0.1
y = 0.2
print("True or not :", x==y)
print(x+y)
# Find given number is even or odd
# Solution : If any number is divisible by 2 and remainder is 0, it is Even number,
# else odd number.
num = int(input("Enter number : "))
print("Given number : ", num)


# Decision Making
if num % 2 == 0:
    print("Even number")  # 4 spaces indentation
else:
    print("Odd number")   # block of statements

'''
If the condition is True program exuection will go inside of if block,
else it will go inside of else block
'''
'''
if num % 2 == 0{
print("Even number");
}
else{
print("Odd number");
}
'''

x = int(input("Enter number: "))

if x < 0:
    print("Negative number")
elif x > 0:
    print("Positive number")
else:
    print("ZERO : NEITHER POS NOR NEG")
