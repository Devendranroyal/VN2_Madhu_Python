# Print numbers from 1 to 10   # 1 2 3 4 5 6 7 8 9 10

'''
- Start printing the number 1
- Increment by 1 for current number
- If the new value is less than 10 then print
- Else stop it
'''

'''
print(1)
print(2)
print(3)
....
num = 1
print(num)
print(num+1)
print(num+2)
print(num+3)
print(num+4)
print(num+5)
print(num+6)
print(num+7)

'''
# REQ: Print numbers from 1 to 10

# using while loop
print("--------Numbers from 1 to 10--------")

num = 1
while num <= 10:   # Check condition in each iteration
    print(num)
    num = num + 1  # num += 1

print("--------End of program--------")


# print numbers between 100 to 150

num = 1
while num <= 20:
    if num < 10:
        print(num, end='-')  # println  # \n
    else:
        print(num)
    num += 1
