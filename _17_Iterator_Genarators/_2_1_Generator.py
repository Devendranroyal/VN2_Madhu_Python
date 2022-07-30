'''
'''
a = [1,2,3,4]
print(a[::-1])
result = [x for x in range(10)]
print(type(result))


#ITERATOR vs Generator
#-----------------------
#http://nvie.com/posts/iterators-vs-generators/


from itertools import islice


#ITERATOR
for c in "python":
    print(c)
    print('------------')

for i in [1,2,3,4]:
    print(i)
    print('------------')

for i in range(10):
    print(i)
    
'''ITERNATION PROTOCOL  :: 
The built-in function iter takes an iterable object and returns an iterator.
    x=iter([1,2,3])
    #x.next()  -- 1
    #x.next() --  2  IF no more elements :: StopIteration
   ''' 
class yrange:
    def __init__(self,n):
        print("in init() method")
        self.i=0;
        self.n=n;  
    def __iter__(self):
        print("in iter() method")
        return self
    def next(self):
        print("in next() method")
        if self.i < self.n:
            i=self.i
            self.i+=1
            return i
        else:
            raise StopIteration()
 
y=yrange(3)
print(y.next())
print(y.next())
print(y.next())
#print(y.next())
#l=list(yrange(5))

result = (x for x in range(10))
print("M",type(result))



val=sum(x*x for x in range(1,3))
print(val)

'''GENERATOR  : Any generator also is an iterator (not vice versa!);
                Any generator, therefore, is a factory that lazily produces values.
'''
print("---------------------Finabocci Series---------------------")
def fib():
    prev, current= 0, 1
    while True:
        yield current   # The return value of the function will be a generator
        prev, current = current, prev+current
        
f=fib()  #the generator (the factory) is instantiated and returned.
         #No code will be executed at this point: 
         #the generator starts in an idle state initially
print("madhu")
#print(f())

print("MAD", list(islice(f, 0, 10)))


'''
islice is an iterator,wrapped inside list.
List wil consume all of its elements and builds list by calling next() on islice instance,which inturn
will start calling next() on our f instance            
'''
'''
2 TYPES OF GENERATORS 
1.GENERATOR FUNCTIONS  : generator function is any function in which the keyword yield appears in its body
2.GENERATOR EXPRESSIONS: generator equivalent of a list/dict/set comprehension
'''
print("---------------------Square of each value---------------------")
# Iterator mechanism
list1 = []
for x in [1,2,3,4,5]:
    list1.append(x*x)

print("Iterator   : ",list1)

# Generator mechanism
#        GENERATOR Expression
#                LIST Comprehension

list1 = [x*x for x in [1,2,3,4,5]]

print("Generator  : ",list1)

'''
Step1 : Python will create empty list 
Step2 : Iterate through sequence and gets first element  
Step3 : value will be given to expression,exuectes the expression
Step4 : Appends output value to empty list

'''

numbers = [1, 2, 3, 4, 5]
s1 = set({})
for x in numbers:
    s1.add(x * x)
print("With for loop  set :", s1)

#SET Comprehension :
s1= {x * x for x in numbers}
print("Set comprehension  :", s1)


#DICTIONARY Comprehension:
numbers = [1,2,3,4,5]
d1  = {}
for x in numbers:
    d1[x] =  x*x
print("With for loop  dict :",d1)

d1 = {x: x*x for x in numbers}

print("Dict comprehennsion :",d1)




#Genreator Expr:
lazy_square=(x*x for x in numbers)
print(lazy_square)
print(next(lazy_square))
print(list(lazy_square))
