'''
@classmethod
@staticmethod
@abstractmethod

Decorator : Provides additional functionality for class or method/function
'''
# Division of numbers :
# Appoach1: Implement validation logic inside function
            # Code Pollution
def divide(n1, n2):
    if n2 == 0:
        return "Invalid data"
    res = n1/n2
    return res

#Callers
print("Division result : ", divide(10,0))


# Appoach2: Implement validation logic while calling function
            # Code duplication

# Function def
def divide(n1, n2):
    res = n1/n2
    return res

#Callers
n1 = 10
n2 = 0
if n2 == 0:
    print("Invalid data")
else:
    print("Division result : ", divide(10, 0))

# Solution is use Decorator
print("-----------------------------------------")
def validate_data(func):
    print("I am in decorator", func)
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        if args[1] == 0:
            return "Invalid denominator value"
        else:
            print("-------PRE Activities---------")
            output = func(*args, **kwargs)  # divide(10,4)
            print("-------POST Activities---------")
            return output
    return wrapper  # wrapper(10,4)

@validate_data  # validate_data(divide)
def divide(n1, n2):
    print("----In divide method-----")
    res = n1/n2
    return res

print("Division of numbers : ", divide(10,4)) # divide (10,4)

print("----------------------------------------------------")

def validate(func):
    def wrapper(*args, **kwargs):
        if args[1] != 0:
            output = func(*args, **kwargs)
            return output
        else:
            return "INVALID DENOMINATOR"
    return wrapper

@validate
def divide(n1, n2):
    res = n1 / n2
    return res

print("Division of numbers : ", divide(10, 0)) # divide (10, 0)


def validate_sum(func):
    def wrapper(*args, **kwargs):
        if args[0] >= 0 and args[1] >= 0:
            print("---Before method call----")
            output = func(*args, **kwargs)
            print("---After method call----")
            return output
        else:
            return "INVALID DATA"
    return wrapper

@validate_sum
def sum(n1, n2):
    res = n1 + n2
    return res

print("Sum of 2 numbers : ", sum(10,-5)) # sum (10,-5)