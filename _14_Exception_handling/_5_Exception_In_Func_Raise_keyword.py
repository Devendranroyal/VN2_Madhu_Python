'''
def get_details(x,y):
    if y == 0 or x == 0:
        raise ZeroDivisionError("Please enter valid numerator")
    result = x / y
    return result

def get_info():
    print("Before method call")
    get_details(0,10)
    print("After method call")

print(get_info())
'''

# After exception handling

# Module 3
def get_details(x,y):
    result = 0
    try:
        if y <= 0:
            raise ZeroDivisionError("Please enter valid numerator/denominator")
        result = x / y
        print("Hello World")
    except ZeroDivisionError as zde: # ZeroDivisionError zde = ZeroDivisionError("Please enter valid numerator/denominator")
        print("ERROR :", zde)
    return result

# Module 2
def get_info():
    print("Before method call")
    res = get_details(2,0)
    print("After method call")
    return res

# Module 1
print("Result is :",get_info())

print("-----------------------------")

def m3(n1, n2):
    print("In m3()")
    print(n1/n2)
    '''
    try:
        print(n1/n2)
    except Exception as e:
        print("Exception details : ", e)
    '''
def m2(n1,n2):
    print("In m2()")
    # business logic
    m3(n1, n2)

def m1(n1, n2):
    print("In m1()")
    # business logic
    m2(n1, n2)

m1(10, 0) # Event trigger
print("----------End of program--------------")