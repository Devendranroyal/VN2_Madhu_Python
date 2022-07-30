'''
http://pymbook.readthedocs.io/en/latest/igd.html

Decorator is way to dynamically add some new behavior to some objects.

'''
import functools

#@my_decorator
def fund_transfer(acno,name,amount):
    pass
    
    
    
#print(add(10,20))

def sub(a,b):
    print("----In subtract method-----")
    return a-b

#add(1, 3)
#sub(1, 3)
'''
Step 1 : First class function : my_decorator function will be called and executed by receviing our method name as argument.  
Step 2 : Nested function      : In my_decorator function,nested will be there which will receive our method arguments.
Step 3:  Returnging function  : wrapper function(i.e. nested function)  name will be returnred

wrapper(a,b)
'''

print("-------DECORATOR 2------------")

def my_dec(func):
    @functools.wraps(func)
    def wrapper():
        print("Before decorator")
        func()
        print("After decorator")
    return wrapper()

@my_dec
def func():
    print("I am function")
print(func)

print("-------DECORATOR WITH ARGS---------")

def my_dec_arg(number):
    def my_dec_func(func):
        @functools.wraps(func)
        def wrapper_arg(*args, **kwargs):
            print("Before decorator")
            if(number == 5):
                 print("Not running function")
                 print("DEC NO is :",number)
            else:
                func(*args,**kwargs)
            print("after decorator")
        return wrapper_arg
    return my_dec_func

@my_dec_arg(10)
def func_arg(x, y):
    print("Arguments passed")
    print(x + y)
func_arg(10,20)    

'''
# Without Decorator
def sum(num1,num2):
    if num1 >= 0 and num2 >= 0:
        res = num1 + num2
        return res
    else:
        return "Please enter values >= 0"

def mul(num1, num2):
    res = num1 * num2
    return res
x = 10
y = 20

output = sum(x, y)
print("Output is: ",output)
'''
# With Decorator
def validate_arith(func):
    def wrapper(*args, **kwargs):
        var1 = args[0]
        var2 = args[1]
        if var1 >= 0 and var2 >= 0:
            res = func(*args)  # sum(10,20)
            return res
        else:
            return "Please enter values >= 0"
    return wrapper

@validate_arith
def sum(num1,num2):
        res = num1 + num2
        return res
print(sum(10,20))
'''
1. PI will divide our function call into 2 parts(P1.sum P2. 10,20)
2. Decorator validate_arith() function will be called by PI by passing P1
2. It returns nested function(wrapper) to PI
3. PI will execute wrapper function by passing P2
    3.2 Internally validation will be performed to call the method or not
    3.3 If validation is success, it will call sum(10,20)
        else, will return some error message
'''

@validate_arith
def mul(num1, num2):
    res = num1 * num2
    return res

x = -10
y = 20
output = sum(x, y)
print("SUM Output is :: ", output)
output = mul(x, y)
print("MUL Output is :: ", output)