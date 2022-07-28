'''
Reverses a string if it's length is a multiple of 4
'''

str1 = 'Vibrant colours on Sunny Day'


def revv(string):
    new_str = ''
    if len(string)%4 == 0:
        new_str = string[::-1]
    else:
        new_str = string
    return new_str


print(revv(str1))
print(len(str1))