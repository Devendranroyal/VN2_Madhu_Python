
class NumberException(Exception):
    def __init__(self,message):
        self.messsage = message

'''
  1 first class function
  2 nested function
  3 returning nested function
  4 *args **kwargs
'''
'''
try:
    if n1 < 0 or n2 < 0:
        raise NumberException("Please enter positive number")
except NumberException as ne:
    print(ne)
'''
'''
def validate_numbers(func): # func = sum
    def wrapper(*args,**kwargs):  # *args = n1 n2
        if args[0] >= 0 or args[1] >= 0:
            res = func(*args)  # sum(n1, n2)
            return res
        else:
        raise NumberException("Please enter positive number")
    return wrapper
'''
'''
def validate_numbers(func): # func = sum
    print("----Inside validate_numbers decorator-----")
    def wrapper(*args,**kwargs):  # *args = n1 n2
        print("----Inside wrapper-----")
        if args[0] >= 0 or args[1] >= 0:
            res = func(*args)  # sum(n1, n2)
            return res
        else:
            print("Please enter Positive numbers only")
    return wrapper
'''


def validate_nums(func):  # validate_numbers(sum)
    def wrapper(*args, **kwargs):
        if args[0] >= 0 and args[1] >= 0:
            output = func(*args, **kwargs)  # sum(10,20)
            return output
        else:
            print("Please enter Positive numbers only")
    return wrapper   # wrapper(10,20)

# LAYER2 : SERVICE LAYER
@validate_nums
def sum(num1, num2):     #  business logic
    res = num1 + num2
    return res

# LAYER1 : CONTROLLER LAYER
n1 = int(input("Enter number 1  :"))
n2 = int(input("Enter number 2  :"))        # 1. n1,n2 will come from UI,receive into python code
result = sum(n1, n2)                        # 2. call service layer method and get the end response
print("Sum of given numbers is :", result)  # 4. Return response and display in UI
'''
Step1 : Our function call will be divided into 2 parts
        sum(10,20) ==>      sum                (10,20)
                            1. functionname    2. arguments 

Step2 : Decorator function will be called by passing our function as argument
        validate_nums(sum)
        Decorator function validate_num(sum) will get executed and 
        it returns nested function(wrapper) to python interpreter
Step3 : Python will execute wrapper function by combing arguments
        wrapper + (10,20) ==> wrapper(10,20)
        Here inside it will validate the data 
          If success : performs the method call 
          else       : returns exception message    
'''
@validate_nums
def sub(n1,n2):
    pass
@validate_nums
def mul(n1,n2):
    pass


def validate_den(func):
    def wrapper(*args, **kwargs):
        if args[1] == 0:
            return "Denominator should not be 0"
        output = func(*args, **kwargs)
        return output
    return wrapper


@validate_den
def div(n1, n2):
    res = n1/n2
    return res

print("Division Result is : ", div(10, 0))
