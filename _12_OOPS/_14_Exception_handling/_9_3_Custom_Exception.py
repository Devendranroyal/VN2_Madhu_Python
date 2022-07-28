'''
@author: madhu
'''

from pip._vendor.distlib.compat import raw_input


class WithDrawException(Exception):  
    def __init__(self, data):  
        self.data = data

    def __str__(self):  
        return repr(self.data)  
  
try:
    amount = int(raw_input("Enter your Amount to withdraw : "))    
    print("Your entered amount is ", amount)
    if amount == 100 or amount == 200 or amount == 500 or amount == 2000 or amount%500 == 0:
        print("You can withdraw Amount ",amount)
    else:
        raise WithDrawException(amount)  
except WithDrawException as custExec:  
    print("Please enter amount multiples of 500 and not :", custExec)
finally:
    print("Your current transaction process completed")
