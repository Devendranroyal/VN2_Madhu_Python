'''
Append  a list to list
Appending flowers to colors
'''

colors = ['red' , 'yello', 'blue', 'brown', 'pink', 'organge']
flowers = ['rose', 'jasmin', 'crysanthamum', 'lillies', 'dafodils', 'marigold']

# Method1
# colors.extend(flowers)
# print('After appending colors -')
# print(colors)

# Method 2
def append_list(lst1, lst2):
    for i in lst2:
        lst1.append(i)
    return lst1

if __name__ == '__main__':
    print(append_list(colors, flowers))