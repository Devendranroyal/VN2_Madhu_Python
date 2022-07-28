'''
OOPs : Object Oriented Programming
Why oops : To overcome drawback of direct state initialization(STATE + BEHAVIOR)

    obj.method().method1().method().method()
type declaration : int x = 10
                       x = 10

CRUD DATATYPE   STATE + BEHAVIOR

list1  = [1,2,3]
1. Builtin functions     : print("Length of list : ",len(list1))
2. DecisionMaking,Loops  : list1 = [1,2,3]  Beh : for loop            # we will never implement
3. Functions             : list1 = [1,2,3]  Beh : function : for loop
                            # STATE   # BEHAVIOR
4. OOPs                  : class : STATE + BEHAVIOR
'''


# Find length of list in python

# 1. Builtin functions :
list1 = [1,2,3,4,5]
print("1. Builtins  : Length of list : ",len(list1))

#2. Manual implementation : DecisionMaking,Loops

list1 = [1,2,3,4,5]  # State

length = 0          # Behavior
for each in list1:
    length += 1
print("2. Man. impl : Length of list : ",length)

#3 Functions
list1 = [1,2,3,4,5]       #STATE
def get_length(in_list):  #BEHAVIOR
    length = 0
    for each in in_list:
        length += 1
    return length

print("3. Functions : Length of list : ",get_length(list1))

#4 OOPs
print("---------------4.1 With Instance variable----------------------")
class ListLength:
    # STATE
    def __init__(self, list1):
        self.list1 = list1

    # BEHAVIOR
    def get_length(self):
        length = 0
        for each in self.list1:
            length += 1
        return length

obj = ListLength([1,2,3,4,5])
res = obj.get_length()
print("4.1 OOPs      : Length of list : ",res)

print("---------------4.1.1 With Instance method calling----------------------")
class ListLength:
    # STATE
    def __init__(self):
        pass

    # BEHAVIOR
    def get_length(self, list1):
        length = 0
        for each in list1:
            length += 1
        return length

obj = ListLength()
res = obj.get_length([1,2,3,4,5])
print("4.1 OOPs      : Length of list : ",res)


#print("4. OOPs      : Length of list : ",ListLength([1,2,3,4,5]).get_length())   #print(10)

print("---------------4.2 With class  variable----------------------")
class ListLength:
    # STATE
    list1 = [1,2,3,4,5]

    def __init__(self):
        pass
    # BEHAVIOR
    @classmethod
    def get_length(cls):
        length = 0
        for each in cls.list1:
            length += 1
        return length

print("4.2 OOPs      : Length of list : ",ListLength.get_length())

print("---------------4.2.1 With class method calling----------------------")


class ListLength:

    def __init__(self):
        pass

    # BEHAVIOR
    @classmethod
    def get_length(cls, list1):
        length = 0
        for each in list1:
            length += 1
        return length

print("4.2 OOPs      : Length of list : ", ListLength.get_length([1,2,3,4,5]))

print("---------------4.3.  With static  method----------------------")
class ListLength:
    # STATE
    def __init__(self):
        pass

    # BEHAVIOR
    @staticmethod
    def get_length(list1): #local variable
        length = 0  #local variable
        for each in list1:
            length += 1
        return length

print("4. OOPs      : Length of list : ",ListLength.get_length([1,2,3,4,5]))

