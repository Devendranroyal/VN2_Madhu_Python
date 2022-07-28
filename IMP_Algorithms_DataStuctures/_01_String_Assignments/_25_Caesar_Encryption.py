'''
program to create a Caesar encryption
Caesar encryption is where each letter of a given text is replaced by a letter some fixed
 number of positions down the alphabet
'''
str1 = 'abcdefghij'
shift = int(input('shift positions : '))
char1 = ''


def caesar_fun(string, shift):
    new_str = ''
    for i in range(len(string)):
        char1 = string[i]
        if char1.isupper():
            new_str += chr(((ord(char1) - 65 + shift) % 26 + 65))
        if char1.islower():
            new_str += chr(((ord(char1) - 97 + shift) % 26 + 97))
    return new_str


print(caesar_fun(str1, shift))
