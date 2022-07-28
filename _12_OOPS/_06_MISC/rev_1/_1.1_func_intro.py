''''''
'''
State    : Numbers / Bool / String / List / Tuple / Dict /Set /
           other builtin objects or
           user defined objects  ex: madhu = Employee(100,'MadhuN',10000)

Behavior : Functions / Methods
                Decision making (OR)  /
                Loops with CS
                    Operators    x = 10 y = 20  print(x+y)
                    Variables    x = 10   print(x)  # CRUD

REQ : find student exam result based on marks

CRUD             Data types(ip /op)         STATE    BEHAVIOR
--------------------------------------------------------------
1 CRUD       ---> Retrieval
2 Datatype   ---> marks  int    :input
                  result String :output

3.1 STATE    ---> marks int
3.2 BEHAVIOR ---> decision making / functions  / OOPs
'''


# 1st approach :
x = 10     # STATE
#print(x) # BEHAV

marks = 10 # int(input("Enter your marks "))    # STATE

# BEHAVIOR
if marks >= 35:
    print("PASS")
else:
    print("FAIL")

# 2nd aproach :
# STATE
marks = 10 # int(input("Enter your marks  "))

# BEHAVIOR
def get_st_result(st_marks):
    if st_marks >= 35:
        print("PASS")
    else:
        print("FAIL")

print("Student result is : ",get_st_result(marks))

def sum(num1,num2):
    res = num1 + num2
x = 10
y = 20
#print("Sum is  ",sum( x,y))




