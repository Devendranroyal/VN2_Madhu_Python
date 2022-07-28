'''
21. Convert a given string to all uppercase
Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

'''
str1 = 'MySterious book'


def upper_count(string):
    upper_chars = 0
    for i in string[0:4]:
        if i.isupper():
            upper_chars += 1  # upper_chars increments with every uppercase letter
    if upper_chars >= 2:
        return string.upper()
    return string


print('Input String : ', str1)
print('Modified String : ', upper_count(str1))
