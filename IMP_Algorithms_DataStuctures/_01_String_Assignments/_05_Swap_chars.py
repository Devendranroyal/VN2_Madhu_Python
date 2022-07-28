'''
Code to swap character in a string
functionality : Swapping characters in string
Convert String into the list, swap Characters and copy the list into string
input : string
'''
str1 = str(input('Enter a string: '))
print('Enter positions of chars to swap')
char1, char2 = map(int, input().split())


def swap(inp_string, pos1, pos2):
    list1 = []
    for i in inp_string:
        list1.append(i)
    list1[pos1], list1[pos2] = list1[pos2], list1[pos1]
    new_string = ''
    for i in list1:
        new_string += i
    return new_string


print('String before swapping : ', str1)
print('String after swapping : ', swap(str1, char1, char2))
