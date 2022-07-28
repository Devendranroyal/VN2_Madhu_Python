# scope of variable  LEGB Rule in python 

x = 100
print("Value of x1 :", x)

def get_data():
    # print("Value of x2 :", x)
    x = 25
    a = 10
    print("Value of x3 :", x, a)

get_data()

print("Value of x4 :", x)

