print("--------else block-------------")
try:
    print("In try block")
except:
    print("In except block")
else:
    print("In else block")
finally:
    print("In finally block")

print("--------Except block-------------")

try:
    print("In try block")
    raise Exception("Sample Exception")
except:
    print("In except block")
else:
    print("In else block")
finally:
    print("In finally block")