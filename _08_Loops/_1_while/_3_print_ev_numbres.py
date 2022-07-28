
# REQ : Print even numbers between 1 to 10
'''
  | 2  4          |   2)4(
'''
'''
# STATE    : num = 1

# BEHAVIOR : Print even numbers
             upper limit 10
'''
print("--------Print even numbers--------")
# STATE
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1

# REQ: Print numbers betweeen 2 to 100 which are divisible by 3 and 4
print("-----divisible by 3 and 4-----")
num = 2
while num <= 100:
    if num % 3 == 0 and num % 4 == 0:
        print(num)
    num += 1


print("--------Print odd numbers--------")

# Print odd numbers betweeen 10 to 20
num = 10
while num <= 20:
    if num % 2 == 1:
        print(num)
    num += 1

# Print numbers between 500 to 1000 and divisible by 5

print("--Numbers divisible  with 5------")
num = 500
while num <= 600:
    if num % 5 == 0:
        print(num)
    num += 1


# Print numbers between 500 to 1000. It should be divisible by 5 and divisible by 8
print("--Numbers divisible  with 5 and 8------")
num = 500
while num <= 600:
    if num % 5 == 0 and num % 8 == 0:
        print(num)
    num += 1

# Print numbers between 500 to 1000. It should be divisible by 5 or divisible by 9
print("--Numbers divisible  with 5 or 9------")
num = 500
while num <= 600:
    if num % 5 == 0 or num % 9 == 0:
        print(num)
    num += 1
