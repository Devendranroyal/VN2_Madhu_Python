'''
Convert list of chars to string
'''

chars_list = ['a', 's', 'h', 'a', ' ', 'k', 'a', 's', 'u']

def char_to_str(lst):
    str_name = ''.join(lst)
    return str_name


if __name__ == '__main__':
    print(char_to_str(chars_list))