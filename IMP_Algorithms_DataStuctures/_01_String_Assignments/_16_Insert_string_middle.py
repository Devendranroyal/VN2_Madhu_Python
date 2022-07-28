'''
Insert string in middle of another string
'''
import math
str1 = 'red blue'
mid_str = 'Pink'

def insert_string(string, sub_str):
    final_string = ''
    lengths = len(string)
    if lengths%2 == 0:
        final_string = string[0: math.floor(lengths/2)] + sub_str + string[math.floor(lengths/2):]
    else:
        final_string = string[0: math.floor(lengths / 2)] + sub_str + string[math.floor(lengths / 2):]
    return final_string


print(insert_string(str1, mid_str))
