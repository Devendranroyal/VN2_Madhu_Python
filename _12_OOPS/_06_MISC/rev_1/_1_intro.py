'''
# Object Oriented Programming System
Class Object
Encapsulation
Abstraction
Inheritance
Polymorphism

'''
# REQUIREMENT : Find length of the given list
# 1. CRUD       2. Datatype   3. State Behavior
# 1. Retrieval
# 2. list(input) int
# 3. State (Data)  Behavior (Functionality implementation)

# Approach 0 : Using Builtin functions 
list1 = [1,2,3,4,5]
print("---------Approach 0 : Using Builtin functions----------")
print("Length of list :",len(list1))

# Approach 1 : Normal code
print("---------Approach 1 : Normal code----------")
# STATE
list1 = [1, 2, 3, 4, 5] # customer provided input
le = 0  # To work on requirement
# BEHAVIOR
for each in list1:
    le += 1
print("Length of list :",le)

# Disadvantage : Code reusability is missing


print("---------Approach 2 : Using functions----------")

# Approach 2 : Using functions
# STATE
list1 = [1, 2, 3, 4, 5]

# BEHAVIOR
def find_length(in_list): # WORA
    le = 0
    for each in in_list:
        le += 1
    # print("Length of list : ", le)
    return le
# find_length(list1) # 2.1
val = find_length(list1) # 2.2
print("Length of list :",val)
print("Length of list :",find_length(list1)) # 2.3


# Using Functions
list1 = [1, 2, 3, 4, 5]

def find_length(in_list):
    le = 0
    for each in in_list:
        le += 1
    print("Length of list : ", le)

# Disadvantage : No security for State. To avoid this,use class structure


class SequenceLength:
    # STATE
    list1 = [1, 2, 3, 4, 5]

    # BEHAVIOR
    def find_length(in_list):
        le = 0
        for each in in_list:
            le += 1
        print("Length of list : ", le)