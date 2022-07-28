
# REQ: Find length of the string

  # 1. STATE
str1 = 'hello world'

  # 2.BEHAVIOR
def find_length(in_str):
    le = 0
    for char in in_str:
        le += 1
    return le


print("Length of string : ", find_length(str1))
str1 = str1 + 'python world'
print("Length of string : ", find_length(str1))
# Here the state variable str1 can be accessed and modified by anyone in entire project
# Solution is , combine both state and behavior and configure in a single entity(i.e, class)

