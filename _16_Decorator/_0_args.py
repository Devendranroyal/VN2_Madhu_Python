# https://www.geeksforgeeks.org/args-kwargs-python/
# *ARGS

print("----Program 1 -------------")


def my_fun(*args):
    print(args, "----", type(args))
    for val in args:
        print(val)
    print("*******")

my_fun()  # my_fun ()
my_fun('Hello', 'Welcome', 'to', 'Geeks for Geeks')
my_fun(1, 2, 3, 4, 5)
my_fun(1, 2.4, 'Madhu', True, [1, 2, 3], (1, 2, 3), {1:1, 2:2}, {11, 2, 3})



print("-------Program 2----------------")
def myFun(val, *args):
    print("First argument :", val, "------", args)
    for arg in args:
        print("Next argument through *argv :", arg)

# myFun() ERROR
myFun(100)
myFun(100, 'Madhu Nettem')
myFun('', 'Welcome', 'to', 'GeeksforGeeks')

