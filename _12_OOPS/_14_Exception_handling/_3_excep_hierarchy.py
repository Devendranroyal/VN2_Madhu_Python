
'''
    Exception
    ArithmeticError
    ZeroDivisionError

'''
try:
    x = 'Madhu'
    y = -5
    if y <= 0:
        raise ValueError("Only positive numbers are allowed") # here i am throwing exception manually
    if type(x) != int:
        raise TypeError("Type Error")  # here i am throwing exception manually
except Exception as e:
    print("Exception occured :: ", e)

print("------------------------------------")
try:
    x = -20
    y = 30
    # raise TypeError("Type Error")
    if x < 0 or y < 0:
        raise ArithmeticError("** Negative Values are not allowed **")
    #raise ArithmeticError("A ISSUE")
    #raise ZeroDivisionError("ZDE ISSUE")
except ZeroDivisionError as zde:
    print("In Zero Division Error")
except ArithmeticError as ae:
    print("In Arithmetic Error :: ", ae)
except Exception as e:  # Exception e = TypeError("Value is not proper")    Upcasting
    print("In Exception ")

print("Hello world")

print("----------------------------------------")

try:
    x = 20
    y = 30
    raise ValueError("Value is not proper")
    #raise ZeroDivisionError("ZDE ISSUE")
    #raise ArithmeticError("A ISSUE")

except ZeroDivisionError as zde:  # ZeroDivisionErrorzde zde = ZeroDivisionError("ZDE ISSUE")  2
    print("In Zero Division Error ::", zde)  # XXX ZeroDivisionErrorzde zde = ArithmeticError("A ISSUE")  4
except ArithmeticError as ae:     # ArithmeticError ae = ArithmeticError("A ISSUE")            1
    print("In Arithmetic Error ::", ae)
except Exception as e:  # Exception e = ValueError("Value is not proper")  3
    print("In Exception :: ", e)
print("Hello world")




try:
    pass
except Exception as e:
    print("Exception occured")

#Compiliation Exceptions,Runtime Exceotions

