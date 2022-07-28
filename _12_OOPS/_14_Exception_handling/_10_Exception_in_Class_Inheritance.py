'''
@author: madhu
'''

class A(Exception):
    pass
class B(A):
    pass
class C(B):
    pass

for cls in [A, B, C]:
    try:
        raise cls()  # raise A() raise B() raise C()
    except C:           #  C c = A() invalid
        print("C")
    except B:           # B b = A() invalid
        print("B")
    except A:           # A a = A() valid
        print("A")
        
print("----------")

class X(Exception):
    pass
class Y(X):
    pass
class Z(Y):
    pass

for cls in [X,Y,Z]:
    try:
        raise cls()
    except Z:         # ZeroDivisionError
        print("Z")
    except Y:         # ArithmeticError
        print("Y")
    except X:
        print("X")    # Exception
    
    
    '''
    except X:         # Exception
        print("X")
    except Y:         # ArithmeticError
        print("Y")
    except Z:
        print("Z")    # ZeroDivisionError
    '''
