'''
program to check whether a string starts with specified characters
'''
str1 = str(input('Enter Input String : '))
specified_chars = str(input('Enter specified chars : '))


def spec_chars(string , sub_str):
    if len(sub_str) <= len(string):
        if string[0:len(sub_str)] == sub_str:
            return True
        else:
            return False
    else:
        return "Insufficient Characters in Input string"


print('Patten matches :',spec_chars(str1, specified_chars))