

# continue : for some action, stop executing remaining lines of block and go to next iteration

# Print first 7 numbers  between 1 to 100. Which are divisible by 5.
# If number ends with 0(divisible by 10) don't consider it.

'''
1   2  3  4  5  6  7  8  9 10
11 12 13 14 15 16 17 18 19 20
21 22 23 24 25 26 27 28 29 30
........

required output : 5
count = 1
'''

n1 = 1
n2 = 100
count = 0
while n1 <= n2:
    if n1 % 5 == 0:
        if n1 % 10 == 0:
            n1 += 1
            continue
        print(n1)
        count += 1
        if count == 7:
            break
    n1 += 1
print("End of program")

# Every mobile postpaid bill every 24 hours
import time
while True:
    time.sleep(2)
    print("Python programming")