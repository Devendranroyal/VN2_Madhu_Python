# Variables
'''
if we want to use value in one place,
then directly use the value
'''
print(10)
print(10+20)

'''
if we want to use value in multiple places,
then assign the value to a variable 
'''
x = 10
print(x)
print(x+20)

res = 10+20
print(res)
print(res+100)


print("Addition is : ", 10+20)

x = 40
y = 50
print("Addition is : ", x+y)
print("Subtraction is : ", x-y)
print("Mulitplication is : ", x*y)
print("Division is : ", x/y)

x = 10
y = 20
res = x+y
print("Addition is : ", res)
print("Addition is : ", res+100)

print("-----Single usage------")
for char in 'Hello World':
    print("Character : ", char)

print("-----Multiple usage-----")

msg = 'Hello World'
for char in msg:
    print("Character : ", char)

print("Further usage : ", msg)