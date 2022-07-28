from _10_Functions import my_ops        # (module,  class, function, var)
# from _10_Functions._5_Return_type import data
# print("Data is : ", data())
# from _04_Operators import my_ops
print("From arithmetic : ", my_ops.x)
print("From arithmetic : ", my_ops.e_id)
print("From arithmetic : ", my_ops.e_name)


print("From arithmetic : ", my_ops.get_data())

'''
# from _04_Operators.my_ops import x, e_id, e_name, get_data

print("From arithmetic : ", x)
print("From arithmetic : ", e_id)
print("From arithmetic : ", e_name)
print("From arithmetic : ", get_data())
'''

# Find even or odd
num = 145
if num % 2 == 0:
    print("Even number",num)
else:
    print("Odd number",num)

def get_result(input_no):
    my_ops.find_even_odd(input_no)

if __name__ == '__main__':
    num = int(input("Enter number : "))
    my_ops.find_even_odd(num)
    # get_result(num)