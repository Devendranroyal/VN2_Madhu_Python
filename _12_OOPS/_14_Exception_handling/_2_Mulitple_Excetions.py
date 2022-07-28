

# Exception vs Error
# https://docs.python.org/3/library/exceptions.html
'''
IndexError     :
KeyError       :
ValueError     :
TypeError      :
SyntaxError    :
NameError      :
ZeroDivisionError :


try:
except:
finally:

'''

'''
finally: To close the things which were opened in try block
open operations: open a file 
                 db connection
                 
    Finally will be executed whether exception occured or not 
    
'''




# Without Exception handling
# 1.ZeroDivisionError
'''
a = int(input("Enter a:"))
b = int(input("Enter b:"))
print("Hello world")
c = a / b    # ZeroDivisionError('division by zero')
print("Result is ", c)
print("Hello world")
# With exception handling
# madhu = Employee(10,'Madhu N',20000)
'''
'''
inx x = 10                        x = 10
String message = "Hello World"    message = "Hello World"
Employee madhu = Employee(...)    madhu = Employee(...)

String message = 10 # ERROR

ZeroDivisionError zde = ZeroDivisionError("division by zero")
'''
print("----------------------------------------------")
try:
    a = int(input("Enter a2:"))  # raise ValueError("invalid literal for int() with base 10")
    b = int(input("Enter b2:"))  # raise ValueError("invalid literal for int() with base 10")
    c = a / b                    # raise ZeroDivisionError("division by zero")
    print("Result is ", c)
except ValueError as ve:        # ValueError ve = ZeroDivisionError("division by zero")  FAIL
    print("Please enter any value")
except ZeroDivisionError as zde:    # ZeroDivisionError zde = ZeroDivisionError("division by zero")
    print("Please enter value other than 0 for b: ",zde)
finally:
    print("Closing operations")

'''
x = 10    =Java=> int x = 10
             madhu = Employee(100,'MadhuN',1000)
    Employee madhu = new  Employee(100,'MadhuN',1000)
                  zde = ZeroDivisionError("division by zero")
ZeroDivisionError zde = ZeroDivisionError("division by zero")

'''
'''
2L 5L can 
1. 2L Can <== 2L water        int x   = 10          SoftEmp semp = SoftEmp()
2. 5L Can <== 5L water        float x = 10.5        Employee emp = Employee()
3. 5L Can <== 2L water        float x = 10          Employee emp = SoftEmp()
                                (implicit casting)   
                                Memory Loss
4. 2L Can <== 5L water X      int x   = (int)10.95   SoftEmp emp = Employee()
                              (explicit casting)  
                              Data Loss

1. SoftEmp semp = SoftEmp()
2. Employee emp = Employee() 
3. Employee emp = SoftEmp()
4. SoftEmp emp = Employee()
'''

'''
Inheritance :
----------------
Employee   5L Can
SoftwareEmployee 2L Can

1. Employee madhu = Employee(100,'Madhu',2000)
2. SEmployee madhu = SEmployee(100,'Madhu',2000)
3. Employee madhu = SEmployee(100,'Madhu',2000)  # Upcasting


4. SEmployee madhu = Employee(100,'Madhu',2000)  # Downcasting X



Animal 
    WildAnimal
            Lion
            Tiger
            Horse
# 1
WildAnimal wa = WildAnimal()
Lion l = Lion()
Tiger t = Tiger()
Horse h = Horse()  

# 2
Animal a = Animal()

#3 
Animal a = WildAnimal()    # 5L Can - 2L Water
Animal a = Lion()
WildAnimal a = Lion()

Lion l = Tiger()  #invalid
Tiger t = Horse()  #invalid

 Exception
    ArithmeticError
            FloatingPointError
            OverflowError
            ZeroDivisionError  
    ValueError       

'''




'''
                Exception 
                   - ArithmeticError
                        - FloatingPointError
                        - OverflowError
                        - ZeroDivisionError
'''
# SC 1: OverflowError occured
try:
    # 10  FloatingPointError
    # 12  OverflowError
    # 15  ZeroDivisionError
    # 17 ArithmeticError
    pass
except FloatingPointError as fpe:  # FloatingPointError fpe =  OverflowError()  XXX
    pass
except OverflowError as ofe:       # OverflowError ofe =  OverflowError()  CORRECT
    pass
except ZeroDivisionError as zde:
    pass
except ArithmeticError as ae:
    pass



# SC 2 When ZeroDivisionError occurs:

try:
    # 10  FloatingPointError
    # 12  OverflowError
    # 14 ArithmeticError
    # 15  ZeroDivisionError
    pass
except FloatingPointError as fpe:      # FloatingPointError fpe =  ZeroDivisionError()  XXX
    pass
except OverflowError as ofe:           # OverflowError ofe =  ZeroDivisionError()         XXX
    pass
except ArithmeticError as ae:          # ArithmeticError ae = ZeroDivisionError()  #Executes this
    pass
except ZeroDivisionError as zde:      # ZeroDivisionError zde = ZeroDivisionError()
    pass
'''
In above scenario, write ArithmeticError at last

except FloatingPointError as fpe:
    pass
except OverflowError as ofe:   
    pass
except ZeroDivisionError as zde:
    pass
except ArithmeticError as ae:          # ArithmeticError ae = ZeroDivisionError()  #Executes this
    pass
'''

# SC 3

try:
    # 10  FloatingPointError
    # 12  OverflowError
    # 15  ZeroDivisionError
    # 16 ArithmeticError
    pass
except ArithmeticError as ae:   #  ArithmeticError ae = FloatingPointError()   5L Can <-- 1L Water
    pass                        #  ArithmeticError ae = OverflowError()        5L Can <-- 2L Water
                                #  ArithmeticError ae = ZeroDivisionError()    5L Can <-- 3L Water
                                #  ArithmeticError ae = ArithmeticError()      5L Can <-- 5L Water

'''
If any other exception may occur:
except Exception as e:
    pass
'''


# SC 4
try:
    # 10  KeyError
    # 12  IndexError
    # 15  ZeroDivisionError
    # 18  ValueError
    pass
except Exception as ex:                       # Exception ex = KeyError()
    print("Exception details : ", ex)
finally:
    pass

try:
    # 10  ArithmeticError
    # 12  BufferError
    # 15  OSError
    pass
except Exception as ex:
    pass
finally:
    pass

'''
Polygon p = new Triange()
Polygon p = new Quadrialteral()
Polygon p = new Hexagon()
Polygon p = new PEntagon()

Exception
    - ArithmeticError
          - FloatingPointError
          - OverflowError
          - ZeroDivisionError
    - AssertionError
    - ImportError
    - NameError
    - OSError
    - RuntimeError
    - TypeError
    - ValueError
    - Warning
  
'''


