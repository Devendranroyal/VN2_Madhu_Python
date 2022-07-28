print(10)
# OR
x = 10
print(x)

print(x+20)
print(x+30)

print(10+20)

# OR
x = 10 + 20
print(x)
print("Value is : ", x)


# Get student result based on marks.
# User Criteria : <Pending>

def find_studentresult(marks):
    pass

find_studentresult(x)



print("--------Return types------------")
'''
Here sum function is taking 2 responsibilities
    1. Implementing the business logic
    2. Handling the end result/output
'''
# Without return types
def sum(n1, n2):
    result = n1 + n2
    print("Addition : ", result)

sum(100, 200)       # returns None

print("Function call2  :", sum(101, 201))  # returns None
print("-------List with return=------------")
li = [12, 32, 43, 24, 15]
print("Insertion: ", li.insert(2, 100))  #  no return type
print("Remove   : ", li.remove(24))  # no return value
print("Pop      : ", li.pop(2))  # it returns removed value


# with return type
def sum(n1, n2):
    result = n1 + n2
    return result  # int float bool string list tuple dict set

sum(11, 22)   #  int float bool string list tuple dict set
10000
x = 10000


# Return value : one time usage
print("Addition2 is  :: ", sum(25, 10))  # print(10)


# Correct approach
# Return value : Two or more places
output = sum(25, 10)              # x = 10    print(x)
print("Addition1 is  :: ", output)

print("----Return type examples----")

list1 = [1, 2, 3, 4, 5]
print("Before append : ", list1)
list1.append(50)  # It will append 50 to list1 and returns nothing
print("Append 100 :", list1.append(100))

app = list1.append(200)
print("Append 54 :", app)

print("After append  : ", list1)

print("-----Pop operations-------")
list1 = [1, 2, 43, 65, 23, 46, 78, 29, 83, 23, 3, 4]
print(list1.pop())  # It will remove last element and returns the element to us
print("Removed values1 is :", list1.pop())
print("LIST : ", list1)

val = list1.pop(5)
print("Values is :", val)
print(val)
print()
print("Removed value is2 : ", val)

print("Removed value is3 :", list1.remove(65))

print("Index is : ", list1.index(29))