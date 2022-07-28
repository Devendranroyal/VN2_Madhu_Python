ages = {'max':23,'tim':23,'jim':22}
print(ages.popitem())
variable = 5
def print_function(variable=variable):
    print(variable)
variable=6
print_function(8)
print_function()
print(variable)

x = (1, 2, 3, 4, 5, 6, 7, 8)
print(x[:3])


class world:

    def __init__(wow):
        wow.__newtime()

    def dow(wow):
        print('change your thoughts and you change your world ')

    def __newtime(wow):
        print('Where are you')


x = world()
x.dow()

import copy

A = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
B = copy.copy(A)

A[1][1] = 'AA'

print("A:", A)
print("B:", B)

squares = {x:x*x for x in range(6)}
numbers = [val for val in ["Zero","One","Two"]]
result = list(zip(squares,numbers,squares.items()))
new_result = dict(zip(dict.fromkeys(squares),numbers))
print(result)
print(new_result)

class py:

    def __init__ (self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 1

    def __eq__(self, other):
        return self.a * self.b == other.a * other.b

obj1 = py(4, 5)
obj2 = py(5, 4)
print("DATA",obj1 == obj2)

list1 = [[4,5,6], [1,5,9], [3,5,8]]
list1.append([12])
list1 = list1.copy()
list1.reverse()
list1.pop(1)
list1.sort(key=None, reverse=True)
print(list(zip(*list1)))


class Base(object):
    def taste(m):
        print("Yummy")


class Crust(object):
    def taste(m):
        print("delicious!")


def Food(Dish):
    Dish.taste()


x = Base()
y = Crust()

Food(x)
Food(y)


def myFunc(x, *y):
    return type(y)

b = myFunc(1, 2, 3, 4, 5, 6, 7, 8)
print(b)

import threading
def cube(num):
    print("Cube: {}".format(num * num * num))
def square(num):
    print("Square: {}".format(num * num))

if __name__ == "__main__":
   t1 = threading.Thread(target=square, args=(10,))
   t2 = threading.Thread(target=cube, args=(10,))
   t1.start()
   t2.start()

   t1.join()
   t2.join()

class Run(object):


    # Constructor
    def __init__(boy, why):
        boy.why = "Gump"


    def Identity(boy):
        return boy.why


    def isBoy(boy):
        return False


class Forrest(Run):

    def isBoy(boy):
        return True

x = Run("John")
print(x.Identity(), x.isBoy())

x = Forrest("Abram")
print(x.Identity(), x.isBoy())


class A:
    def __init__(self, val):
        self.val = val
        self._val1 = val
        self._val2 = self._val1
obj=A(10)
print(obj._val2)
print(A.__init__.__repr__)
print(len(obj.__dict__))


class TestClass():
    def __repr__(self):
        return '__repr__ is called'
    def __str__(self):
        return '__str__ is called'

test = TestClass()
print('test')
