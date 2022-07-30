'''
@author: madhu
'''
'''
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Pre production  (pre method call)
        if args[0] >= 0 and args[1] >=0:
            result = func(*args, **kwargs)   # add(10, 20)
        else:
            return "Please enter positive numbers"
        # Post production (post method call)
        return result
    return wrapper
'''
def my_decorator(func):   # add
    print("-----Started executing the Decorator---------")
    def wrapper(*args, **kwargs): # wrapper((10,20))
        print("****  Before method call : Perform some pre action ****")
        result = func(*args, **kwargs)   # add(10, 20)
        print("****   After method call : Perform some post action ****")
        return result
    print("-----Stopping executing the Decorator---------")
    return wrapper

@my_decorator  # mediator
def add(a, b):
    print("----In add method-----")
    return a + b

output = add(-10, 20) # required logic   1. add   2. (10,20)
print("Normal add function call :", output)

'''
Part1 : function_name   ===> func  :::  add
Part2 : function_args   ===> *args :::  (10,20)
Part3 : Python will load respective decorator by passing method name as argument and 
        starts executing it
Part4 : PI will receive the nested function(wrapper) complete address(function name)
Part5 : It will execute nested function by passing the arguments which were received in step2
        wrapper(10,20)
Part6 : Nested function(here wrapper()) will be executed and returns the result if any to PI
Part7 : PI will pass the same result to our method call

What is decorator
Purpose of decorator.Advatanges Disadvantages
Python Decorators 
Django Decorators
Did you write any customized decorator
What is the decorator execution sequence if multiple decorators exists
'''

def balance_check(func):
    def wrapper():
        # Before check balance 
        # func_call()
        pass
    return wrapper

@balance_check
def dir_fund_transfer():
    pass
    
@balance_check
def ewallet_fund_transfer():
    pass
@balance_check
def ecommerce_fund_transfer():
    pass

