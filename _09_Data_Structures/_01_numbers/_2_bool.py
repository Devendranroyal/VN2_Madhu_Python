
# 2. BOOLEAN:
is_active = True
print("Are you active ??", is_active, type(is_active))

x = 0
print("Normal value : ", x, type(x))
x = bool(0)
print("Boolean value : ", x, type(x))


x = 1
print("Normal value : ", x, type(x))

x = bool(1)
print("Boolean value : ", x, type(x))

x = False
print(x, type(x))

'''
if False -->  False
if None  -->  False
if 0     -->  False 
    
if True    --> True
if not None -> True
if -5      --> True

You are a good person - You are not a good person 
You are a bad person  - You are not a bad person 
'''