'''
Code to find the length of the string
functionality : return length of string
len() : returns length of string
input : string
'''
str1 = str(input('Enter a string : '))
print('length of ', str1, ' with len(): ', len(str1))
length_of_str = 0
for i in str1:
    length_of_str += 1
print('length of ', str1, ' : ', length_of_str)
