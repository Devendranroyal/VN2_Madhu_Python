# break

# print first 7  between 1 to 20
#  1 2 3 4 5 6 7
n1 = 1
n2 = 20
counter = 0
while n1 <= n2:
    print(n1)
    counter += 1
    if counter == 7:
        break
    n1 += 1
print("---End of loop------")


# Print first 11 even numbers between 1 to 100
# counter = 3
# 2 4 6 8 10 12 14 16 18 20 22
print("------11 even numbers------")
n1 = 1
n2 = 100
counter = 0
while n1 <= n2:
    if n1 % 2 == 0:
        print(n1)
        counter += 1
        if counter == 11:
            break
    n1 += 1
print("End of while loop")

print("----wrong program-----")

n1 = 1
n2 = 100
while n1 <= n2:
    if n1 % 2 == 0:
        print(n1)
    if n1 == 11:
        break
    n1 += 1
print("End of while loop")

# Print first 4 numbers divisible by 6  between 1 to 100
'''
1   2  3  4  5  6  7  8  9 10
11 12 13 14 15 16 17 18 19 20
21 22 23 24 25 26 27 28 29 30
........ 

required output : 6 12 18 24
count = 4
'''
print("--------Divisible by 6----------")
n1 = 1
n2 = 100
count = 0
while n1 <= n2:
    if n1 % 6 == 0:
        print(n1)
        count += 1
        if count == 4:
            break
    n1 += 1
print("End of while loop")
