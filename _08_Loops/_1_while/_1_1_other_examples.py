# REQ: Print odd numbers from 1 to 100
# 1 3 5 7 9 11 13 ...
'''
Numbers between 1 to 100
Only odd numbers(Which are not divisble by 2)
'''
  #STATE
'''
num1 = 1
while num1 <= 100:
'''
print("-----------Odd numbers----------")
num1 = 1    # int(input("Enter number1: "))
num2 = 100  # int(input("Enter number2: "))
while num1 <= num2:
    if num1 % 2 == 1:
        print(num1)
    num1 += 1


print("------------ Divisible by 3 and 5 --------")
# Divisible by 3 and 5
num1 = 1
num2 = 100
while num1 <= num2:
    if num1 % 3 == 0 and num1 % 5 == 0:
        print(num1)
    num1 += 1

print("--------------------------------")

# REQ: Print even numbers between 1 to 20
# 2 4 6 8 10 12 .....
# 1 2 3 4 5 6 7 8 9 10 ....20
print("----even numbers between 1 to 20----")
# STATE
x = 1

# BEHAVIOR
li = []
while x <= 20:   # < =   > =    ! =
    if x % 2 == 0:
        li.append(x)
    x += 1
print("Even numbers: ", li)





# REQ: Print numbers divisible  by 5 between 1 to 100
# 0 5 10 15 20 25 .....
print("------Divisible by 5------")
n1 = 1
n2 = 100
while n1 <= n2:
    if n1 % 5 == 0:
        print(n1)
    n1 += 1
print("-------------------------")



# REQ: Print numbers divisible  by 3
# 3 6 9 12 .....

# REQ: Print numbers divisible  by 7
# 7 14 21 28 35 42 .......


# Print numbers divisible by 3 and 7
print("------Divisible by 3 and 7----------")
n1 = 1
n2 = 500
while n1 <= n2:
    if n1 % 3 == 0 and n1 % 7 == 0:
        print(n1)
    n1 += 1
print("----------------------------------")


# Print numbers divisible by 5 or 6
print("------Divisible by 5 or 6----------")
n1 = 100
n2 = 500
while n1 <= n2:
    if n1 % 5 == 0 or n1 % 6 == 0:
        print(n1)
    n1 += 1
print("----------------------------------")


print("------Numbers which ends with 0----------")
n1 = 100
n2 = 500
while n1 <= n2:
    if n1 % 10 == 0:
        print(n1)
    n1 += 1
print("----------------------------------")