# Print even numbers between 1 to 100

# validation logic
# business logic

n1 = 1
n2 = 100

while n1 <= n2:
    if n1 % 2 == 0:
        print(n1)
    n1 += 1
'''
if n1 <= n2:
    # Implement business logic
    while n1 <= n2:
        if n1 % 2 == 0:
            print(n1)
        n1 += 1
else:
    print("------INVALID INPUT DATA------")
'''
# Print numbers between 500 to 600 which are divisible by 9

n1 = 500
n2 = 600
'''

'''
if n1 <= n2:
    while n1 <= n2:
        if n1 % 9 == 0:
            print(n1)
        n1 += 1
else:
    print("===INVALID INPUT DATA===")

# Print numbers between 1 to 100 which are divisible by 5 and 3
'''
1 2 3 4 5 6 7 8 9 10 .15.. 100
'''
'''
validation logic  : if else
business logic    : while
'''
n1 = 500
n2 = 600
if n1 <= n2:
    while n1 <= n2:
        if n1 % 5 == 0 and n1 % 3 == 0:
            print(n1)
else:
    print("===INVALID INPUT DATA===")
