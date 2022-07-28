'''
Count words in a string
functionality : Count no.of words in string
input : string
'''
str1 = 'The radient sun and the half moon'


# convert to list ang git the length of list
def word_count(string):
    list1 = []
    list1 = string.split()
    return len(list1)


print('String is :"', str1, '"')
print('No.of words :', word_count(str1))