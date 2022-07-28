'''
 True    / False
 Non 0   / 0
 nonNone / None

'''
print("---------1----------")
x = 10 + 20
if x >= 10:
    print("Success", x)
    print("Hello world")

print("---------2----------")
if 10+20 >= 10:
    print("Arithmetic ops")
    print("Comparion ops")

print("---------1 Arithmetic----------")
if 10:
    print("Value is 10")
if 10+20:
    print("Arithmetic ops Addition1 ")

if 10-10:
    print("Arithmetic ops Substraction 1 ")

if 10-20:
    print("Arithmetic ops Substraction 2")

if 10 > 20:
    print("Comparions ops 1")

if 10+20 > 5+10:
    print("Comparions ops 2 ")


print("-------6 Logical--------")
x = True
y = False

if x or y:
    print("Boolean or1")

if False or True:
    print("Boolean or2")

if 10 > 20 or 5 < 10:
    print("Boolean or3")

