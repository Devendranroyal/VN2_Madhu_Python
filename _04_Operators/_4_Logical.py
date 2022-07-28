# Boolean   True 1   False 0

# num div by 5 or 7 :
num = 15
if num % 5 == 0 or num % 7 == 0:
    print("Yes. Valid number")
else:
    print("Invalid number")


x = True
print("Value of x: ", x)
x = False
print("Value of x: ", x)

# Logical gate ===> and or not

# OR operator:
# Guest   Coffee or Tea
print("OR 1 :", True or False)   # True
print("OR 2 :", True or True)    # True
print("OR 3 :", False or True)   # True
print("OR 4 :", False or False)  # False
print("-----------------------")

# 3  - 2   ==> Final     M1(W) M2(W) M3(Optional)  - Final
#                        M1(W) M2(L) M3(W)         - Final
#                        M1(W) M2(L) M3(L)         - HOME

# AND operator:
# Guest Water and Coffee
print("AND 1 :", True and False)  # False
print("AND 2 :", True and True)   # True
print("AND 3 :", False and True)  # False
print("AND 4 :", False and False)  # False


# not
not True  # False
not False  # True

'''
condition1   AND/OR    condition2   AND/OR  condition3

condition
not condition

'''
print("Cond 1:", 10 > 20 and 5 < 2)  # False and False ==> False
print("Cond 2:", 10 < 20 and 5 > 2)  # True and True  ==> True
print("Cond 2:", 10 < 20 and 5 < 2)  # True and False  ==> False
# print("Cond 3:", not 5>2)
