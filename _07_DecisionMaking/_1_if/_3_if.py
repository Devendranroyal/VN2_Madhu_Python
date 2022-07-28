
# We are assigning value 10 to variable x in Static manner
'''
10 --> static value
   --> hardcoded value
'''
x = 10
if x != 0:
    print("Value exists for x :", x)

# For Dynamic nature/ to receive the value at runtime

x = input("Enter any number1 :")
print(x, type(x))  # "100" '100'
if x != 0:
    print("Value exists for x :", x)


x = int(input("Enter any number2 :"))  # Here we are converting string of number to number
print(x, type(x)) #  100
if x >= 10:
    print("Value exists for x :", x)


