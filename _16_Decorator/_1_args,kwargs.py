print("--------------For Decorator purpose-----------")
def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
    print("------------")


# Now we can use both *args ,**kwargs to pass arguments to this function :
myFun()
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks", address={'hno':25,'area':'BLR'})
myFun('geeks', 'for', 'geeks', {1:1,2:2,3:3})
