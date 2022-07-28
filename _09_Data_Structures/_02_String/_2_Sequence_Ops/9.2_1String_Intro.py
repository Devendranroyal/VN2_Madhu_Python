'''

@author: mnettem
'''
from sys import getsizeof

msg = 'hello world!'
print("----message1-----", msg)

message2 = "PYTHON PROGRAMMING!"
print("----message2-----",message2)

'''
1. indexing
2. slicing
3. adding
4. multiplying and
5. checking for membership.
'''
msg = 'hello world!'

# 1 INDEXING
print("----- 1st index in message1 -----", msg[4])
print("----- 4th index in message1 -----  Positive : ", msg[1], "  Negative :  ", msg[-11])

# 2 SLICING 
print("Slicing positive : ", msg[6:11])  # print from index 6 to position 11
print("Slicing Negative : ", msg[-6:-1]) #
print("Slicing with start stop step : ",message2[0:9:3], " == ",message2[0:13], "  ",message2[0:13:2]," ",message2[0:13:3])
print("Slicing without any positions + :",message2[::],"  ",message2[2::]," ",message2[:8:]," ",message2[::2]," ",message2[::3])
print("Slicing without any positions - :",message2[::],"  ",message2[-2::]," ",message2[:-8:]," ",message2[::-2]," ",message2[::-3])



# 3 ADDING CONCATINATION

final_message = msg + " Welcome to " + message2

print("Concatenation :: ", final_message)



# 4 MULTIPLYING
print("Multiplication : ", msg * 4)
print("Multiplication : ", final_message*4)


# 5 CHECKING FOR MEMBERSHIP
print("--Membership---- : ", "PYTHON" in message2)
print("--Membership---- : ", "IN" in message2)
print("--Membership---- : ", "IAM" in message2)


# 6 len()

msg ='Hello World'

print("Length of string : ", len(msg))

# 7 max()
print("Max value in string  : ", max(msg))
msg1 = '12345'
print("Max value in string  : ", max(msg1))

# 8 min()
print("Min value in string  : ", min(msg))
msg1 = '12345'
print("Min value in string  : ", min(msg1))
