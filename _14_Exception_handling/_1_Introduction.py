'''
In 16th line,when python is unable to perform conversion to int,
it will load the respective exception class,will create object with respective message
    ValueError("invalid literal for int() with base 10")
    ZeroDivisionError("division by zero")
Then PI will check whether we handled the exception or not,
==> If we don't handle the exception : It will throw the exception details to console
            ZeroDivisionError("division by zero")
            ValueError("invalid literal for int() with base 10")
==> If we handle the exception : PI will throw the exception which will be received by except block
        ZeroDivisionError zde = ZeroDivisionError("division by zero")
        ValueError ve = ValueError("invalid literal for int() with base 10")

class ZeroDivisionError:
    def __init__(self,message):
        self.message = message
'''
# After exception handling
'''
During exception handling:
- First handle the exception(To continue program execution)
- Display proper message to customer
if    -> only one time execution,if condiation satisfy
elif
else
for   -> till last element in seqnece
while -> till condition satisfies,iterates 
function/method -> when it is being called
class           -> when object is created

try    -> Place the code which cause exception
except -> to handle the exception,print meaningful message
'''
'''
                       Animal
            WildAnimal      DomesticAnimal
        Lion Tiger              Cat Dog
        
        
Tiger tiger = Tiger()       #            2L Can <--- 2L water
Animal anim = Tiger()       # Upcasting  5L Can <--- 2L Water
https://airbrake.io/blog/python/class-hierarchy
            
                Exception 
                   - ArithmeticError
                        - FloatingPointError
                        - OverflowError
                        - ZeroDivisionError
                        
ZeroDivisionError zde = ZeroDivisionError()   #            2L Can <--- 2L water   int x = 10
ArithmeticError   ae = ZeroDivisionError()    # Upcasting  5L Can <--- 2L Water   float x = 10
Exception          e = ZeroDivisionError()    # Upcasting  5L Can <--- 2L Water
                                                           2L Can XXX  5L Water   int x = 10.5
'''


print("---------Handling Exceptions in generic way--------")


try:
    x = int(input("Enter numerator value :"))   # At a time we can handle one exception only
    y = int(input("Enter denominator value:"))
    print(x / y)
    print("Hello world")
except Exception as exc:
    print("EXC : Something is wrong.Please check *** ", exc)
print("Welcome to Python")

'''
Exception exc = ValueError()
Exception exc = ZeroDivisionError()
'''


try:
    list1 = [1, 2, 3]
    print(list1[5])
except IndexError as ie:
    print("Respevide index didnt found **", ie)


try:
    list1 = [1, 2, 3]
    print(list1[5])
except Exception as e:
    print("Respevide index didnt found **", e)