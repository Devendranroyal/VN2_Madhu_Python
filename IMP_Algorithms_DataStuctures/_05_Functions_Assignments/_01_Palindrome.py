'''
check given word is palindrome or not
'''
str1 = 'racecar'
str2 = 'deleveled'
str3 = 'michigan'
str4 = 'mississauga'


def palindrome(s):
    leng = len(s)
    for i in range(0, int(leng/2)):
        if s[i] == s[-i - 1]:
            pass
        else:
            return False
    return True


if __name__ == '__main__':
    print(str1,' -',palindrome(str1))
    print('{} - {}'.format(str2,palindrome(str2)))
    print('%s - %s'%(str3,palindrome(str3)))
    print(f'{str4} - {palindrome(str4)}')


# def palindrome(s):
#     leng = len(s)
#     if leng % 2 == 0:
#         for i in range(0, int(leng/2)):
#             if s[i] == s[-i - 1]:
#                 pass
#             else:
#                 return False
#     elif leng % 2 != 0:
#         for i in range(0,int(leng/2)):
#             if s[i] == s[-i - 1]:
#                 pass
#             else:
#                 return False
#     return True