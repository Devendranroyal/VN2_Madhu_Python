print("================ KWARGS ==================")
print("---------Program 1 --------------")
def myFun(**kwargs):
    print(kwargs, type(kwargs))
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun()
myFun(first='Geeks', mid='for', last='Geeks')  # dictionary

print("---------Program 2 --------------")
def myFun(val, **kwargs):
    print("First parameter : ", val)
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
    print("************")

myFun() # Error
myFun(10)
myFun("Hi", first='Geeks', mid='for', last='Geeks')

print("----Program 3---------")
def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

myFun("Geeks", "for", "Geeks")

args = ("Geeks", "for", "Geeks")
myFun(*args)  #myFun("Geeks", "for", "Geeks") Packing unpacking

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)


