'''
program to sort a string lexicographically
'''
str1 = 'Asha Nikhil'

def lex_string(string):
    list_of_str = []

    for i in string:
        list_of_str.append(i)
    for m,i in enumerate(list_of_str,0):
        for n,j in enumerate(list_of_str,0):
            if ord(i) < ord(j):
                list_of_str[m], list_of_str[n]= list_of_str[n], list_of_str[m]
    return ''.join(list_of_str)
print('Input String : ',str1)
print('Lexical String : "', lex_string(str1),'"')