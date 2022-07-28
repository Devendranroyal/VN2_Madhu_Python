'''
@author: madhu
https://docs.python.org/2.7/tutorial/appetite.html
https://docs.python.org/2.7/tutorial/errors.html
'''
# S O L I D principles
class MyClass(object):

    def getDetails(self):
        count = 0
        while True:
            try:
                count += 1
                print(count)
                if count > 3:
                    return 'Account Blocked'
                x = int(input("Please enter number"))
                res = x + 10
                print("Entered value is :",x)
                # .....
                #break
            except (ValueError, TypeError, NameError, OSError):
            # except Exception as e:
                print("Please enter valid input :: ")
            finally:
                print("Finally executed")

my=MyClass()
print(my.getDetails())


print("------------------------------")


from pip._vendor.distlib.compat import raw_input

f = None
try:  
    num1 =int(raw_input("Enter num1"))
    num2 =int(raw_input("Enter num2"))
    result = num1/num2
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except (ZeroDivisionError,IOError) as err:
    print("Exception occured :",err)
else:
    print("Successfully Executed")
finally:
    print("Finally executed")
    f.close()




'''
SC1 : Exception didn't occur
        1. try block will be executed completely.
        2. It will skip except block
        3. else block will be executed
        3. finally block will be executed
SC2 : Exception  occurs
        1. try block will be executed till exception line of code.
           It will stop executing lines of code after exception statement
        2. It will execute except block
        3. skips else block 
        3. finally block will be executed

'''
'''
Exception
    ZeroDivisionError

Animal
  Dog
  Cat 
  
my_list = [1,2,3,4]
1. Animal a = new Animal()       a = Animal()
2. Dog    d = new Dog()          d = Dog()
3. Animal d = new Dog()         -- Upcasting  2L Water into 5L can
4. Dog    d = new Animal()    X -- Downcasting

Specification:
-------------
class Animal:
   m1()
   m2()
class Dog(Animal):
   m2()
   m3()
   m4()
  
Animal a = new Dog()
a.m1()
a.m2()  -- Dog m2()
a.m3()  X
a.m4()  X



'''