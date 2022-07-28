# Animal anim = Animal()
# ValueError name = ValueError("Insuff. Funds")
# KeyError name = ValueError("Insuff. Funds") # INVALID

try:
    amt = 6000
    if amt > 5000:
        raise ValueError("Insuff. Funds")  # Raise exception manually
    print("Fund transfer completed successfully")
except ValueError as ve:  # ValueError ve = ValueError("Insuff. Funds")
    print("AN EXCEPTION OCCURED ::", ve)
print("Remaining code")

'''
NameError name = NameError("Insuff. Funds")   2L Can <--- 2L water
'''
'''
In Java, below line is object cration

Java   : NameError name = NameError("Insuff. Funds")
         Employee madhu = Employee(10,'Madhu Nettem',10000)

Python : name = NameError("Insuff. Funds")  # Rem. all scenarios
         NameError name = NameError("Insuff. Funds")   #Exception handling
'''