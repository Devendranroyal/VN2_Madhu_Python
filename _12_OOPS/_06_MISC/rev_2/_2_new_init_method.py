'''def __new__(cls,*args,**kwargs):
        print(cls)
        print("*args =",*args)
        print("**kwargs =",**kwargs)
  '''
 # http://agiliq.com/blog/2012/06/__new__-python/
# http://spyhce.com/blog/understanding-new-and-init


class Employee(object):
    '''
    def __new__(cls,*args = None,**kwargs = None):
        new_instance = object.__new__(cls,*args,**kwargs)
        setattr(new_instance, 'created_at', datetime.datetime.now())
        return new_instance
    '''
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
        print("INIT gets called")
        print("self IS : ", self)

    def get_grade(self):
        print("-----------inside get method----------")

madhu = Employee(100, 'Madhu Nettem', 90000)


#madhu = Employee()

list1 = [1,2,3]  # CREATE  => list([1,2,3]) # object creation of list structure
print(list1)     # RETRIEVAL
list1.append(10) # UPDATE
del list1        # DELETE


list1 = list([])
print(list1,type(list1))

num = int()
print(num,type(num))
bo = bool()
f_val = float()
str_val = str()
t_val = tuple()
dict1 = dict()
set1 = set()
print(num,f_val,bo, str_val,list1,t_val,dict1,set1)


age = 10 # ==> int(10)
bil = 10.4 # ==> float(10.5)
bool = True # ==> bool(True)
msg = 'hello' # ==> str('Hello')
msg.capitalize()
list1 = [1,2,3] # ==> list([1,2,3])

