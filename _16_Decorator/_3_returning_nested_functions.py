# 3. RETURNING FUNCTIONS
print("---------------3. RETURNING NESTED FUNCTION NAME------------------")

def parent(num):

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    if num == 10:
        return first_child
    else:
        return second_child
    '''
    try:
        assert num == 10
        print("Assertion is True.Continue to execute the remaining code")
        return first_child  # returning function name
    except AssertionError:
        return second_child # returning function name
    finally:
        print("Finally executed")
    '''

f_c = parent(10)

print("*************")
print("Returning function name FC : ", f_c)
print("Executing function FC      : ", f_c())
print("*************")

s_c = parent(11)
print("Returning function name SC : ", s_c)
print("Executing function SC      : ", s_c())

print("-------------------------------------")

def parent1():
    def first_child():
        return "In First Child"
    # return first_child
    msg = first_child()
    return msg

# parent1 = 0x000002C5F8EA3D08
    # first_child = 0x0000020456463E18
x = 10
print(id(x))  # x = 1885629744
print(x)
print("Printing parent1 function : ", parent1)
print("Calling parent1 function : ", parent1())
x = parent1()  # 0x0000020456463E18
print("Printing child1  function : ", x)
# print("Calling child2 function : ", x())
print("Calling child3 function : ", parent1())
# print("Calling child4 function : ", parent1()())