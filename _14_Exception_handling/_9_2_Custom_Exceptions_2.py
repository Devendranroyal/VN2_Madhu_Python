'''
@author: madhu
'''

class AgeError(Exception):
    """Excpetions raised for errors in input
       Attributes:
         Expression : Input expression in which error occured.
         Message    : Explanation of error
    """
    def __init__(self, expression, message):
            self.expression = expression
            self.message = message

class TransitionError(Exception):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """
    
    def __init__(self, previous, next, message):
        self.previous=previous
        self.next=next
        self.message=message
    '''
    def __str__(self, *args, **kwargs):
        return self.previous," ",self.next," ",self.message
    '''
x = 10 
try:  
    if x == 18:
        raise AgeError('IO Error','input out error')
    elif x < 18:
        raise TransitionError('Pr','Ne','Raised Trans Error')
    # Business logic
except Exception as e:
    print("HAndled exception")
    print("Exception details :: ",e)